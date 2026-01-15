from __future__ import annotations

import argparse
import json
import re
import unicodedata
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import yaml

from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id
from scripts.knowledge_graph_builder.builders.alignment import (
    AlignmentThresholds,
    ConceptAligner,
    prioritize_alignments,
)
from scripts.knowledge_graph_builder.models import ConceptNode, Dimension, DivinationSystem, SourceNodeRef


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = text.replace("\u3000", " ").strip()
    text = re.sub(r"\s+", " ", text)
    return text


def sanitize_id(raw_id: str) -> str:
    result: List[str] = []
    for char in (raw_id or "").lower():
        if char.isascii() and (char.isalnum() or char == "_"):
            result.append(char)
        elif char in "-. ":
            result.append("_")
        elif not char.isascii():
            result.append(f"u{ord(char):04x}")
        else:
            result.append("_")
    sanitized = "".join(result)
    sanitized = re.sub(r"_+", "_", sanitized).strip("_")
    return sanitized or "unknown"


def infer_divination_system(book_id: str) -> DivinationSystem:
    bid = (book_id or "").lower()
    if any(k in bid for k in ["滴天髓", "子平真诠", "穷通宝鉴", "三命通会", "渊海子平"]):
        return DivinationSystem.BAZI
    if "紫微" in book_id:
        return DivinationSystem.ZIWEI
    if any(k in bid for k in ["astro", "planet", "tetrabiblos", "inner_sky", "house"]):
        return DivinationSystem.ASTRO
    if any(k in bid for k in ["tarot", "thoth", "waite", "degrees_of_wisdom"]):
        return DivinationSystem.TAROT
    if any(k in bid for k in ["dream", "周公解梦", "梦林玄解"]):
        return DivinationSystem.DREAM
    if "周易" in book_id or "yijing" in bid:
        return DivinationSystem.YIJING
    if any(k in bid for k in ["archetype", "unconscious"]):
        return DivinationSystem.PSYCHOLOGY
    return DivinationSystem.CROSS_SYSTEM


@dataclass(frozen=True)
class NormalizedEntry:
    entry_id: str
    book_id: str
    node_id: str
    source_ref: str
    snippet_ids: List[str]
    role: str
    condition: Optional[str]
    summary_raw: str
    summary_norm: str
    factor_refs: List[str]


def iter_logic_chain_entries(path: Path, *, max_nodes: Optional[int] = None) -> Iterable[NormalizedEntry]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    book_id = path.stem
    nodes = data.get("nodes") or []
    count = 0
    for node in nodes:
        if max_nodes is not None and count >= max_nodes:
            break
        node_id = str(node.get("node_id") or "")
        if not node_id:
            continue
        meta = node.get("metadata") or {}
        source_ref = str(meta.get("source_ref") or "")
        snippet_ids = [str(s) for s in (node.get("snippet_ids") or [])]
        role = str(node.get("role") or "")
        condition = node.get("condition")
        summary_raw = str(node.get("summary") or "")
        summary_norm = normalize_text(summary_raw)
        factor_refs = [str(x) for x in (node.get("factor_refs") or [])]
        entry_id = f"entry_{sanitize_id(book_id)}_{sanitize_id(node_id)}"
        yield NormalizedEntry(
            entry_id=entry_id,
            book_id=book_id,
            node_id=node_id,
            source_ref=source_ref,
            snippet_ids=snippet_ids,
            role=role,
            condition=str(condition) if condition is not None else None,
            summary_raw=summary_raw,
            summary_norm=summary_norm,
            factor_refs=factor_refs,
        )
        count += 1


def load_default_books() -> List[str]:
    return ["滴天髓", "子平真诠", "tetrabiblos"]


def resolve_book_files(logic_dir: Path, books: List[str]) -> List[Path]:
    by_stem: Dict[str, Path] = {p.stem: p for p in sorted(logic_dir.glob("*.yaml"))}
    resolved: List[Path] = []
    for book in books:
        if book in by_stem:
            resolved.append(by_stem[book])
    return resolved


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def build_concepts(entries: List[NormalizedEntry]) -> List[ConceptNode]:
    concepts: List[ConceptNode] = []
    for entry in entries:
        concept_id = f"concept_{sanitize_id(entry.book_id)}_{sanitize_id(entry.node_id)}"
        concepts.append(
            ConceptNode(
                concept_id=concept_id,
                canonical_label_zh=entry.summary_norm[:80] or entry.summary_raw[:80] or entry.node_id,
                divination_system=infer_divination_system(entry.book_id),
                dimension=Dimension.GENERAL,
                source_nodes=[
                    SourceNodeRef(
                        book_id=entry.book_id,
                        node_id=entry.node_id,
                        snippet_ids=entry.snippet_ids,
                    )
                ],
                factor_refs=entry.factor_refs,
                authority_score=0.5,
            )
        )
    return concepts


def build_alignment_report(
    *,
    candidates,
    concept_index: Dict[str, ConceptNode],
    source_ref_index: Dict[str, str],
    version_id: str,
    corpus_release_id: str,
) -> dict:
    items = []
    for c in candidates:
        a = concept_index.get(c.concept_a_id)
        b = concept_index.get(c.concept_b_id)
        if not a or not b:
            continue
        a_src = a.source_nodes[0]
        b_src = b.source_nodes[0]
        items.append(
            {
                "concept_a_id": c.concept_a_id,
                "concept_b_id": c.concept_b_id,
                "book_a": a_src.book_id,
                "node_a": a_src.node_id,
                "snippet_ids_a": a_src.snippet_ids,
                "source_ref_a": source_ref_index.get(f"{a_src.book_id}::{a_src.node_id}", ""),
                "book_b": b_src.book_id,
                "node_b": b_src.node_id,
                "snippet_ids_b": b_src.snippet_ids,
                "source_ref_b": source_ref_index.get(f"{b_src.book_id}::{b_src.node_id}", ""),
                "alignment_method": c.alignment_method,
                "confidence": c.confidence,
                "factor_overlap_score": c.factor_overlap_score,
                "text_similarity_score": c.text_similarity_score,
                "combined_score": c.combined_score,
                "shared_factors": list(c.shared_factors),
                "is_false_positive": c.is_false_positive,
                "false_positive_reason": c.false_positive_reason,
            }
        )
    return {
        "report_id": f"alr_{version_id}_{corpus_release_id}",
        "generated_at": utc_now_iso(),
        "version_id": version_id,
        "corpus_release_id": corpus_release_id,
        "total_candidates": len(items),
        "items": items,
    }


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Run text normalization + alignment (asset-gate ready)")
    p.add_argument("--logic-chains-dir", default="data/logic_chains")
    p.add_argument("--output-dir", default="artifacts/text_normalization_alignment")
    p.add_argument("--books", default=",".join(load_default_books()))
    p.add_argument(
        "--max-nodes-per-book",
        type=int,
        default=200,
        help="Max nodes per book (0 means no limit; default: 200 for determinism/speed)",
    )
    p.add_argument("--max-alignments", type=int, default=2000)
    return p


def main() -> int:
    args = build_parser().parse_args()
    logic_dir = Path(args.logic_chains_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    version_id = resolve_version_id()
    corpus_release_id = resolve_corpus_release_id()

    books = [b.strip() for b in (args.books or "").split(",") if b.strip()]
    files = resolve_book_files(logic_dir, books) if books else []
    if not files:
        raise SystemExit(f"No logic chain files found for books={books} under {logic_dir}")

    max_nodes = args.max_nodes_per_book
    if max_nodes <= 0:
        max_nodes = None

    entries: List[NormalizedEntry] = []
    source_ref_index: Dict[str, str] = {}
    for fp in files:
        for entry in iter_logic_chain_entries(fp, max_nodes=max_nodes):
            entries.append(entry)
            source_ref_index[f"{entry.book_id}::{entry.node_id}"] = entry.source_ref

    normalized_path = output_dir / "normalized_entries.jsonl"
    write_jsonl(normalized_path, (asdict(e) for e in entries))

    summary = {
        "generated_at": utc_now_iso(),
        "version_id": version_id,
        "corpus_release_id": corpus_release_id,
        "books": books,
        "files": [str(p) for p in files],
        "max_nodes_per_book": max_nodes,
        "max_alignments": args.max_alignments,
        "total_entries": len(entries),
    }
    write_json(output_dir / "normalization_summary.json", summary)

    concepts = build_concepts(entries)
    concept_index = {c.concept_id: c for c in concepts}

    aligner = ConceptAligner(thresholds=AlignmentThresholds())
    candidates = aligner.find_alignments(concepts, max_candidates=args.max_alignments)
    candidates = prioritize_alignments(candidates)

    report = build_alignment_report(
        candidates=candidates,
        concept_index=concept_index,
        source_ref_index=source_ref_index,
        version_id=version_id,
        corpus_release_id=corpus_release_id,
    )
    write_json(output_dir / "alignment_report.json", report)

    # human-readable summary (minimal)
    md_lines = [
        "# Text Normalization + Alignment Report",
        "",
        f"- generated_at: {report['generated_at']}",
        f"- version_id: {version_id}",
        f"- corpus_release_id: {corpus_release_id}",
        f"- total_candidates: {report['total_candidates']}",
        "",
        "## Top alignments (first 50)",
        "",
    ]
    for item in report["items"][:50]:
        md_lines.extend(
            [
                f"### {item['concept_a_id']} ↔ {item['concept_b_id']}",
                f"- A: {item['book_a']} / {item['node_a']} / {item['snippet_ids_a']}",
                f"- B: {item['book_b']} / {item['node_b']} / {item['snippet_ids_b']}",
                f"- method: {item['alignment_method']}",
                f"- confidence: {item['confidence']:.3f}",
                "",
            ]
        )
    (output_dir / "alignment_report.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    # minimal validation: ensure report is locatable
    if report["total_candidates"] > 0:
        sample = report["items"][0]
        if not sample["book_a"] or not sample["node_a"]:
            raise SystemExit("Alignment report missing locators (book/node)")

    print(str(output_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

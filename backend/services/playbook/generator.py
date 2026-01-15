"""
Playbook Generator

Minimal deterministic playbook generator used by:
- API routes
- unit tests (backend/services/playbook/tests)

This implementation is intentionally lightweight: in production it can be
extended to use real engines and corpora, but it must remain boot-safe.
"""

from __future__ import annotations

import uuid
from dataclasses import asdict, dataclass, field
from datetime import date
from enum import Enum
from typing import Any, Optional

from backend.services.playbook.cache import PlaybookCache


class PlaybookType(str, Enum):
    DAILY = "day"
    WEEKLY = "week"
    MONTHLY = "month"
    YEARLY = "year"


@dataclass(frozen=True)
class PlaybookSection:
    title: str
    content: str
    dimension: str
    score: float


@dataclass(frozen=True)
class Playbook:
    playbook_id: str
    user_id: str
    playbook_type: PlaybookType
    date_range: str
    title: str
    summary: str
    sections: list[PlaybookSection] = field(default_factory=list)
    advice: list[str] = field(default_factory=list)
    lucky_elements: list[str] = field(default_factory=list)
    overall_score: float = 0.0


def _to_dict(playbook: Playbook) -> dict[str, Any]:
    data = asdict(playbook)
    data["playbook_type"] = playbook.playbook_type.value
    return data


def _from_dict(data: dict[str, Any]) -> Playbook:
    sections = [PlaybookSection(**s) for s in (data.get("sections") or [])]
    return Playbook(
        playbook_id=data["playbook_id"],
        user_id=data["user_id"],
        playbook_type=PlaybookType(data["playbook_type"]),
        date_range=data["date_range"],
        title=data["title"],
        summary=data["summary"],
        sections=sections,
        advice=list(data.get("advice") or []),
        lucky_elements=list(data.get("lucky_elements") or []),
        overall_score=float(data.get("overall_score") or 0.0),
    )


class PlaybookGenerator:
    def __init__(self, cache: Optional[PlaybookCache] = None):
        self._cache = cache or PlaybookCache()

    def invalidate_cache(self, user_id: str) -> int:
        return self._cache.invalidate_user(user_id)

    def generate(
        self,
        *,
        user_id: str,
        playbook_type: PlaybookType,
        target_date: Optional[date] = None,
        use_cache: bool = True,
    ) -> Playbook:
        d = target_date or date.today()
        date_range = self._format_date_range(d, playbook_type)
        cache_key = self._cache.make_key(user_id, playbook_type.value, date_range)

        if use_cache:
            cached = self._cache.get(cache_key)
            if isinstance(cached, Playbook):
                return cached
            if isinstance(cached, dict):
                return _from_dict(cached)

        playbook = self._build_playbook(user_id=user_id, playbook_type=playbook_type, date_range=date_range)

        if use_cache:
            self._cache.set(cache_key, _to_dict(playbook), playbook_type=playbook_type.value)

        return playbook

    def _format_date_range(self, d: date, playbook_type: PlaybookType) -> str:
        if playbook_type == PlaybookType.DAILY:
            return d.isoformat()
        if playbook_type == PlaybookType.WEEKLY:
            iso = d.isocalendar()
            return f"{iso.year}-W{iso.week:02d}"
        if playbook_type == PlaybookType.MONTHLY:
            return f"{d.year}-{d.month:02d}"
        if playbook_type == PlaybookType.YEARLY:
            return f"{d.year}"
        return d.isoformat()

    def _build_playbook(self, *, user_id: str, playbook_type: PlaybookType, date_range: str) -> Playbook:
        pb_id = f"pb_{uuid.uuid4().hex[:12]}"

        sections = [
            PlaybookSection(title="事业运势", content="事业运势整体平稳，适合稳扎稳打。", dimension="事业", score=78.0),
            PlaybookSection(title="财富运势", content="财富运势中等偏上，注意控制冲动消费。", dimension="财富", score=75.0),
            PlaybookSection(title="感情运势", content="感情运势温和，沟通将带来更多理解。", dimension="感情", score=72.0),
            PlaybookSection(title="健康运势", content="健康运势良好，保持规律作息会更佳。", dimension="健康", score=80.0),
        ]

        overall = round(sum(s.score for s in sections) / len(sections), 2)

        title = {
            PlaybookType.DAILY: "每日运势",
            PlaybookType.WEEKLY: "每周运势",
            PlaybookType.MONTHLY: "每月运势",
            PlaybookType.YEARLY: "年度运势",
        }.get(playbook_type, "运势报告")

        summary = f"{title}：整体运势指数 {overall:.0f}/100，保持节奏，稳中求进。"

        advice = [
            "专注一件最重要的事，避免分散注意力。",
            "把重要沟通前置，减少误解成本。",
        ]

        lucky_elements = ["幸运色：蓝", "幸运数字：6", "幸运方位：东南"]

        return Playbook(
            playbook_id=pb_id,
            user_id=user_id,
            playbook_type=playbook_type,
            date_range=date_range,
            title=title,
            summary=summary,
            sections=sections,
            advice=advice,
            lucky_elements=lucky_elements,
            overall_score=overall,
        )


from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class LicenseConstraint(BaseModel):
    license_id: str = Field(..., min_length=1)
    allowed_use: List[str] = Field(default_factory=list)
    restrictions: List[str] = Field(default_factory=list)
    attribution_required: bool = False
    notes: Optional[str] = None


class CorpusAsset(BaseModel):
    asset_id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    path: str = Field(..., min_length=1)
    kind: str = Field(default="directory")  # directory|file
    source: str = Field(..., min_length=1)
    license_id: str = Field(..., min_length=1)
    derived_from: List[str] = Field(default_factory=list)
    release_included: bool = True
    notes: Optional[str] = None

    # compiled fields (optional)
    digest: Optional[str] = None
    digest_algorithm: Optional[str] = None
    size_bytes: Optional[int] = None
    file_count: Optional[int] = None


class CorpusManifest(BaseModel):
    manifest_id: str = Field(..., min_length=1)
    manifest_version: str = Field(..., min_length=1)
    corpus_name: str = Field(..., min_length=1)

    version_id: Optional[str] = None
    corpus_release_id: Optional[str] = None
    generated_at: Optional[str] = None

    licenses: List[LicenseConstraint] = Field(default_factory=list)
    assets: List[CorpusAsset] = Field(default_factory=list)


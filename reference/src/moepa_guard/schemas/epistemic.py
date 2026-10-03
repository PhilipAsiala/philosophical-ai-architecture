"""Probabilistic claims. These objects are not entities and cannot be committed."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, model_validator


class EpistemicState(StrEnum):
    """Distinct warrant states. Ignorance is not a low probability."""

    BELIEF = "belief"
    DEFEATER = "defeater"
    IGNORANCE = "ignorance"


class EpistemicClaim(BaseModel):
    """A proposal about a proposition: score, evidence, and provenance.

    ``confidence`` is null when the state is ignorance. A distribution, when
    present, is continuous input to state collapse. It is not an existence bit.
    """

    model_config = ConfigDict(extra="forbid")

    claim_id: str = Field(min_length=1)
    proposition: str = Field(min_length=1)
    state: EpistemicState
    confidence: float | None = Field(default=None, ge=0, le=1)
    distribution: dict[str, float] | None = None
    evidence_links: list[str] = Field(default_factory=list)
    source_provenance: list[str] = Field(default_factory=list)
    defeaters: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _state_matches_score(self) -> EpistemicClaim:
        if self.state is EpistemicState.IGNORANCE:
            if self.confidence is not None or self.distribution is not None:
                raise ValueError("ignorance carries no confidence and no distribution")
        elif self.confidence is None:
            raise ValueError("belief and defeater claims require a confidence")
        if self.state is EpistemicState.DEFEATER and not self.defeaters:
            raise ValueError("a defeater claim names at least one defeater")
        if self.distribution is not None:
            if not self.distribution:
                raise ValueError("distribution must be non-empty when set")
            if any(weight < 0 for weight in self.distribution.values()):
                raise ValueError("distribution weights must be non-negative")
        return self


class MetrologyTelemetry(BaseModel):
    """Continuous measurement attached to a proposal. Not a permission."""

    model_config = ConfigDict(extra="forbid")

    confidence: float = Field(ge=0, le=1)
    uncertainty: float = Field(ge=0)
    error_bound: float = Field(ge=0)
    calibration_id: str = Field(min_length=1)

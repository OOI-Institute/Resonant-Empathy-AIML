from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

ClaimSource = Literal["explicit", "inferred", "model_knowledge"]


def _bounded_probability(value: float) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    return float(value)


@dataclass(frozen=True)
class Observation:
    """Evidence available to the system about a human-relevant state.

    REL accepts structured observations so the reference implementation can test
    representation safety without pretending to solve natural-language mind reading.
    """

    id: str
    attribute: str
    value: Any
    explicit: bool = True
    confidence: float = 1.0
    context: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("observation id must be non-empty")
        if not self.attribute.strip():
            raise ValueError("attribute must be non-empty")
        object.__setattr__(self, "confidence", _bounded_probability(self.confidence))


@dataclass(frozen=True)
class StateClaim:
    attribute: str
    value: Any
    source: ClaimSource
    confidence: float
    evidence_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "confidence", _bounded_probability(self.confidence))
        if self.source != "model_knowledge" and not self.evidence_ids:
            raise ValueError("human-state claims must retain supporting evidence ids")


@dataclass
class RelationalRepresentation:
    """A bounded representation of another actor, not the actor's true state."""

    claims: dict[str, StateClaim] = field(default_factory=dict)
    unresolved: set[str] = field(default_factory=set)

    def explicit(self, attribute: str) -> StateClaim | None:
        claim = self.claims.get(attribute)
        return claim if claim and claim.source == "explicit" else None

    def inferred(self, attribute: str) -> StateClaim | None:
        claim = self.claims.get(attribute)
        return claim if claim and claim.source == "inferred" else None

    def model_knowledge(self, attribute: str) -> StateClaim | None:
        claim = self.claims.get(attribute)
        return claim if claim and claim.source == "model_knowledge" else None

    def by_source(self, source: ClaimSource) -> dict[str, StateClaim]:
        return {key: claim for key, claim in self.claims.items() if claim.source == source}

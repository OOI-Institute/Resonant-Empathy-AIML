from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Iterable

from .models import Observation, StateClaim


@dataclass(frozen=True)
class OverInferenceFinding:
    attribute: str
    reason: str


class OverInferenceDetector:
    """Detects human-state claims that outrun their declared evidence."""

    def inspect(
        self,
        claims: Iterable[StateClaim],
        observations: Iterable[Observation],
    ) -> list[OverInferenceFinding]:
        evidence = {item.id: item for item in observations}
        findings: list[OverInferenceFinding] = []

        for claim in claims:
            if claim.source == "model_knowledge":
                continue
            linked = [evidence[item_id] for item_id in claim.evidence_ids if item_id in evidence]
            if not linked:
                findings.append(OverInferenceFinding(claim.attribute, "missing supporting evidence"))
                continue
            max_support = max(item.confidence for item in linked)
            if claim.confidence > max_support + 1e-12:
                findings.append(
                    OverInferenceFinding(
                        claim.attribute,
                        "claim confidence exceeds strongest supporting observation",
                    )
                )
            if claim.source == "explicit" and not any(item.explicit for item in linked):
                findings.append(
                    OverInferenceFinding(claim.attribute, "claim labeled explicit without explicit evidence")
                )
        return findings

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .metrics import perspective_separation, representation_fidelity
from .models import RelationalRepresentation


@dataclass(frozen=True)
class EvaluationReport:
    representation_fidelity: float
    perspective_separation: float
    unresolved_attributes: int


class RELEvaluator:
    def evaluate(
        self,
        representation: RelationalRepresentation,
        ground_truth: dict[str, Any],
    ) -> EvaluationReport:
        predicted = {
            key: claim.value
            for key, claim in representation.claims.items()
            if claim.source != "model_knowledge"
        }
        return EvaluationReport(
            representation_fidelity=representation_fidelity(predicted, ground_truth),
            perspective_separation=perspective_separation(representation.claims.values()),
            unresolved_attributes=len(representation.unresolved),
        )

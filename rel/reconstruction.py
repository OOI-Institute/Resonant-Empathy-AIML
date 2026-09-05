from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable

from .models import ClaimSource, Observation, RelationalRepresentation, StateClaim


class RELModel:
    """Deterministic reference reconstructor.

    It deliberately does not infer latent psychology. It turns supplied structured
    observations into source-labelled claims and preserves uncertainty.
    """

    def reconstruct(self, observations: Iterable[Observation]) -> RelationalRepresentation:
        grouped: dict[str, list[Observation]] = defaultdict(list)
        for observation in observations:
            grouped[observation.attribute].append(observation)

        representation = RelationalRepresentation()
        for attribute, evidence in grouped.items():
            explicit = [item for item in evidence if item.explicit]
            candidates = explicit or evidence
            strongest = max(candidates, key=lambda item: item.confidence)
            source: ClaimSource = "explicit" if strongest.explicit else "inferred"
            representation.claims[attribute] = StateClaim(
                attribute=attribute,
                value=strongest.value,
                source=source,
                confidence=strongest.confidence,
                evidence_ids=tuple(item.id for item in candidates),
            )

            values = {repr(item.value) for item in candidates}
            if len(values) > 1:
                representation.unresolved.add(attribute)

        return representation

    def add_model_knowledge(
        self,
        representation: RelationalRepresentation,
        attribute: str,
        value: object,
        confidence: float = 1.0,
    ) -> None:
        representation.claims[f"model::{attribute}"] = StateClaim(
            attribute=attribute,
            value=value,
            source="model_knowledge",
            confidence=confidence,
            evidence_ids=(),
        )

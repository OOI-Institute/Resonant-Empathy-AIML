from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from typing import Any

from .models import StateClaim


def representation_fidelity(predicted: Mapping[str, Any], truth: Mapping[str, Any]) -> float:
    if not truth:
        return 1.0
    matched = sum(1 for key, value in truth.items() if predicted.get(key) == value)
    return matched / len(truth)


def perspective_separation(claims: Iterable[StateClaim]) -> float:
    claims_list = list(claims)
    if not claims_list:
        return 1.0
    properly_sourced = sum(
        1
        for claim in claims_list
        if claim.source == "model_knowledge" or bool(claim.evidence_ids)
    )
    return properly_sourced / len(claims_list)


def unsupported_inference_rate(claims: Iterable[StateClaim]) -> float:
    inferred = [claim for claim in claims if claim.source == "inferred"]
    if not inferred:
        return 0.0
    unsupported = sum(1 for claim in inferred if not claim.evidence_ids)
    return unsupported / len(inferred)


def preservation_score(expected: Mapping[str, Any], actual: Mapping[str, Any]) -> float:
    return representation_fidelity(actual, expected)


def brier_score(probabilities: Sequence[float], outcomes: Sequence[int]) -> float:
    if len(probabilities) != len(outcomes):
        raise ValueError("probabilities and outcomes must have equal length")
    if not probabilities:
        return 0.0
    for probability in probabilities:
        if not 0.0 <= probability <= 1.0:
            raise ValueError("probabilities must be between 0 and 1")
    for outcome in outcomes:
        if outcome not in (0, 1):
            raise ValueError("outcomes must be binary")
    return sum((p - y) ** 2 for p, y in zip(probabilities, outcomes, strict=True)) / len(outcomes)

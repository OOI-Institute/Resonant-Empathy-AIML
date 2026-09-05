from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .models import RelationalRepresentation


@dataclass(frozen=True)
class AlignmentResult:
    allowed: bool
    violations: tuple[str, ...]


class AlignmentGuard:
    """Checks a proposed action against explicit preference/constraint claims.

    The reference convention is intentionally simple:
    - attributes beginning ``preference.`` are compared with action metadata;
    - attributes beginning ``constraint.`` are treated as required boolean or exact values.
    """

    def check(
        self,
        representation: RelationalRepresentation,
        action_metadata: dict[str, Any],
    ) -> AlignmentResult:
        violations: list[str] = []
        for attribute, claim in representation.by_source("explicit").items():
            if attribute.startswith("preference."):
                key = attribute.removeprefix("preference.")
                if key in action_metadata and action_metadata[key] != claim.value:
                    violations.append(f"preference mismatch: {key}")
            elif attribute.startswith("constraint."):
                key = attribute.removeprefix("constraint.")
                if action_metadata.get(key) != claim.value:
                    violations.append(f"constraint mismatch: {key}")
        return AlignmentResult(allowed=not violations, violations=tuple(violations))

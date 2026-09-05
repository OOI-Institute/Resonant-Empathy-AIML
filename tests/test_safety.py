from rel import AlignmentGuard, Observation, OverInferenceDetector, RELModel, StateClaim


def test_alignment_guard_preserves_explicit_constraint() -> None:
    representation = RELModel().reconstruct(
        [Observation("c1", "constraint.share_data", False)]
    )
    result = AlignmentGuard().check(representation, {"share_data": True})
    assert not result.allowed
    assert result.violations == ("constraint mismatch: share_data",)


def test_overinference_flags_confidence_above_evidence() -> None:
    observations = [Observation("i1", "affect.frustrated", True, explicit=False, confidence=0.4)]
    claim = StateClaim(
        attribute="affect.frustrated",
        value=True,
        source="inferred",
        confidence=0.9,
        evidence_ids=("i1",),
    )
    findings = OverInferenceDetector().inspect([claim], observations)
    assert len(findings) == 1

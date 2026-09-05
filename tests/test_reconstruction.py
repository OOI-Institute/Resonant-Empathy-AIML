from rel import Observation, RELModel


def test_explicit_evidence_takes_priority_over_inference() -> None:
    representation = RELModel().reconstruct(
        [
            Observation("i1", "preference.mode", "verbose", explicit=False, confidence=0.9),
            Observation("e1", "preference.mode", "concise", explicit=True, confidence=0.8),
        ]
    )
    claim = representation.explicit("preference.mode")
    assert claim is not None
    assert claim.value == "concise"
    assert claim.source == "explicit"


def test_conflicting_evidence_marks_attribute_unresolved() -> None:
    representation = RELModel().reconstruct(
        [
            Observation("e1", "goal.destination", "A"),
            Observation("e2", "goal.destination", "B", confidence=0.8),
        ]
    )
    assert "goal.destination" in representation.unresolved

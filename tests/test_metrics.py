from rel.metrics import brier_score, preservation_score, representation_fidelity


def test_representation_fidelity() -> None:
    assert representation_fidelity({"a": 1, "b": 2}, {"a": 1, "b": 3}) == 0.5


def test_preservation_score() -> None:
    assert preservation_score({"tone": "brief"}, {"tone": "brief"}) == 1.0


def test_brier_score() -> None:
    score = brier_score([0.9, 0.2], [1, 0])
    assert abs(score - 0.025) < 1e-12

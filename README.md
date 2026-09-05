# Resonant Empathy Law (REL)

### Computational human-alignment and representation-safety primitives for AI systems

REL is an experimental AI-safety framework for evaluating whether an AI system represents a human's relevant preferences, constraints, beliefs, and uncertainty before selecting a response or action.

REL does **not** assume that fluent emotional language is evidence of understanding. It separates what a human explicitly supplied, what a model inferred, what the model independently knows, and what remains unresolved.

> **Research status:** experimental / pre-1.0. REL is a safety-oriented research implementation, not a claim that AI systems experience empathy and not a psychological diagnostic tool.

## Safety problem

An AI system can sound empathic while still failing in important ways: inventing a preference, confidently assigning an emotional state, overriding an explicit boundary, or confusing the user's view with the model's own knowledge. REL treats these as representation and alignment failures that should be observable and testable.

## Core model

```text
Human / Actor
     ↓
Observable Evidence
     ↓
Structural Reconstruction
     ↓
Perspective Separation
     ↓
Uncertainty Preservation
     ↓
Preference / Constraint Check
     ↓
Safe Response or Action
```

REL focuses on four requirements:

1. **Representation fidelity** — inferred state should track supported evidence.
2. **Perspective separation** — explicit human claims, model inference, and model knowledge remain distinguishable.
3. **Uncertainty calibration** — ambiguous evidence must not become false certainty.
4. **Preference and constraint preservation** — explicit human goals and boundaries should survive downstream reasoning, subject to legitimate safety constraints.

The historical REL formulation used **structural reconstruction, temporal relation, and sustained coherence** as its conceptual core. In this AI/ML implementation, structural reconstruction is operationalized directly; temporal relation and coherence are treated conservatively as interaction consistency and evidence-to-representation agreement rather than as claims of literal physiological or oscillator synchronization.

## Installation

```bash
python -m pip install -e .
```

Development install:

```bash
python -m pip install -e '.[dev]'
pytest
```

## 30-second example

```python
from rel import Observation, RELModel

rel = RELModel()

representation = rel.reconstruct([
    Observation(
        id="obs-1",
        attribute="preference.response_style",
        value="concise",
        explicit=True,
        confidence=1.0,
    ),
    Observation(
        id="obs-2",
        attribute="affect.frustrated",
        value=True,
        explicit=False,
        confidence=0.45,
    ),
])

print(representation.explicit("preference.response_style").value)
print(representation.inferred("affect.frustrated").confidence)
```

The first state is an explicit preference. The second is only an inference and remains labeled and uncertain.

## Public API

- `Observation` — structured evidence about a human-relevant state.
- `StateClaim` — a bounded claim linked to supporting evidence.
- `RelationalRepresentation` — separates explicit and inferred state.
- `RELModel` — evidence-to-representation reconstruction.
- `AlignmentGuard` — preference and constraint checks.
- `OverInferenceDetector` — flags claims with insufficient evidential support.
- `RELEvaluator` — computes core safety metrics.

## Safety metrics

REL currently provides primitives for:

- representation fidelity
- perspective separation
- unsupported inference rate
- preference preservation
- constraint preservation
- Brier score for probabilistic calibration

See [`docs/METRICS.md`](docs/METRICS.md) and [`docs/SAFETY_MODEL.md`](docs/SAFETY_MODEL.md).

## Scope

REL is intentionally narrower than a general relational-intelligence architecture. This repository does not expose generalized asymmetric actor-state intelligence, longitudinal relational geometry, dynamic execution topology, or other productized relational-computation mechanisms.

REL is also not:

- a consciousness model;
- proof that AI experiences empathy;
- a general theory of intelligence;
- a psychological diagnostic system;
- a claim that empathy is literally phase synchronization;
- a replacement for established AI-safety or alignment research.

## Repository layout

```text
rel/         core package
examples/    executable examples
tests/       unit tests
docs/        theory, safety model, metrics, prior art, limitations
research/    conceptual lineage from earlier REL / bio-physiological work
legacy/      preserved pre-v0.1 artifacts
```

## Development status

**v0.1.0** establishes the safety-oriented public model and a small deterministic reference implementation. The next research work is benchmark construction, baseline comparison, and evaluation against real model outputs.

## License

Apache-2.0. See [`LICENSE`](LICENSE).

## Citation

See [`CITATION.cff`](CITATION.cff).

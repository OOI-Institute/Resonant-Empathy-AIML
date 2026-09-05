# REL Metrics

The v0.1 reference implementation provides small, inspectable metrics rather than a single opaque "empathy score."

## Representation Fidelity

Fraction of known task-relevant attributes represented correctly against supplied ground truth.

## Perspective Separation

Fraction of claims that retain their declared source/provenance. Future benchmark versions should test harder cases where human belief conflicts with model knowledge.

## Unsupported Inference Rate

Fraction of inferred human-state claims without linked evidence. The v0.1 data model prevents creation of such claims through normal constructors; the metric remains useful for imported/model-generated outputs.

## Preference / Constraint Preservation

Agreement between explicit human preferences or constraints and downstream action metadata.

## Calibration

REL uses standard probabilistic metrics when applicable. `brier_score` is included in v0.1. Future work should add ECE/NLL only where benchmark outputs support them correctly.

## No universal empathy scalar

REL intentionally does not collapse all dimensions into one number. Safety tradeoffs should remain inspectable.

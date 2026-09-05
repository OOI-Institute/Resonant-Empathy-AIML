# REL Overview

REL is a safety-oriented computational framework for keeping a model's representation of a human bounded by evidence.

The implementation emphasizes four properties: **fidelity, perspective separation, uncertainty, and preference/constraint preservation**.

## Design invariant

A model-side representation is an estimate, not the human's true state:

```text
representation(human | evidence, context) != human true state
```

Every human-state claim should therefore carry provenance, source type, and confidence.

## Isolation boundary

This repository is self-contained and limited to REL's public AI-safety primitives. It has no dependency on, or implementation of, separate proprietary cognition, orchestration, execution, or product architectures.

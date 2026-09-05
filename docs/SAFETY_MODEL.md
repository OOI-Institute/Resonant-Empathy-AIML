# REL Safety Model

REL treats failures of human representation as safety-relevant when they can distort downstream responses or actions.

## Failure classes

### Over-Inference
A model asserts a human-state claim more strongly than the evidence permits.

### Perspective Collapse
The model confuses the human's belief, the model's inference, and independent world knowledge.

### Preference Substitution
The model silently replaces an explicit human preference with its own optimization default.

### Constraint Loss
An explicit boundary disappears before action selection.

### False Certainty
Ambiguous evidence is converted into unjustified confidence.

### Human-State Hallucination
The model creates a human attribute without supporting evidence.

### Emotional Mimicry Without Representation Fidelity
Supportive language masks an inaccurate representation of the user.

### Unsafe Deference
Representing a human preference does not imply that every requested action should be executed. External safety rules still apply.

### Unsafe Override
Conversely, safety reasoning should not be used as a blanket justification to erase benign user preferences.

### Actor Confusion
State belonging to one person is attributed to another.

## Safety principle

REL separates **representing what a human wants or believes** from **deciding whether an action is safe or permissible**. Accurate representation is necessary for alignment, but it is not sufficient for action authorization.

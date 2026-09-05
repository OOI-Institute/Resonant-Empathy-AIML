from rel import Observation, RELModel


observations = [
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
]

representation = RELModel().reconstruct(observations)

for attribute, claim in representation.claims.items():
    print(attribute, claim.value, claim.source, f"confidence={claim.confidence:.2f}")

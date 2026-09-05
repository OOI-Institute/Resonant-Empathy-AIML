from rel import AlignmentGuard, Observation, RELModel


representation = RELModel().reconstruct(
    [
        Observation("p1", "preference.response_style", "concise"),
        Observation("c1", "constraint.share_data", False),
    ]
)

result = AlignmentGuard().check(
    representation,
    {"response_style": "long", "share_data": True},
)
print("allowed:", result.allowed)
print("violations:", result.violations)

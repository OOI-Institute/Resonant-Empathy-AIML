from rel import Observation, RELModel


rel = RELModel()
representation = rel.reconstruct(
    [Observation("human-1", "belief.route_safe", True, explicit=True, confidence=1.0)]
)
rel.add_model_knowledge(representation, "route_safe", False, confidence=0.99)

print("Human belief:", representation.explicit("belief.route_safe").value)
print("Model knowledge:", representation.model_knowledge("model::route_safe").value)

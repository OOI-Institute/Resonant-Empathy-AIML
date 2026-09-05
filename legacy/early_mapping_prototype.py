compute_mapping.py
def compute_structural_mapping(human_features, model):
    """
    Computes Structural Mapping (SM) using a multimodal contrastive encoder.
    """
    return model.encode(human_features)
compute_coherence.py
import numpy as np

def coherence_operator(mapped_human, ai_latents):
    """
    Computes the cross-substrate coherence operator:
    C(H, A) = <M(H), A>
    """
    return float(np.dot(mapped_human, ai_latents) / 
                 (np.linalg.norm(mapped_human) * np.linalg.norm(ai_latents)))
RSA_demo.ipynb
A runnable notebook showing how to measure representational similarity.

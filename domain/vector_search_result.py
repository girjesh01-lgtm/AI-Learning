from dataclasses import dataclass


@dataclass
class VectorSearchResult:
    
    vector_id : int
    
    similarity_score: float

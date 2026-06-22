import math

class CosineSimilarity:
    
    @staticmethod
    def calculate(vector1, vector2):

        """
        Calculate the cosine similarity between two vectors.
        """

        if vector1 != None and vector2 != None and len(vector1) != len(vector2):
            raise ValueError("Vectors must have same dimensions and some values.")
        
        dot_product = 0

        for a,b in zip(vector1, vector2):
            dot_product += a * b


        magnitude1 = math.sqrt(sum(x * x for x in vector1))
        magnitude2 = math.sqrt(sum(x * x for x in vector2))

        if magnitude1 == 0 or magnitude2 == 0:
            raise ValueError("Zero magnitude vector encountered.")
        
        return dot_product / (magnitude1 * magnitude2)
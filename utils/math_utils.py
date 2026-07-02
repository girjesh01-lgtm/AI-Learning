class MathUtils:

    @staticmethod
    def dot_product(a: list[float], b:list[float]) -> float:
        if len(a) != len(b):
            raise ValueError("Vectors must have the same dimensions.")
        
        result = 0.0

        for x,y in zip(a,b) :
            result += x * y
        
        return result
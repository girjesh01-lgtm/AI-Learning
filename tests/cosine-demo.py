from similarity.cosine_similarity import CosineSimilarity

vector1 = [1, 0]
vector2 = [-1, 0]

score = CosineSimilarity.calculate(vector1, vector2)

print(score)
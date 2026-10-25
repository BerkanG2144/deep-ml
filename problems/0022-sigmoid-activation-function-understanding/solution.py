import math

def sigmoid(z: float) -> float:
	denominator = 1 + math.exp(-z)
	result = 1 / denominator
	return result
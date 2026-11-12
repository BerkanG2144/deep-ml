import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
    
    for f in features:
        z = sum(wi * xi for wi,xi in zip(f, weights)) + bias 
        sigmoid = 1 / (1 + math.exp(-z))
        probabilities.append(sigmoid)
    
    error = 0
    for label, probability in zip(labels, probabilities):
        diff = (label - probability) ** 2 
        error+=diff
        
    n = len(labels)
    mse = (1 / n) * error
    
    probabilities = [round(p, 4) for p in probabilities]
    mse = round(mse, 4)

    return probabilities, mse
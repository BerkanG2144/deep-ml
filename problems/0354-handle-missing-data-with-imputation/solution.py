import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    result = data.copy()

    for col in range(result.shape[1]):
        column = result[:, col]

        valid_values = column[~np.isnan(column)]

        if len(valid_values) == 0:
            continue

        if strategy == 'mean':
            fill_value = np.mean(valid_values)

        elif strategy == 'median':
            fill_value = np.median(valid_values)

        elif strategy == 'mode':
            values, counts = np.unique(valid_values, return_counts=True)
            fill_value = values[np.argmax(counts)]

        else:
            raise ValueError("Unknown strategy")

        column[np.isnan(column)] = fill_value

    return result
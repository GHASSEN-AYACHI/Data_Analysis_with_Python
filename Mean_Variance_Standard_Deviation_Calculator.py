import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
       
    matrix = np.array(list).reshape((3, 3))

    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    axis1 = matrix.mean(axis=0).tolist()
    axis2 = matrix.mean(axis=1).tolist()
    flattened = matrix.mean()
    
    calculations['mean'] = [axis1, axis2, flattened]

    axis1 = matrix.var(axis=0).tolist()
    axis2 = matrix.var(axis=1).tolist()
    flattened = matrix.var()
    
    calculations['variance'] = [axis1, axis2, flattened]

    axis1 = matrix.std(axis=0).tolist()
    axis2 = matrix.std(axis=1).tolist()
    flattened = matrix.std()
    
    calculations['standard deviation'] = [axis1, axis2, flattened]

    axis1 = matrix.max(axis=0).tolist()
    axis2 = matrix.max(axis=1).tolist()
    flattened = matrix.max()
    
    calculations['max'] = [axis1, axis2, flattened]

    axis1 = matrix.min(axis=0).tolist()
    axis2 = matrix.min(axis=1).tolist()
    flattened = matrix.min()
    
    calculations['min'] = [axis1, axis2, flattened]

    axis1 = matrix.sum(axis=0).tolist()
    axis2 = matrix.sum(axis=1).tolist()
    flattened = matrix.sum()
    
    calculations['sum'] = [axis1, axis2, flattened]






    return calculate
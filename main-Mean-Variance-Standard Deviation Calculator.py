import numpy as np


def calculate(MyList):
    if len(MyList) != 9:
        raise ValueError("List must contain nine numbers.")
    # first convert the List into a 3 by 3 matrix
    MyMatrix = np.array(MyList).reshape(3, 3)

    # Create the means
    ColMean = [np.mean(MyMatrix[:, 0]), np.mean(MyMatrix[:, 1]), np.mean(MyMatrix[:, 2])]
    RowMean = [np.mean(MyMatrix[0, :]), np.mean(MyMatrix[1, :]), np.mean(MyMatrix[2, :])]
    FlatMean = np.mean(MyList)

    # Create the variance
    ColVar = [np.var(MyMatrix[:, 0]), np.var(MyMatrix[:, 1]), np.var(MyMatrix[:, 2]), ]
    RowVar = [np.var(MyMatrix[0, :]), np.var(MyMatrix[1, :]), np.var(MyMatrix[2, :]), ]
    FlatVar = np.var(MyList)

    # Create the standard deviation
    ColStd = [np.std(MyMatrix[:, 0]), np.std(MyMatrix[:, 1]), np.std(MyMatrix[:, 2]), ]
    RowStd = [np.std(MyMatrix[0, :]), np.std(MyMatrix[1, :]), np.std(MyMatrix[2, :]), ]
    FlatStd = np.std(MyList)

    # Craete the max
    ColMax = [np.max(MyMatrix[:, 0]), np.max(MyMatrix[:, 1]), np.max(MyMatrix[:, 2]), ]
    RowMax = [np.max(MyMatrix[0, :]), np.max(MyMatrix[1, :]), np.max(MyMatrix[2, :]), ]
    FlatMax = np.max(MyList)

    # Create the min
    ColMin = [np.min(MyMatrix[:, 0]), np.min(MyMatrix[:, 1]), np.min(MyMatrix[:, 2]), ]
    RowMin = [np.min(MyMatrix[0, :]), np.min(MyMatrix[1, :]), np.min(MyMatrix[2, :]), ]
    FlatMin = np.min(MyList)

    # Create the sum
    ColSum = [np.sum(MyMatrix[:, 0]), np.sum(MyMatrix[:, 1]), np.sum(MyMatrix[:, 2]), ]
    RowSum = [np.sum(MyMatrix[0, :]), np.sum(MyMatrix[1, :]), np.sum(MyMatrix[2, :]), ]
    FlatSum = np.sum(MyList)

    # create the dictionary
    calculations = {
        'mean': [ColMean, RowMean, FlatMean],
        'variance': [ColVar, RowVar, FlatVar],
        'standard deviation': [ColStd, RowStd, FlatStd],
        'max': [ColMax, RowMax, FlatMax],
        'min': [ColMin, RowMin, FlatMin],
        'sum': [ColSum, RowSum, FlatSum],
    }

    # print(f"This is my dictionary {calculations}")

    return calculations




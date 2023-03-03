import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd

def make_relationship_matrix(data: DataFrame):

    # 相关系数矩阵可视化
    correlations = data.corr()

    plt.imshow(correlations, cmap='coolwarm', vmin=-1, vmax=1)

    plt.colorbar()

    plt.xticks(range(len(correlations)), correlations.columns, rotation=90)

    plt.yticks(range(len(correlations)), correlations.columns)

    plt.show()
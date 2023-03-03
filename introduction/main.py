import pandas as pd

from data_statistics import data_statistics_visualization, make_visualization
from relationship_matrix import make_relationship_matrix

"""
    Introduction
    The data in this dataset is mostly binary, so mean, median, standard deviation, minimum, and maximum are meaningless. 
    We performed group statistics on the columns as shown below. 
    By understanding the dataset, there are several groups of variables that may be associated: 
        h1n1_concern and opinion_h1n1_risk: The level of concern of respondents about H1N1 influenza may be related to their perceived risk of contracting H1N1 influenza. 
        h1n1_knowledge and doctor_recc_h1n1: The level of knowledge about H1N1 influenza may be related to whether a physician recommends the H1N1 vaccine. 
        doctor_recc_h1n1 and doctor_recc_seasonal: Whether physicians recommend H1N1 vaccine may be related to whether they recommend seasonal influenza vaccine. 
        opinion_h1n1_vacc_effective and opinion_seas_vacc_effective: Respondents' views on the effectiveness of the H1N1 vaccine may be related to their views on the effectiveness of the seasonal flu vaccine. 
    The verification is carried out by generating the correlation coefficient matrix.
"""

if __name__ == '__main__':

    data = pd.read_csv('../csv/training_set_features.csv')

    # data_statistics_visualization(data)

    # 生成统计
    make_visualization(data)

    # 相关系数矩阵可视化
    make_relationship_matrix(data)







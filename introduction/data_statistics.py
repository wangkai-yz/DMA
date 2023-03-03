import math

import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd

def data_statistics_visualization(data: DataFrame):

    # 计算均值、中位数、众数、标准差、最小值和最大值
    # mean = data.mean()
    # median = data.median()
    # mode = data.mode()
    # std = data.std()
    # minimum = data.min()
    # maximum = data.max()

    # 输出统计描述结果
    # print('均值：\n', mean)
    # print('中位数：\n', median)
    # print('众数：\n', mode)
    # print('标准差：\n', std)
    # print('最小值：\n', minimum)
    # print('最大值：\n', maximum)

    # 均值、中位数、标准差、最小值和最大值对一些列毫无意义，所以利用饼状图进行百分比展示。
    stats = data.describe()

    # 创建一个柱状图
    fig, ax = plt.subplots()

    # 设置图形的标题和x轴标签
    ax.set_title('Descriptive Statistics')
    ax.set_xlabel('Statistic')

    # 设置y轴范围
    ax.set_ylim([0, 5])

    # 添加柱状图
    ax.bar(stats.columns, stats.loc['mean'], label='Mean')
    ax.bar(stats.columns, stats.loc['50%'], label='Median')
    ax.bar(stats.columns, stats.loc['std'], label='Standard Deviation')
    ax.bar(stats.columns, stats.loc['min'], label='Minimum')
    ax.bar(stats.columns, stats.loc['max'], label='Maximum')

    # 显示图例
    ax.legend()

    # 显示图形
    plt.show()

def make_visualization(data: DataFrame):

    # 均值、中位数、标准差、最小值和最大值对一些列毫无意义，所以利用饼状图进行百分比展示。
    cols = list(data.columns)

    demand_cols = [x for x in cols if x not in ['respondent_id', 'age_group', 'census_msa', 'employment_industry', 'employment_occupation']]

    for col in demand_cols:

        # col_value = list(data[col])
        #
        # value_class = list(filter(lambda x: not isinstance(x, float) or not math.isnan(x), list(set(col_value))))
        #
        # values = list(filter(lambda x: not isinstance(x, float) or not math.isnan(x), col_value))

        grouped = data.groupby(col).size()

        grouped.plot(kind='pie', autopct='%1.1f%%')

        plt.title(col)

        plt.savefig('../%s.png' % col)

        # plt.show()



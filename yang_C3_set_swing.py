import pandas as pd


import pandas as pd
from sklearn.preprocessing import MinMaxScaler  # 导入MinMaxScaler

import pandas as pd
from sklearn.preprocessing import MinMaxScaler  # 导入MinMaxScaler

def merge_columns_with_weights_and_save(file_path, column_names, weights, output_file):
    # 读取 CSV 文件
    data = pd.read_csv(file_path)

    # 确保输入的列名和权重数量一致
    if len(column_names) != len(weights):
        raise ValueError("列名和权重数量不一致")

    # 归一化指定的列到0到100
    scaler = MinMaxScaler(feature_range=(0, 100))  # 设置归一化范围为0到100
    scaled_data = scaler.fit_transform(data[column_names])  # 归一化这些列
    scaled_data_df = pd.DataFrame(scaled_data, columns=column_names)  # 将归一化后的数据转换为DataFrame

    # 根据权重合并指定的列
    swing_values = pd.Series(0, index=data.index)  # 初始化为0的序列，确保长度与data一致
    for i, column_name in enumerate(column_names):
        swing_values += scaled_data_df[column_name] * weights[i]

    # 将合并后的值添加为新列 'p1_swing'
    data['p1_swing'] = swing_values

    # 保存更新后的数据到新文件
    data.to_csv(output_file, index=False)
    print(f"数据已保存到 {output_file}")


# 使用示例：
file_path = 'american_1107_match_swing.csv'  # 替换成你的文件路径
column_names = ['p1_momentum', 'p1_streak', 'p1_physical_strength']  # 替换成你要提取的列名
weights = [0.5, 0.25, 0.25]  # 替换成相应的权重值
output_file = 'american_1107_match_swing.csv'  # 替换成保存结果的文件路径

merge_columns_with_weights_and_save(file_path, column_names, weights, output_file)

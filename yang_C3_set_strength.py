import pandas as pd
import numpy as np

def preprocess_data(file_path):
    # 读取 CSV 文件
    data = pd.read_csv(file_path)

    # 执行你的所有预处理步骤
    # 例如，计算时间差
    data['elapsed_time'] = pd.to_timedelta(data['elapsed_time'])
    data['time_diff'] = data['elapsed_time'].diff().fillna(pd.Timedelta(seconds=0)).dt.total_seconds()

    # 返回预处理后的数据
    return data

def merge_columns_with_weights_and_save(data, column_names, weights, output_file, strength_no):
    # 确保输入的列名和权重数量一致
    if len(column_names) != len(weights):
        raise ValueError("列名和权重数量不一致")

    # 初始化swing_values序列，确保长度与data一致
    swing_values = pd.Series(0, index=data.index)
    for i in range(len(column_names)):
        column_name = column_names[i]
        weight = weights[i]
        if column_name not in data.columns:
            raise ValueError(f"列名 '{column_name}' 不存在于数据中")
        # 对每个指定列进行加权
        if i == 0:
            swing_values += data[column_name] * weight + 100
        else:
            swing_values += data[column_name] * weight

    # 使用numpy.clip确保所有的值都在0到100之间
    swing_values_clipped = np.clip(swing_values, 0, 100)

    # 将处理后的值赋给新列
    data[strength_no] = swing_values_clipped

    # 保存更新后的数据到新文件（或覆盖原始文件）
    data.to_csv(output_file, index=False)
    print(f"数据已保存到 {output_file}")

# 定义文件路径
file_path =  'american_1107_match_swing.csv'
output_file =  'american_1107_match_swing.csv'  # 覆盖原始文件

# 预处理数据
preprocessed_data = preprocess_data(file_path)

# 定义列名和权重
column_names = ['time_diff', 'speed_mph', 'p1_distance_run', 'rally_count']
weights = [0.05, -0.2, -1, -0.5]
strength_no = 'p1_physical_strength'

# 合并列并保存结果
merge_columns_with_weights_and_save(preprocessed_data, column_names, weights, output_file, strength_no)

strength_no2 = 'p2_physical_strength'
column_names = ['time_diff', 'speed_mph', 'p2_distance_run', 'rally_count']

# 合并列并保存结果
merge_columns_with_weights_and_save(preprocessed_data, column_names, weights, output_file, strength_no2)

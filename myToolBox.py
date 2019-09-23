import numpy as np
import pandas as pd

def get_attributes_type(attribute_path):
    attributes_dict = {}
    
    with open(attribute_path,'r') as f:
        for line in f:
            a = line.split(' ')
            attribute = a[1][:-1] # Get list from a and remove ':'
            if 'continuous' in a:
                attributes_dict[attribute] = 'num' # numerical
            else:
                attributes_dict[attribute] = 'cat' # categorical 
    return attributes_dict

def count_distinct(mlist):
    
    # Get the counter
    from collections import Counter

    # Return the size of the counter = distinct numbers
    distinct = len(Counter(mlist))
    
    return distinct
    
def count_isolated(mlist):
    # Get the counter
    from collections import Counter
    count_dict = Counter(mlist)

    # list of isolated item
    list_iso = [k for k,v in count_dict.items() if v == 1]
    # Numbers of isolated item
    len_iso = len(list_iso)
    
    return len_iso

def create_stat_df(df, attributes_type):   
    ''' Lập 1 bảng thống kê (dataframe), mỗi dòng là :
    - Thuộc tính
    - Kiểu dữ liệu
    - Trung bình/Số phần tử phân biệt
    - Phương sai/Số phần tử duy nhất
    - Số giá trị null '?'
    '''
    df_col = ['thuộc tính', 'kiểu dữ liệu','tb/số pbiet',
              'phg sai/số duy 1','số null']
    df_data = []

    for attribute in df.columns:
        line = [attribute]
        # Remove null values
        col_values = [num for num in df[attribute].to_list() if num != '?']

        if attributes_type[attribute] == 'num':
            # Add attribute type
            line.append('numerical')

            # Convert to int type (if string)
            if isinstance(col_values[0],str): 
                col_values = [float(num) for num in col_values]
            # Calculate mean and standard deviation
            mean = np.mean(col_values)
            std = np.std(col_values)

            # Add mean & std
            line += [mean,std]
        elif attributes_type[attribute] == 'cat':
            line.append('nominal')
            # flu
            c_distinct = count_distinct(col_values)
            c_isolated = count_isolated(col_values)
            line += [c_distinct, c_isolated]

        # Add null qty 
        null_qty = sum([1 for i in df[attribute].to_list() if i=='?'])
        line.append(null_qty)

        # Append that line to df_data
        df_data.append(line)
    stat_df = pd.DataFrame(df_data,columns = df_col)
    return stat_df

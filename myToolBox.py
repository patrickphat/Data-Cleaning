import numpy as np
import pandas as pd

def get_attributes_type(attribute_path):
    attributes_dict = {}
    numeric_term = None
    with open(attribute_path,'r') as f:
        for i,line in enumerate(f):
            if i == 0:
                numeric_term = line.replace('\n','').split(' ')[0]
                continue
            line = line.strip() # Remove leading spaces 
            a = line.split(' ') # Tokenize that line by spacing
            prefix = a[0] # Get the first prefix of that line
            attribute = line.replace(a[0],'') # Remove the prefix from the line
            attribute = attribute[:attribute.find(':')].strip() # Get all the way to ":"
           
            # Calculate num words in attribute names
            len_attribute = len(attribute.split(' '))
            
            if  len_attribute > 1: # If there are spaces between attribute names
                attribute = '-'.join(attribute.split(' ')) # Use "-" to join
            if numeric_term in line:
                attributes_dict[attribute] = 'num' # numerical
            else:
                attributes_dict[attribute] = 'cat' # categorical 

    return attributes_dict
def numericize_list(mList):
            result = []
            for item in mList:
                if isfloat(item):
                    result.append(float(item))
                    continue
                    
                if str(item).isdigit():
                    result.append(item)
            result = np.array(result)
            result = result[~np.isnan(result)].tolist() # remove nan
            return result
def isfloat(value):
    if value == np.nan:
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False 

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

def create_stat_df(dataset_folder):   
    ''' Create a stat table(dataframe), for each line contains :
    - Attribute
    - Data type
    - Mean/Distinct values
    - Std/Isolated values
    - Num of Null
	
     INPUT:
	- a dataframe
	- a dictionary of dataframe's attribute mapping to either 'num' (numerical) or 'cat' (categorical)

    OUTPUT:
	- A statistical dataframe
    '''
    ## Helper Functions
    # Check if a string can be converted to float
    def isfloat(value):
        if value == np.nan:
            return False
        try:
            float(value)
            return True
        except ValueError:
            return False

    # Convert a list of (strings, float, int, nan,..) to list of numbers
    def numericize_list(mList):
            result = []
            for item in mList:
                if isfloat(item):
                    result.append(float(item))
                    continue
                    
                if str(item).isdigit():
                    result.append(item)
            result = np.array(result)
            result = result[~np.isnan(result)].tolist() # remove nan
            return result
    
    # Load data 
    dataset_path = dataset_folder + 'load.data'
    attributes_path = dataset_folder + 'attributes.txt'
    attributes_type = get_attributes_type(attributes_path)

    df = pd.read_csv(dataset_path,header=None, names=list(attributes_type.keys()))
    len_df = len(df)
    df_col = ['Attribute', 'Data type','Mean/Distinct values',
              ' Std/Isolated values','Num of Nulls']
    df_data = []
    
    for attribute in df.columns:
        line = [attribute]
        # Remove null values
        col_values = [num for num in df[attribute].to_list() if num != '?']

        if attributes_type[attribute] == 'num':
            # Add attribute type
            line.append('numerical')
            # Convert the list to numerical type
            col_values = numericize_list(col_values)
            # Calculate mean and standard deviation
            mean = '%.2f' % np.mean(col_values)
            std = '%.2f' % np.std(col_values)

            # Add mean & std
            line += [mean,std]
        elif attributes_type[attribute] == 'cat':
            line.append('nominal')
            # calculate distinct & isolated values
            c_distinct = count_distinct(col_values)
            c_isolated = count_isolated(col_values)
            line += [c_distinct, c_isolated]

        # Add null qty 
        null_qty = sum([1 for i in df[attribute].to_list() if i=='?'])
        null_qty = str(null_qty) + " (" + str('%.2f' % (null_qty/len(df)*100)) + "%)"
        line.append(null_qty)

        # Append that line to df_data
        df_data.append(line)
    stat_df = pd.DataFrame(df_data,columns = df_col)
    return stat_df, len_df
def fill_missing_df(dataset_folder):
     
    # Load data 
    dataset_path = dataset_folder + 'load.data'
    attributes_path = dataset_folder + 'attributes.txt'
    attributes_type = get_attributes_type(attributes_path)
    df = pd.read_csv(dataset_path,header=None, names=list(attributes_type.keys()))
    
    filling_log = []
    # Get the mode (most appeared words in the list)
    def most_common(lst):
        return max(set(lst), key=lst.count)
        
    for item in df.keys():
        attribute_type = attributes_type[item]
        
        Series = df[item].tolist()

        if attribute_type == "num":
            Series = numericize_list(Series)
            mean_Series = "%.2f" % np.mean(Series)
            df[item] = df[item].replace("?",mean_Series)
            filling_log.append(mean_Series)
            
        if attribute_type == "cat":

            mode_Series = most_common(Series)
            df[item] = df[item].replace("?",mode_Series)
            filling_log.append(mode_Series)
    return df,filling_log


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

class Normalizer:
    def __init__(self,mode,new_min=0,new_max=1):
        self.mode = mode
        self.new_min = new_min
        self.new_max = new_max 
        self.min_max_dict = {} # Dictionary mapping from attributes name to a tuple of (min,max)
        self.z_score_dict = {} # Dictionary mapping from attributes name to a tuple of (mean,std)
        self.transform_log = {} # Dictionary mapping from attributes name to a tuple of (min_log,max_log)
        
    def transform_minmax_Series(self,Series,min_max):
        # Retrieve min max from tuple
        min,max = min_max
        
        # Convert to float in case of strings
        Series = Series.astype(float)
        
        # Transform the Series to min max values 
        Series = (Series - min)/(max-min)*(self.new_max-self.new_min)+self.new_min
        
        return Series.round(4) # round to precision of 2 
    
    def transform_zscore_Series(self,Series,mean_std):
        # Retrieve mean, std from tuple
        mean,std = mean_std
        
        # Convert to float in case of strings
        Series = Series.astype(float)
        
        # Transform the Series to min max values 
        Series = ((Series - mean)/std).round(4)
        
        # Series_transform_log monitors the range of normalization within an attribute
        Series_transform_log = (np.min(Series),np.max(Series))
        return Series,Series_transform_log
        
        
    
    def fit_transform(self,dataset_folder):
        
        # Load data 
        df,_ = fill_missing_df(dataset_folder) # Fill missing value
        attributes_path = dataset_folder + 'attributes.txt'
        attributes_type = get_attributes_type(attributes_path)
        
        # Min-max 
        if self.mode == 'minmax':
            # Fitting min max of each attribute to the Normalize
            for item in df.keys():
                if attributes_type[item] == 'cat':
                    continue

                if attributes_type[item] == 'num':
                    attri_min = float(np.min(df[item].astype('float')))
                    attri_max = float(np.max(df[item].astype('float')))
                    self.min_max_dict[item] = (attri_min,attri_max)

            # Transform the dataframe
            for item in df.keys():
                if attributes_type[item] == 'cat':
                    continue

                if attributes_type[item] == 'num':
                    # Replace Series values with new normalized values with the scaler
                    df[item] = self.transform_minmax_Series(df[item], self.min_max_dict[item])
                    self.transform_log[item] = (self.new_min,self.new_max)
            
            return df,self.transform_log
        
        # Z-Score
        elif self.mode == 'zscore':
            # Fitting min max of each attribute to the Normalize
            for item in df.keys():
                if attributes_type[item] == 'cat':
                    continue

                if attributes_type[item] == 'num':
                    attri_items = df[item].astype(float)
                    attri_mean =  np.mean(attri_items)
                
                    attri_std =  np.std(attri_items)
                    self.z_score_dict[item] = (attri_mean,attri_std)
                    
            # Transform the dataframe
            for item in df.keys():
                if attributes_type[item] == 'cat':
                    continue

                if attributes_type[item] == 'num':
                    # Replace Series values with new normalized values with the scaler
                    df[item],transform_log = self.transform_zscore_Series(df[item], self.z_score_dict[item])
                    self.transform_log[item] = transform_log
            
            return df,self.transform_log
                     
class Discretizer:
    def __init__(self,mode,depth=4,width=4):
        self.mode = mode
        self.depth = depth
        self.width = width
        self.attri_to_bins = {} # A dict map from attri to bin
        self.discretize_log = {} # A dict map from attri to list of tuples (bin,frequency)        
    def fit_transform(self,dataset_folder):
        # Load data 
        df,_ = fill_missing_df(dataset_folder)
        attributes_path = dataset_folder + 'attributes.txt'
        attributes_type = get_attributes_type(attributes_path)
 
        # Fit to data to create bins
        if self.mode == 'width':
            for item in df.keys():
                if attributes_type[item] == 'num':
                   
                    Series = df[item]
                    bins = self.width_discretize(Series,width = self.width)
                    self.attri_to_bins[item] = bins
                else: continue
        elif self.mode == 'depth':
            for item in df.keys():
                if attributes_type[item] == 'num':
                    Series = df[item]
                    bins = self.depth_discretize(Series,depth = self.depth)
                    self.attri_to_bins[item] = bins
                else: continue
        
        # Transform dataframe to discretized bins
        for item in df.keys():
            if attributes_type[item] == 'num':
                    Series = df[item]
                    attri_bins = self.attri_to_bins[item]
                    df[item] = Series.astype(float).map(lambda x: self.val_to_bin(x,attri_bins))
            else: continue
    
        # Log for discretization
        for item in df.keys():
            if attributes_type[item] == 'num':
                bins_frequency = []
                # get iterator items (bins,frequency) of count object
                for count_tuple in df[item].value_counts().items(): 
                    bins_frequency.append(count_tuple)
                    
                self.discretize_log[item] = bins_frequency
            else: continue
        
        return df, self.discretize_log

            
    def width_discretize(self,Series,width):
        '''
        Input: a Series and width of discretization (proportional 0->1.0)
        Output: list of bins
        '''
        sorted_list = sorted(Series.astype(float).tolist())
        left_bound = np.min(sorted_list)
        right_bound = np.max(sorted_list)
        step = (right_bound - left_bound)*width
        bins = []

        pivot = left_bound
    
        while pivot < right_bound:
            
            if pivot + width > right_bound:
                # Round to work with numerical error
                bins.append((np.round(pivot,4),right_bound)) #
                break

            # Round to work with numerical error
            bins.append((np.round(pivot,4),np.round(pivot+step,4))) 
            pivot += np.round(step,4)
        return bins

    def depth_discretize(self,Series,depth):
        '''
        Input: a Series and width of discretization
        Output: list of bins
        '''
        sorted_list = sorted(Series.astype(float).tolist())

        left_bound = 0
        right_bound = len(sorted_list)-1

        bins = []

        pivot = 0
        while pivot < right_bound:
            left_bin = sorted_list[pivot]

            if pivot + depth >= right_bound:
                right_bin = sorted_list[right_bound]
                bins.append((left_bin,right_bin))
                break

            # Round to work with numerical error
            right_bin = sorted_list[pivot+int(depth)-1]
            bins.append((left_bin,right_bin)) 
            pivot += int(depth) - 1 
        return bins
    
    def val_in_bin(self,value,bin,mode):
        '''
        Input: value & bin (tuple of left bound and right bound)
        Output: True or False if value in that bin
        '''

        left_bound, right_bound = bin
        value
        if mode == 'leftest': 
            return (value <= right_bound and value >= left_bound)
        if mode == 'mid':
            return (value <= right_bound and value > left_bound)
        if mode == 'rightest':
            return (value <= right_bound and value > left_bound)

    def val_to_bin(self,value,bins):
        '''
        Input: value & sorted list of bins (bins are tuple of left bound and right bound)
        Output: bin that value falls in (the leftest bin)
        '''
        
        for i,bin in enumerate(bins):
            if i == 0:

                if self.val_in_bin(value,bin,mode="leftest"):
                    return bin
                else: continue
            elif i == len(bins)-1:

                if self.val_in_bin(value,bin,mode="rightest"):
                    return bin
                else: continue
            elif self.val_in_bin(value,bin,mode="mid"):
                return bin
            else: continue

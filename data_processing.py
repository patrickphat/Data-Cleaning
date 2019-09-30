import argparse
from myToolBox import *
import numpy as np

def summary_option(dataset_folder,log_path):
    stats,len_df = create_stat_df(dataset_folder)
    with open(log_path,'w') as f:
        f.write('# So mau: {}\n\n'.format(len_df))
        f.write('# So thuoc tinh: {}\n\n'.format(len(stats)))
        for i in range(len(stats)):
            line_data = stats.iloc[i] # data of i-th row
            attri_name = line_data['Attribute']
            attri_type = line_data['Data type']
            f.write('# thuoc tinh {}: "{}" {}\n'.format(i+1,attri_name,attri_type))
    print('Option executed: "summary"')
    print('- summary log file: '+ log_path)
    return log_path

def replace_option(dataset_folder,output_path,log_path):
    stats,len_df = create_stat_df(dataset_folder)
    df,filling_log = fill_missing_df(dataset_folder)
    with open(log_path,'w') as f:
        # For i in numbers of attribute
        for i in range(len(stats)):
            line_data = stats.iloc[i] # data of i-th row
            attri_name = line_data["Attribute"]
            attri_replace = filling_log[i]
            attri_null = line_data['Num of Nulls'].split(' ')[0]
            f.write('# thuoc tinh {}: "{}", {}, {}\n'.format(i+1,attri_name,attri_null,attri_replace))
    df.to_csv(output_path)
    print('Option executed: "summary"')
    print('- output file: ' + output_path)
    print('- summary log file: '+ log_path)
    return output_path,log_path
    
def normalize_option(dataset_folder,output_path,log_path):
    #stats,len_df = create_stat_df(dataset_folder)
    
    # Choose normalization mode
    print('Enter normalization mode: "minmax" or "zscore"?')
    normalizer_mode = input()
    
    # df and normalization log placeholder
    df = None
    norm_log = None

    # If option == minmax
    if normalizer_mode == "minmax":
        # User input for min max
        print("Enter new min:")
        new_min = float(input())
        new_max = float(input())
        
        # Declare normalizer
        Norm = Normalizer(mode = "minmax",new_min=new_min,new_max=new_max)
        df,norm_log = Norm.fit_transform(dataset_folder)
        
    # If options == zscore
    elif normalizer_mode == "zscore":
        # Declare normalizer
        Norm = Normalizer(mode = "zscore")
        df,norm_log = Norm.fit_transform(dataset_folder)
    
    with open(log_path,'w') as f:
        # For i in numbers of attribute
        for i,item in enumerate(norm_log.items()):
            attri_name = item[0]
            attri_range = item[1]
            f.write('# thuoc tinh {}: "{}", ({},{})\n'.format(i+1,attri_name,attri_range[0],attri_range[1]))
    df.to_csv(output_path)
    print('Option executed: "normalization"')
    print('- output file: ' + output_path)
    print('- summary log file: '+ log_path)
    return output_path,log_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--option",help='your option of processing the file')
    parser.add_argument("--input",help='path to input file')
    parser.add_argument("--output",help='path to output file')
    parser.add_argument("--log",help='path to log file')
    options = ['summary','replace','normalize']

    args = parser.parse_args()
    dataset_folder = args.input
    # If pass in invalid options then reject
    if args.option not in options:
        print('The option you passed in is invalid. Available options are {}. Press enter to stop then try again..'.format(options))
        input()
        exit()
    if args.input == None:
        print('You should insert your input file. Try again..')
        input()
        exit()

    if args.option == 'summary':
        if args.log == None:
            log_path = args.input + 'summary_log.txt'
            summary_option(dataset_folder,log_path)
        else:
            summary_option(dataset_folder,args.log)

    if args.option == 'replace':

        output_path = None
        log_path = None

        # If user doesn't declare output 
        if args.output == None:
            output_path = dataset_folder + 'replace_output.csv'
        
        # If user doesn't declare log 
        if args.log == None:
            log_path = dataset_folder + 'replace_log.txt'

        _,_ = replace_option(dataset_folder,output_path,log_path)

    if args.option == 'normalize':

        output_path = None
        log_path = None

        # If user doesn't declare output 
        if args.output == None:
            output_path = dataset_folder + 'normalize_output.csv'
        
        # If user doesn't declare log 
        if args.log == None:
            log_path = dataset_folder + 'normalize_log.txt'

        _,_ = normalize_option(dataset_folder,output_path,log_path)
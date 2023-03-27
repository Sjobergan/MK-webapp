# df_1 = pd.read_csv('automobile_1.csv', sep=';')
# df_2 = pd.read_csv('automobile_2.csv', sep=';')
# df_1 = pd.read_csv('data_files/automobile_1.csv', sep=';')
# df_2 = pd.read_csv('data_files/automobile_2.csv', sep=';')
import pandas as pd
import scipy as sc
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mp
from matplotlib import pyplot as plt
import pylab
import scipy.stats as stats
from DjangoWebProject1 import get_df as gd
from django.http import HttpRequest







#def splitSearchString(stringToSplit):
#    x = stringToSplit.split(' ')
#    return x
#def get_filenames(wanted_file):
#    if wanted_file == 'file_1':
#        file_1 = input('Please enter name of csv 1: ')
#        return file_1
#    if wanted_file == 'file_2':
#        file_2 = input('Please enter name of csv 2: ')
#        return file_2
#    if wanted_file == 'sepa':
#        sepa = input('What kind of separator is it in the file?: ')
#        return sepa
    
# # Remember to fix so that user can use their joine df through all of the program   
#file_1 = input('Please enter name of csv 1: ')
#file_2 = input('Please enter name of csv 2: ')
#sepa = input('What kind of separator is it in the file?: ')
#file_location = 'data_files/'
## file_1 = 'automobile.csv'
## file_2 = 'customer_job.csv'
## file_2 = ''
## sepa = ','
## df_1 = []
## df_2 = []
## df = []
#sample_df = []

#def get_dataframes_if_forgotten(wanted_df):
#    if wanted_df == 'df-1':
#        file_1 = input('Please enter name of csv 1: ')
#    elif wanted_df == 'df-2':
#        file_2 = input('Please enter name of csv 2: ')
#    sepa = input('What kind of separator is it in the file?: ')
#    if wanted_df == 'df-1':
#        df_1 = pd.read_csv(file_location + file_1, sep=sepa)
#        return df_1
#    # elif file_1 == '':
#    #     df_1 = df_1
#    #     return df_1
#    elif wanted_df == 'df-2':
#        df_2 = pd.read_csv(file_location + file_2, sep=sepa)
#        return df_2
#    elif file_2 == '':
#        df_2 = []
#        return df_2

#def get_dataframe(wanted_df):
#    # file_1 = get_filenames('file_1')
#    # file_2 = get_filenames('file_2')
#    # sepa = get_filenames('sepa')
#    if file_1 != '' and wanted_df == 'df-1':
#        df_1 = pd.read_csv(file_location + file_1, sep=sepa)
#        return df_1
#    elif file_1 == '':
#        df_1 = df_1
#        return df_1
#    if file_2 != '' and wanted_df == 'df-2':
#        df_2 = pd.read_csv(file_location + file_2, sep=sepa)
#        return df_2
#    elif file_2 == '':
#        df_2 = []
#        return df_2

#def get_dataframe_without_choice():
#    file_1 = get_filenames()[0]
#    file_2 = get_filenames()[1]
#    sepa = get_filenames()[2]
#    if file_1 != '':
#        df_1 = pd.read_csv(file_location + file_1, sep=sepa)
#        return df_1
#    elif file_1 == '':
#        df_1 = df_1
#        return df_1
#    if file_2 != '':
#        df_2 = pd.read_csv(file_location + file_2, sep=sepa)
#        return df_2
#    elif file_2 == '':
#        df_2 = []
#        return df_2    

# def get_sample_df():
#         choice = input('For full dataframe enter full else enter sample: ').lower()
#         if choice == 'sample':
#             size_of_sample = input('Enter number of sample size: ').lower()
#         if choice == 'full':
#             return df_1
#         elif choice == 'sample':
#             sample_df = df_1(n=int(size_of_sample), random_state=1).dropna()       
        
        
        

# if len(df_1):
#     df_1.sort_index('index', inplace=True)
# if len(df_2):
#     df_2.sort_index('index', inplace=True)

# def unconcatinated_df(df1, df2):
#     if len(df_1):
#         return df_1
#     elif not len(df_1):
#         return df_1
#     if len(df_2):
#         return df_2
#     elif not len(df_2):
#         return df_2
#     else:
#         print('You have to input atleast one csv file for this program to work.')


# if not df_1.empty:
#     df_1.sort_index('index', inplace=True)
# if not df_2.empty:
#     df_2.sort_index('index', inplace=True)
# # if not df_1.empty and df_2.empty:
# #     df = pd.concat([df_1, df_2]).dropna()
# else:
#     df = df_1


# df_2 = pd.read_csv('')    

# df_1 = pd.read_csv('automobile_1.csv', sep=';')
# df_2 = pd.read_csv('automobile_2.csv', sep=';')
# df_1 = pd.read_csv('data_files/automobile_1.csv', sep=';')
# df_2 = pd.read_csv('data_files/automobile_2.csv', sep=';')
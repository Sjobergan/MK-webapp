# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 09:05:51 2022

@author: janne
"""
from DjangoWebProject1 import imports_and_df as iad
from DjangoWebProject1 import functions_input as func
# df_1, df_2 = iad.unconcatinated_df()
df_1 = iad.get_dataframe('df-1')
df_2 = iad.get_dataframe('df-2')

def print_choices():
    if len(df_1):
        if not df_1.empty:
            print(df_1.info())
    if len(df_2):
        if not df_2.empty:
            print(df_2.info())
    numbers = {'Inner join: ': 'inner', 'Left outer join: ': 'left', 'Concatinate: ': 'concat'}
    for k, v in numbers.items():
        print(k, v)
# def get_new_dataframes():
#     if wanted_df == '1':
#         df_1 = iad.get_dataframes_if_forgotten('df-1')
#         return df_1
#     elif wanted_df == '2':
#         df_2 = iad.get_dataframes_if_forgotten('df-2')
#         return df_2
#     else:
#         print('')

#Here the user can join 2 dataframes by choosing what join they want
def make_different_joins():
    column_choice = ''
    if len(df_1) and len(df_2):
        print_choices()   
        join_choice = input('Enter wich type of join you want to do: ')
        if join_choice != 'concat':
            column_choice = input('Enter wich column you want to join on: ')
        question = input('Do you want the entire list or just head? Type head for only the head of list and all for entire dataframe: ').lower()
        question = question.lower()
        if join_choice != 'concat' or join_choice != '' and column_choice != '':
            func.df_joined = iad.pd.merge(df_1, df_2, on=column_choice, how=join_choice)       
            if question == 'head':
                print(func.df_joined.head())
            elif question == 'all':
                print(func.df_joined)
        elif join_choice != 'concat' and join_choice == '':
            print('You forgot to choose wich join you want')
            make_different_joins()
        elif join_choice != 'concat' and column_choice == '':
            print('You forgot to choose wich column to join on')
            make_different_joins()
        elif join_choice == 'concat' and column_choice == '':
            df_concat = iad.pd.concat([df_1, df_2])
            if question == 'head':
                print(df_concat.head())
            elif question == 'all':
                print(df_concat)
    elif not len(df_1) or not len(df_2):
        restart = input('Sorry you need 2 dataframes to make a join. Please try again by typing retry: ').lower()
        if restart == 'retry':
            if not len(df_1):
                df_1 = iad.get_dataframes_if_forgotten('df-1')
            elif not len(df_2):
                df_2 = iad.get_dataframes_if_forgotten('df-2')
            make_different_joins()
        else:
            print('Thank you for testing my dataframe search program')
    else:
        restart = input('Sorry, something went wrong. Please try again by typing start: ')
        restart = restart.lower()
        if restart == 'start':
            import Dataframe_search as ds
            ds.startFunction()
        else:
            print('Thank you for testing my dataframe search program')
        
# def concatinated_df():
#     print_choices()
#     if len(iad.df_1) and len(iad.df_2):
#         df = iad.pd.concat([iad.df_1, iad.df_2])
#         return df
#     else:
#         return 'You need two csv files to be able to concatinate'
        
#Here I want to call all inputs to clean up other functions
# def inputs():
    
#Here functions for different kind of drop nans will be developed    
# def drop_nan(dataframe, nan_to_drop):
    
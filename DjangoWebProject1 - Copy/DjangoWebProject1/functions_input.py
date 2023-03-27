# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 00:53:20 2022

@author: janne
"""
from DjangoWebProject1 import imports_and_df as iad
# Remember to fix so that user can use their joine df through all of the program
df_1 = iad.get_dataframe('df-1')
df_2 = iad.get_dataframe('df-2')
df = []
def splitSearchString(stringToSplit):
    x = stringToSplit.split(' ')
    return x       
def get_numbers_on_what_info():
    numbers = {'Info,': '1', 'Describe,': '2'}
    for k, v in numbers.items():
        print(k, v)
def df_choice():
    filename_1 = iad.file_1
    filename_2 = iad.file_2
    if filename_1 != '':
        numbers = {filename_1: '1'}
    elif filename_2 != '':
        numbers = {filename_2: '2'}
    elif filename_1 != '' and filename_2 != '':
        numbers = {filename_1: '1', filename_2: '2'}
    for k, v in numbers.items():
        print(k, v)
    dataframe = input('Wich dataframe do you want to use?: ')
    return dataframe
        
#Here I let the user show info, describe and others for the dataframe(s)
def get_iteresting_info():
    choice_of_df = df_choice()
    if choice_of_df == '1':
        df = df_1
    elif choice_of_df == '2':
        df = df_2
    else:
        print('You have to choose a dataframe to get info from.')
        get_iteresting_info()
        
    get_numbers_on_what_info()
    choice = input('Enter number to choose what information you want to see: ')
    info = 0
    desc = 0
    if choice == '1':
        info = df.info()
        print(info)
    elif choice == '2':
        desc = df.describe()
        print(desc)
    else:
        print('That number, search is not developted yet')
        get_iteresting_info()

def compare_lists(searchList, df):
    for i in searchList:
        for d in df:
            if i == d:
                return True
    return False

#Here the user can do different searches in their dataframe
def printAndConsumeSearch():
    choice_of_df = df_choice()
    if choice_of_df == '1':
        df = df_1
    elif choice_of_df == '2':
        df = df_2
    else:
        print('You have to choose a dataframe to search in.')
        printAndConsumeSearch()
        
    print(df.info())
    searchFrase = input('Please enter your search, if you use more than one word please put space between words: ')
    question = input('Do you want the entire list or just head? Type head for only the head of list: ')
    searchList = splitSearchString(searchFrase)
    if len(searchList) and compare_lists(searchList, df) == True:
        my_list = df[searchList]
        q = question.lower()
        if q == 'head':
            print(my_list.head())
        elif question == '':
            print(my_list)
    else:
        print('There is no column in dataframe that is named', searchList)
        printAndConsumeSearch()

#Here the user can get some Important numbers from the dataframe like min median and so on
def get_interesting_numbers():
    numbers = {'Median,': '1', 'Min,': '2'}
    for k, v in numbers.items():
        print(k, v)
        
    choice = input('Enter number to choose what numbers you want to see: ')
    median = 0
    mini = 0
    if choice == '1':
        median = df[['price']].median()
        print(median)
    elif choice == '2':
        mini = df[['price']].min()
        print(mini)
    else:
        print('That nukmber, search is not developted yet')
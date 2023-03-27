import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def splitSearchString(string_to_split, splitter):
    #Here i split the filepath to seperate it to a list
    x = string_to_split.split(splitter)
    return x

def get_filepath():
    #This function gets the filepath and filename
    # Assuming the current file is in the "app" folder
    # and the parent folder "static" is in the project root
    #project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    ## Path to the file
    #file_path = os.path.join(project_root, 'app', 'static', 'app', 'data_files', 'NetConsult AB - Mario kart 2023.csv')
    file_path = 'app/static/app/data_files/NetConsult AB - Mario kart 2023.csv'
    filepath_list = splitSearchString(file_path, '/')
    return file_path

def get_filename():
    #Here i take the last value from the list, wich is the filename
    filepath_list = get_filepath()
    filename = filepath_list[-1]
    return filename

def question(value):
    return value

#def get_filepath():
#    #This function opens filedialog and getting the filepath
#    root = tk.Tk()
#    root.withdraw()
#    file_path = filedialog.askopenfilename(initialdir='C:/users/')
#    filepath_list = splitSearchString(file_path, '/')
#    return file_path

#def get_filename():
#    #Here i take the last value from the list, wich is the filename
#    filepath_list = get_filepath()
#    filename = filepath_list[-1]
#    return filename

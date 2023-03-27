# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:27:15 2022

@author: janne
"""
from DjangoWebProject1 import imports_and_df as iad
# Remember to fix so that user can use their joine df through all of the program
df = []
df_1 = iad.get_dataframe('df-1')
df_2 = iad.get_dataframe('df-2')
salery = ''
df_choice = ''

def get_numbers_on_what():
    numbers = {'Basic diagrams:': '1', 'Barchart single column:': '2', 'Barchart double columns': '3', 'Piechart': '4'}
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

def get_diagrams_on_dataframe():
    if len(df_1) or len(df_2):
        if len(df_1):
            print(df_1.info())
        if len(df_2):
            print(df_2.info())
        df_choice = input('Please enter wich dataframe you like to use: ')
        get_numbers_on_what()
        chart_choice = input('Please enter the type of chart you want: ')
    else:
        print('You have to shoose a dataframe and column.')
    if df_choice == '1' and not df_1.empty and chart_choice == '1':
        column_name = input('Please enter the column name you want diagrams for: ') 
        get_qqplot(df_1, column_name)
        get_distribution_plot(df_1, column_name)
    elif df_choice == '2' and not df_2.empty and chart_choice == '1':
        column_name = input('Please enter the column name you want diagrams for: ') 
        get_qqplot(df_2, column_name)
        get_distribution_plot(df_2, column_name)
    elif df_choice == '1' and not df_1.empty and chart_choice == '2':
        column_x = input('Enter the column you want as your x-axis: ')
        column_y = input('Enter the column you want as your y-axis: ')
        get_bar_chart_single(df_1, column_x, column_y)
    elif df_choice == '2' and not df_2.empty and chart_choice == '2':
        column_x = input('Enter the column you want as your x-axis: ')
        column_y = input('Enter the column you want as your y-axis: ')
        get_bar_chart_single(df_2, column_x, column_y)
    elif df_choice == '1' and not df_1.empty and chart_choice == '3':
        column_x = input('Enter the column you want as your x-axis: ')
        column_y_1 = input('Enter the column you want as your left y-axis: ')
        column_y_2 = input('Enter the column you want as your right y-axis: ')
        get_bar_chart_double(df_1, column_x, column_y_1, column_y_2)
    elif df_choice == '2' and not df_2.empty and chart_choice == '3':
        column_x = input('Enter the column you want as your x-axis: ')
        column_y_1 = input('Enter the column you want as your left y-axis: ')
        column_y_2 = input('Enter the column you want as your right y-axis: ')
        get_bar_chart_double(df_2, column_x, column_y_1, column_y_2)
    elif df_choice == '1' and not df_1.empty and chart_choice == '4':
        items = input('Enter the column with the items: ')
        values = input('Enter the column with values: ')
        get_pie_chart(df_1, items, values)
    elif df_choice == '2' and not df_2.empty and chart_choice == '4':
        items = input('Enter the column with the items: ')
        values = input('Enter the column with values: ')
        get_pie_chart(df_2, items, values)
    else:
        choice = input('Something went wrong. Please try again. Type retry to go again or stop if you want to close the program: ').lower()
        if choice == 'restart':
            get_diagrams_on_dataframe()
        elif choice == 'stop':
            print('Thank you for testing my searchprogram.')
        else:
            print('Something went wrong. Please try again.')
        
def get_qqplot(df_filtered, column_name):
    iad.stats.probplot(df_filtered[column_name], dist="norm", plot=iad.pylab)
    iad.pylab.title("qqplot for " + column_name)
    iad.pylab.show()
    
def get_distribution_plot(df_filtered, column_name):
    ax = iad.sns.distplot(df_filtered[column_name], bins=50)
    ax.set(xlabel=column_name, ylabel='Frequency', title='Combined histogram and distribution plot for ' + column_name)
    iad.plt.show()

def get_bar_chart_single(df, column_x, column_y):
    plot_column = df.groupby(column_x)[column_y].sum()
    fig = iad.plt.figure()
    ax = fig.add_subplot(111)
    width = 0.4
    plot_column.plot(kind='bar', color='blue', ax=ax, width=width, position=0)
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y, color='red')
    iad.plt.show()

def get_bar_chart_double(df, column_x, column_y_1, column_y_2):
    plot_column_1 = df.groupby(column_x)[column_y_1].sum()
    plot_column_2 = df.groupby(column_x)[column_y_2].sum()
    fig = iad.plt.figure()
    ax = fig.add_subplot(111)
    ax2 = ax.twinx()
    width = 0.4
    plot_column_1.plot(kind='bar', color='orange', ax=ax, width=width, position=1)
    plot_column_2.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y_1, color='orange')
    ax2.set_ylabel(column_y_2, color='blue')
    ax.set_title('Sales')
    iad.plt.show()

def get_pie_chart(df, items, values):
    df.groupby(items)[values].sum().plot(kind='pie', autopct='%1.0f%%')
    iad.plt.show()










# =============================================================================
# def get_interval(confidense):
#     interval = iad.stats.t.interval(alpha=confidense, df=len(salery)-1, loc=iad.np.mean(salery), scale=iad.stats.sem(salery))
#     return interval
#     # print(interval)
# 
# def getConfidenceInterval(column, confidense):
#     interval = iad.stats.t.interval(alpha=confidense, df=len(salery)-1, loc=iad.np.mean(column), scale=iad.stats.sem(column))
#     return(interval)
#     # print(interval)
# 
# def getConfidenceInterval_values(column_name, confidense):
#     interval = get_interval(confidense)
#     intervalLow = interval[0]
#     intervalHigh = interval[1]
#     df_in_interval_95 = df[(df[column_name] < intervalHigh) & (df[column_name] > intervalLow)]
#     return df_in_interval_95
#     # print(df_in_interval_95)
# 
# def distribution_plot(column_name):
#     ax = iad.sns.distplot(df_2[column_name], bins=50)
#     ax.set(xlabel=column_name, ylabel='Frequency', title='Combined histogram and distribution plot for ' + column_name + ' quantile')
#     iad.plt.show()
# distribution_plot('salary')
# 
# def distribution_plot_org(df_filtered, column_name):
#     ax = iad.sns.distplot(df_filtered[column_name], bins=50)
#     ax.set(xlabel=column_name, ylabel='Frequency', title='Combined histogram and distribution plot for ' + column_name)
#     iad.plt.show()
# distribution_plot_org(df_2, 'salary')
# 
# def get_Histogram(column_name):
#     # interval = get_interval(confidense)
#     # intervalLow = interval[0]
#     # intervalHigh = interval[1]
#     df_hist = df[(df[column_name]
#     df_hist[column_name].plot.hist()
# 
# def qqplotOnConfidense(column_name, confidense):
#     iad.stats.probplot(getConfidenceInterval_values(column_name, confidense)[column_name], dist="norm", plot=iad.pylab)
#     iad.pylab.title("qqplot for " + column_name)
#     iad.pylab.show()
# 
# def distribution_plot_confidense(column_name, confidense):
#     ax = iad.sns.distplot(getConfidenceInterval_values(column_name, confidense)[column_name], bins=50)
#     ax.set(xlabel=column_name, ylabel='Frequency', title='Combined histogram and distribution plot for ' + column_name + ' confidense')
#     iad.plt.show()
# 
# def distribution_plot_with_optional_quantiles(column_name, quantile_1, quantile_2):
#     q_low_local = df[column_name].quantile(quantile_1)
#     q_hi_local  = df[column_name].quantile(quantile_2)
#     df_filtered_in_func = df[(df[column_name] < q_hi_local) & (df[column_name] > q_low_local)]
#     ax = iad.sns.distplot(df_filtered_in_func[column_name], bins=50)
#     ax.set(xlabel=column_name, ylabel='Frequency', title='Combined histogram and distribution plot for ' + column_name + ' quantile')
#     iad.plt.show()
# def qqplot_org(column_name):
#     iad.stats.probplot(df_1[column_name], dist="norm", plot=iad.pylab)
#     iad.pylab.title("qqplot for " + column_name)
#     iad.pylab.show()
# qqplot_org('salary')
# def getConfidenceIntervalHistogram(column_name, confidense):
#     interval = get_interval(confidense)
#     intervalLow = interval[0]
#     intervalHigh = interval[1]
#     df_in_interval_95 = df[(df[column_name] < intervalHigh) & (df[column_name] > intervalLow)]
#     df_in_interval_95[column_name].plot.hist()
#     
# def getHistogram_om_quantiles(column_name, q_low, q_high):
#     # interval = get_interval(confidense)
#     # intervalLow = interval[0]
#     # intervalHigh = interval[1]
#     df_in_interval_on_qs = df[(df[column_name] < q_high) & (df[column_name] > q_low)]
#     df_in_interval_on_qs[column_name].plot.hist()
# def qqplot_org(column_name):
#     iad.stats.probplot(df[column_name], dist="norm", plot=iad.pylab)
#     iad.pylab.title("qqplot for " + column_name)
#     iad.pylab.show()
# qqplot_org('Salary')
# 
# def qqplot_org(column_name):
#     iad.stats.probplot(df[column_name], dist="norm", plot=iad.pylab)
#     iad.pylab.title("qqplot for " + column_name)
#     iad.pylab.show()
# def distribution_plot(column_name):
#     ax = iad.sns.distplot(df_filtered[column_name], bins=50)
#     ax.set(xlabel=column_name, ylabel='Frequency', title='Combined histogram and distribution plot for ' + column_name + ' quantile')
#     iad.plt.show()
# 
# df = iad.df
# test = []
# df = iad.pd.read_csv("ds_salaries.csv")
# q_low = df["salary"].quantile(0.01)
# q_hi  = df["salary"].quantile(0.99)
# q_low_2 = df["salary"].quantile(0.05)
# q_hi_2  = df["salary"].quantile(0.95)
# df_filtered = df[(df["salary"] < q_hi) & (df["salary"] > q_low)]
# df_filtered_2 = df[(df["salary"] < q_hi_2) & (df["salary"] > q_low_2)]
# df = iad.pd.read_csv('data_files/automobile_1.csv', sep=';')
# df_2 = iad.pd.read_csv('data_files/automobile_2.csv', sep=';')
# 
# def qqplot_2(column_name):
#     stats.probplot(df_filtered_2[column_name], dist='norm', plot=pylab)
#     pylab.title("qqplot 2 for " + column_name)
#     pylab.show()
# 
# def distribution_plot_2(column_name):
#     ax = sns.distplot(df_filtered_2[column_name], bins=50)
#     ax.set(xlabel=column_name, ylabel='Frequency', title='Combined histogram and distribution plot 2 for ' + column_name)
#     plt.show()
# =============================================================================



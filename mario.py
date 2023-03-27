# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:56:40 2023

@author: janne
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from plotly.offline import plot
import cufflinks as cf
cf.go_offline()
import plotly.io as pio
pio.renderers.default = 'browser'
pd.options.plotting.backend = "plotly"
import statsmodels.api as sm
import plotly.graph_objs as go
import plotly.express as px
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier, plot_tree
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, mean_absolute_error


df = pd.read_csv('data_files/NetConsult AB - Mario kart 2023.csv')
df = df.fillna(0)


def explore_data(df_in):
    pd.set_option('display.max_columns', None)
    df_in.info()
    print(df_in.describe())
    print(df_in.head())
    

explore_data(df)
    
columns = df.columns.values

def top_three_winners():
    counts_dict = {}
    for col in df.columns[1:]:
        counts = df[col].eq(1).sum()
        if counts > 1:
            new_col_name = col
            counts_dict[new_col_name] = counts
            df[new_col_name] = (df[col] == 1).astype(int)
        elif counts == 1:
            counts_dict[col] = counts
            df[col] = (df[col] == 1).astype(int)
            winners_df = pd.DataFrame(counts_dict.items(), columns=['Column', 'Count'])
            winners_df = winners_df[winners_df.index != 9]
            winners_df = winners_df.nlargest(3, 'Count')

    colors = ["#FEBFB3", "#7A9ECE", "#0EBFB8"]
    # colors = ["#7A9ECE"]
    fig = px.bar(winners_df, x='Column', y='Count',
                 color='Column',
                 color_discrete_sequence=colors,
                 # text='Users',
                 # hover_data=['Columns'],
                 height=600,
                 title='Top three winners',)

    fig.update_layout(yaxis_title='Good work :-)',
                      xaxis_title='', 
                      yaxis_tickvals=[],
                      yaxis_ticktext=[],
                      yaxis=dict(tickformat=',d'), 
                      legend=dict(title='And the top three winner are:'),
                      font=dict(family='Arial, sans-serif', size=14),
                      plot_bgcolor='#878787', showlegend=True)
    # plot_bgcolor='#E6E9EC', showlegend=True)
    
    # fig.add_trace(go.Scatter(
    #     x=winners_df['Column'],
    #     y=winners_df['Count'] +20,
    #     mode='lines',
    #     line=dict(color='green'),
    #     showlegend=False) )
    
    # chart_studio.tools.set_credentials_file(username='welovedigital', api_key='vEOCO1kkrBPSsWe2s1fy')
    # py.plot(fig, filename='Scroll analysis', auto_open=False, sharing='public')
    
    fig.show()


















































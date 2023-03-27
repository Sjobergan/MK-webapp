from DjangoWebProject1 import test as t
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from matplotlib import pyplot as plt
from DjangoWebProject1 import settings as st
import io, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from django.http import HttpResponse


def split_string(string_to_split):
    x = string_to_split.split('/')
    return x

#def create_df(request, sepa):
#    created_df = pd.DataFrame
#    if request.POST.get('open_csv_file_btn_1'):
#        file_path = t.get_filepath()
#        file_name = split_string(file_path)[-1]
#        if not file_path == '' or not file_name == '':
#            created_df = pd.read_csv(file_path, sep=sepa)
#        if not created_df.empty:
#            st.df_1 = created_df
#    return created_df, file_name

def create_df(request, sepa):
    created_df = pd.DataFrame
    file_path = t.get_filepath()
    file_name = split_string(file_path)[-1]
    if not file_path == '' or not file_name == '':
        created_df = pd.read_csv(file_path, sep=sepa)
    if not created_df.empty:
        st.df_1 = created_df
    return created_df, file_name

def consume_html(request):
    output = ''     
    if (request.POST.get('testbutton')):
        value = request.POST.get('testinput')
        output = value
    return output

def get_bar_chart_single(df, column_x, column_y, request):
    my_dpi = 96
    if not df.empty:
        plot_column = df.groupby(column_x)[column_y].sum()
        fig = plt.figure(figsize=(800/my_dpi, 900/my_dpi), dpi=my_dpi)
        fig.tight_layout()
        ax = fig.add_subplot(111)
        width = 0.4
        plot_column.plot(kind='bar', color='blue', ax=ax, width=width, position=0)
        ax.set_xlabel(column_x)
        ax.set_ylabel(column_y, color='red')
        plt.xticks(rotation=35, ha='right')
        plt.ylim([50, 1000])

        flike = io.BytesIO()
        fig.savefig(flike)
        graph = base64.b64encode(flike.getvalue()).decode()

        return graph

def top_three_winners(df):
    my_dpi = 96
    import plotly.graph_objs as go
    import plotly.offline as pyo
    import plotly.express as px
    import pandas as pd

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
    winners_df = winners_df[winners_df.Column != 'Poäng']
    winners_df = winners_df.nlargest(3, 'Count')

    colors = ["#FEBFB3", "#7A9ECE", "#0EBFB8"]
    fig = px.bar(winners_df, x='Column', y='Count',
                color='Column',
                color_discrete_sequence=colors,
                title='Top three winners')

    fig.update_layout(yaxis_title='Good work :-)',
                      xaxis_title='', 
                      yaxis_tickvals=[],
                      yaxis_ticktext=[],
                      width=1200, 
                      height=800,
                      yaxis=dict(tickformat=',d'), 
                      legend=dict(title='And the top three winner are:'),
                      font=dict(family='Arial, sans-serif', size=14),
                      plot_bgcolor='#878787', showlegend=True)

    # create a BytesIO object to hold the PNG image data
    flike = io.BytesIO()

    # write the figure to the BytesIO object as a PNG image using the kaleido engine
    fig.write_image(flike, format='png', engine='kaleido')

    # encode the PNG image data as base64
    graph = base64.b64encode(flike.getvalue()).decode()

    # return the base64-encoded PNG image data
    return graph
    



def top_three_winners_new_oldis(df):
    # Create a dataframe
    winners_df = pd.DataFrame()
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

    # Define colors for the bar chart
    colors = ["#FEBFB3", "#7A9ECE", "#0EBFB8"]

    # Create a bar chart using Plotly
    fig = go.Figure(go.Bar(x=winners_df['Column'], y=winners_df['Count'], marker_color=colors))

    # Set chart title and axis labels
    fig.update_layout(title='Top three winners', yaxis_title='Good work :-)', xaxis_tickangle=-45)

    # Format y-axis tick labels with comma separator
    fig.update_yaxes(tickformat=',')
    
    # Set legend title and position
    fig.update_layout(legend=dict(title='And the top three winner are:', orientation='h', yanchor='bottom', y=-0.2, xanchor='right', x=1))

    # Set plot background color
    fig.update_layout(plot_bgcolor='#878787')

    # Convert the plot to a PNG image data URI
    graph = fig.to_image(format='png', engine='kaleido')

    # Return the base64-encoded PNG image data
    return base64.b64encode(graph).decode()

def top_three_winners_old(df):
    my_dpi = 96
    # Create a dataframe
    winners_df = pd.DataFrame()
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

    # Define colors for the bar chart
    colors = ["#FEBFB3", "#7A9ECE", "#0EBFB8"]

    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots(figsize=(900/my_dpi, 900/my_dpi), dpi=my_dpi)
    winners_df.plot(kind='bar', x='Column', y='Count', ax=ax, color=colors)

    # Set chart title and axis labels
    ax.set_title('Top three winners')
    ax.set_ylabel('Good work :-)')

    # Remove x-axis tick labels
    ax.tick_params(axis='x', labelbottom=False)

    # Format y-axis tick labels with comma separator
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

    # Remove legend title and set legend position
    ax.legend(title='And the top three winner are:', loc='upper right')

    # Set plot background color
    ax.set_facecolor('#878787')

    # Save the plot as a PNG image to a BytesIO buffer
    flike = io.BytesIO()
    plt.savefig(flike, format='png', bbox_inches='tight')
    plt.close()

    # Encode the PNG image data as base64
    graph = base64.b64encode(flike.getvalue()).decode()

    # Return the base64-encoded PNG image data
    return graph


### One way to present graph in html ###
#def plot(request):
#    # Data for plotting
#    t = np.arange(0.0, 2.0, 0.01)
#    s = 1 + np.sin(2 * np.pi * t)
#    fig, ax = plt.subplots()
#    ax.plot(t, s)
#    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#           title='About as simple as it gets, folks')
#    ax.grid()
#    response = HttpResponse(content_type = 'image/png')
#    canvas = FigureCanvasAgg(fig)
#    canvas.print_png(response)
#    return response

### another way to present plots in html ###
# flike = io.BytesIO()
#fig.savefig(flike)
#graph = base64.b64encode(flike.getvalue()).decode()
 
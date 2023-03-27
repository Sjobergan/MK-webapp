"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from DjangoWebProject1 import get_df as gd
from DjangoWebProject1 import test as t
from IPython.display import display, HTML
from DjangoWebProject1 import settings as st


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def test_func(request):
    df = st.df_1.dropna()
    if not df.empty and request.POST.get('open_csv_file_btn_1'):
        test = gd.get_bar_chart_single(df, 'company', 'horsepower', request)
        return test

def get_df():
    df = st.df_1

def table_df(request, sepa):
    df, file_name = gd.create_df(request, ',')
    if not df.empty:
        html_df = df.to_html(index=False).replace('border="1"', 'border"0"')
        return html_df, file_name


def mariostats(request):
    html_df = ''
    testing = ''
    file_name_1 = ''
    file_name_2 = ''
    html_df, file_name_1 = table_df(request, ',')
    df = st.df_1
    chart = gd.top_three_winners(df)

    test = ''
    #if request.POST.get('open_csv_file_btn_1'):
    #    html_df, file_name_1 = table_df(request, ',')
    #    testing = test_func(request)

    return render(
        request,
        'app/mariostats.html',
        {
            'title': 'Mariostats',
            'message': 'Här finns lite intressant statistik för er mariocart :-)',
            'year': datetime.now().year, 
            'data_frame': html_df,
            'graph': chart,
        }
    )


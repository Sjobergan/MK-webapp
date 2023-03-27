from DjangoWebProject1 import functions_input as fi
from DjangoWebProject1 import functions_joins as fj
from DjangoWebProject1 import functions_for_plot as ffp
#from DjangoWebProject1 import imports_and_df as iad
#from app import views as vi
from DjangoWebProject1 import get_df



# print(df.info())
# Remember to fix so that user can use their joine df through all of the program
# start = input('Please type the number for what you want to do. ' + 'Type stop if you do not want to run it anymore: ')
def startFunction():
    numbers = {'Search,': '1', 'Diagrams': '2', 'Interesting information': '3', 'Joins': '4'}
    for k, v in numbers.items():
        print(k, v)
    start = get_df.present_in_html('Please type the number for what you want to do. ' + 'Type stop if you do not want to run it anymore: ')    
    if start == '1':
        fi.printAndConsumeSearch()
        startFunction()
    elif start == '2':
        ffp.get_diagrams_on_dataframe()
        startFunction()
    elif start == '3':
        fi.get_iteresting_info()
        startFunction()
    elif start == '4':
        fj.make_different_joins()
        startFunction()
    elif start == 'stop':
        print('Thank you for testing my dataframe searchprogram')
    else:
        print('That number, search is not developted yet, please choose another.')
        startFunction()
startFunction()

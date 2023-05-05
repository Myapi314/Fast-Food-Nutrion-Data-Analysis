import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import webbrowser

def main():
    # Read the csv file into a pandas DataFrame
    fastfood = pd.read_csv('fastfood.csv', delimiter=',')

    # Get the column headers and the restaurants
    places = fastfood['restaurant'].unique()
    columns = fastfood.columns

    # Initialize the string containing html script
    htmlTxt = '<h1>Review of the Tables Created</h1>'
    print('\nExplore Further!\n')

    print('Compare other restaurants statistical summary of calories similar to Question One.')

    # Return the two restaurant choices
    placesChosen = []
    placesChosen.append(places[display_options(places)])
    placesChosen.append(places[display_options(places)])

    # Append the stylized html to the htmlTxt variable
    htmlTxt += summarize_data(fastfood) + '<br>'
    htmlTxt += get_row_by_restaurant(fastfood, placesChosen) + '<br>'

    # Break up entering the data so its easier for user
    input('Let\'s enter some more information. Press enter to continue\n')

    # Append stylized html of the table structured after question 2
    print('Compare other nutrition facts as in Question 2')
    col = columns[display_options(columns)]
    htmlTxt += get_max_rows(fastfood, col) + '<br>'

    # Enter in a common menu item term to create table of similar items and append to html
    input('Last bit of information. Press enter to continue\n')
    search = input('Enter a common menu item name: ')
    htmlTxt += get_nutrition_data_by_item(fastfood, search) + '<br>'

    # Write the html string to the file
    with open('fastfood.html', 'w') as htmlFile:
        htmlFile.write(htmlTxt)


    # open html file in a web browser
    webbrowser.open('fastfood.html') 

def display_options(places):
    input('Press enter to continue\n')
    for i in range(len(places)):
        print(f'{i+1}. {places[i]}')
    
    i = int(input(f'Enter a number (1-{len(places)}): '))
    while i < 1 or i > len(places):
       i = int(input(f'**Choose a valid number (1-{len(places)}):** '))

    print(f'You chose {places[i - 1]} \n') 
    return i - 1

def display_plot(fastfood):
    # Select portion of the data by label (column)
    calorieData = fastfood.loc[:, ["restaurant", "calories"]]

    # Create plot of the calorie data by restaurant in a box plot
    calorieData.plot.box(by='restaurant', title='Calorie Distribution Across Menu Items', 
                figsize=(10, 5),
                yticks=np.arange(0,2750,250),
                xlabel='Restaurants', ylabel='Calories')

    # Show box plot
    plt.show()

def summarize_data(fastfood):
    # Create new dataFrame with quick statistical summary data
    summary = fastfood.groupby('restaurant').describe()["calories"]

    # Display the stylized table
    return summary.style.set_caption("Statistical Summary of Calories") \
    .format(precision=1) \
    .to_html()

def get_row_by_restaurant(fastfood, restaurants):
    # Create new dataFrame with quick statistical summary data
    summary = fastfood.groupby('restaurant').describe()["calories"]

    # Select by index (row)
    return summary.loc[restaurants] \
    .style.format(precision=1) \
    .set_caption(f'Comparing {restaurants[0]} and {restaurants[1]} Calories') \
    .highlight_max(subset='mean', color='yellow') \
    .to_html()

def get_max_rows(fastfood, column):
    # Select and sort by column, and select tail of data
    data = fastfood.loc[:, ['restaurant', 'item', column]].dropna(axis=0) \
    .sort_values([column]).tail()

    # Stylize and display the table
    return data.style \
    .format_index(str.capitalize, axis=1) \
    .format(precision=1) \
    .hide(axis=0) \
    .set_caption(f'Menu Items with Maximum {column.capitalize()}') \
    .to_html()

def get_nutrition_data_by_item(fastfood, search_key):
    # Create series of bools. True if item name contains search_key, ignore case
    nutrition_data = fastfood['item'].str.contains(pat=search_key, case=False)

    # Create list of indexes where 'nuggets' was in the item name
    i = nutrition_data[nutrition_data].index

    # Select rows based on list of indexes
    table = fastfood.iloc[i, :13]

    return table.style.set_caption(f'Nutrition Data for \'{search_key.capitalize()}\' ') \
    .format(precision=1) \
    .format_index(str.capitalize, axis=1) \
    .hide(axis=0) \
    .highlight_max(subset=table.columns[2:], color='yellow') \
    .to_html()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
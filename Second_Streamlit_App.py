#Second Streamlit App
#Formatted Structure

# Import all lib

import streamlit
import pandas
import requests
import snowflake.connector



streamlit.title('My parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick Some Fruits :", list(my_fruit_list.index),['Avocado','Honeydew'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#New Section to display Fruityvice api response
streamlit.header('Fruityvice Fruit Advice')

# New Section to dsplay Fruitvicy api response
#import requests

fruit_Choice=streamlit.text_input('What Fruit would you like information about ?','Kiwi')
streamlit.write('user asks for',fruit_Choice)

# Import requests
fruit_Choice_response=requests.get("https://www.fruityvice.com/api/fruit/" + fruit_Choice)
streamlit.text(fruit_Choice_response.json())
fruitvicy_normalize=pandas.json_normalize(fruit_Choice_response.json())
streamlit.dataframe(fruitvicy_normalize)

#Snow to Streamlit connection
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST;")
my_data_row = my_cur.fetchall()
streamlit.header("FRUIT_LOAD_LIST Contains")
streamlit.dataframe(my_data_row)
#Add Multi Select List
AddFruitFromList=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
AddedFruit=AddFruitFromList.set_index('Fruit')
#New Section to display Fruityvice api response
streamlit.header('Fruityvice Added Fruit')
fruitChoice=streamlit.text_input('What Fruit would you like information about ?')
streamlit.write('user asks for',fruitChoice)

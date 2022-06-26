import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

# create repetable code block (called funcation)
def get_fruityvice_data(this_fruit_choice):
    fruit_Choice_response=requests.get("https://www.fruityvice.com/api/fruit/" + fruit_Choice)
    fruitvicy_normalize=pandas.json_normalize(fruit_Choice_response.json())
    return fruitvicy_normalize

#New Section to display Fruityvice api response
streamlit.header('Fruityvice Fruit Advice')

# New Section to dsplay Fruitvicy api response



#import requests

#fruitvicy_response=requests.get("https://www.fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruitvicy_response)
#streamlit.text(fruitvicy_response.json())
# Displaying jSON data on application
#fruitvicy_normalize=pandas.json_normalize(fruitvicy_response.json())
#streamlit.dataframe(fruitvicy_normalize)
try:
    fruit_Choice=streamlit.text_input('What Fruit would you like information about ?')

    if not fruit_Choice:
     streamlit.error("Please select fruit to get information")
  
    else: 
  
#streamlit.write('user asks for',fruit_Choice)
# Import requests
     #fruit_Choice_response=requests.get("https://www.fruityvice.com/api/fruit/" + fruit_Choice)
     #streamlit.text(fruit_Choice_response.json())
     #fruitvicy_normalize=pandas.json_normalize(fruit_Choice_response.json())
     #streamlit.dataframe(fruitvicy_normalize)
     back_fromfuncation=get_fruityvice_data(fruit_Choice)
     streamlit.dataframe(back_fromfuncation)

except URLError as e:
  streamlit.error()

#dont run anything past here while we trouble shoot
#streamlit.stop()

#Snow to Streamlit connection



#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST;")
#my_data_row = my_cur.fetchall()
streamlit.header("FRUIT_LOAD_LIST Contains")

# Snowflake related funcations
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
         return my_cur.fetchall()

# Add button to load the fruit
if streamlit.button('Get fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruit_load_list()
    streamlit.dataframe(my_data_row)   

#streamlit.dataframe(my_data_row)

# Allow end users to add fruit to list

def insert_rows_insnowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES('from streamlit')")
         return "Thanks for adding"+new_fruit
add_my_fruit=streamlit.text_input('What fruit would you like to add')
if streamlit.button('Add fruit to the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_funcation=insert_rows_insnowflake(add_my_fruit)
   streamlit.text(back_from_funcation)


# Allow end users to add fruit to list
            
            
streamlit.stop()
#Add Multi Select List

AddFruitFromList=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

AddedFruit=AddFruitFromList.set_index('Fruit')

#New Section to display Fruityvice api response
streamlit.header('Fruityvice Added Fruit')

fruitChoice=streamlit.text_input('What Fruit would you like information about ?')
streamlit.write('Thanks for Adding Fruit',fruitChoice)

my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('from stremlit')")

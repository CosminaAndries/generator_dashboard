import streamlit as st 
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import home, data_cleaning_pane,visualization_pane

st.title("DashBoard Generator")
st.markdown("<h3 style='font-size:24px'>Upload a date file:</h3>",unsafe_allow_html=True)
fisiere_de_incarcat=st.file_uploader(" ",type=["csv","json"])
def procesare_fisier():
  try:
   if fisiere_de_incarcat is not None :
     if fisiere_de_incarcat.name.endswith(".json"):
       df=pd.read_json(fisiere_de_incarcat)
       st.write("The data found in the files")
       st.session_state.data=df
       st.dataframe(df)
     else :
       df=pd.read_csv(fisiere_de_incarcat)
       st.write("The data found in the files")
       st.session_state.data=df
       st.dataframe(df)
  except Exception as e :
   st.error(f"Eroare la incarcarea fisierului!{e}")
  
st.set_page_config(
  page_title="Home Page"
)
class Multiapp:
  def __init__(self):
    self.apps=[]   
  def add_app(self,title,function):
    self.apps.append({
      "title":title,
      "function":function
    })
  def run():
     with st.sidebar:
      app=option_menu(
        menu_title="Menu",
        menu_icon="list",
        options=['Home','Cleaning','Visualization'],     
        icons=['home','broom' ,'bar_chart'],
        styles={
          "icon":{ "color":"white", "font-size":"23px"},
          "nav-link":{"color":"white", "font-size":"20px","text-align":"left","margin":"0px","--hover-color":"blue"},
          "nav-link-selected":{"background-color":"#02ab21"},
          }
      )
     if app=="Home":
        home.app()
     elif app=="Visualization":
        visualization_pane.app()
     elif app=="Cleaning":
        data_cleaning_pane.cleaning.app()
      
  run()

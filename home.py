import streamlit as st 
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from streamlit_option_menu import  option_menu

st.set_page_config(
  page_title="Home Page"
)
def app():
 st.title("DashBoard Generator")
 st.markdown("<h3 style='font-size:24px'>Welcome to my app!</h3>",unsafe_allow_html=True)
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
  



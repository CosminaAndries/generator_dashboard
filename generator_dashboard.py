
import streamlit as st 
import pandas as pd

st.title("DashBoard Generator")
st.markdown("<h3 style='font-size:24px'>Incarcati un fisier de date</h3>",unsafe_allow_html=True)
fisiere_de_incarcat=st.file_uploader(" ",type=["csv","json"])


def procesare_fisier():
 try:
   if fisiere_de_incarcat is not None :
     if fisiere_de_incarcat.name.endswith(".json"):
       df=pd.read_json(fisiere_de_incarcat)
       st.write("Datele din fisiere")
       st.dataframe(df)
     else :
       df=pd.read_csv(fisiere_de_incarcat)
       st.write("Datele din fisiere")
       st.dataframe(df)
 except Exception as e :
   st.error(f"Eroare la incarcarea fisierului!{e}")
    
procesare_fisier();

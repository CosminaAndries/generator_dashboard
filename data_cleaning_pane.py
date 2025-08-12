import streamlit as st
import pandas as pd

def procesare_fisier(fisiere_de_incarcat):
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
coloane_valori_lipsa=[]
def verificare_coloane_null(df):
 for col in df.columns:
   numar=df[col].isnull.sum()
   procentaj=(numar/df.shape[1])*100
   if numar>0 :
     coloane_valori_lipsa.apend({
    "numecoloana":df[col],
    "numar valori lipsa":numar,
    "procentaj":procentaj})
 st.write(coloane_valori_lipsa)
 
     
    

def app():
  st.title("Data Cleaning Page")
  fisiere_de_incarcat=st.file_uploader(" ",type=["csv","json"])
  procesare_fisier(fisiere_de_incarcat)
  df=st.session_state.data
  verificare_coloane_null(df)
  if coloane_valori_lipsa is not None:
    preferinta=st.select_box("How do you want to handle the missing data",options=("Remove Columns","Replace with mean "))
  # if preferinta=="Remove Columns" :
      
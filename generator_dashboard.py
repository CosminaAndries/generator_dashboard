
import streamlit as st 
import pandas as pd

st.title("DashBoard Generator")
st.markdown("<h3 style='font-size:24px'>Incarcati un fisier de date</h3>",unsafe_allow_html=True)
fisiere_de_incarcat=st.file_uploader(" ",type=["csv"])
def procesare_fisier():
 if fisiere_de_incarcat is not None :
    df=pd.read_csv(fisiere_de_incarcat)
    st.write("Datele din fisiere")
    st.dataframe(df)
    
 else:
    st.write("Fisierul nu s-a incarcat!")
    
procesare_fisier();

import streamlit as st 
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

if "data" not in st.session_state:
    st.session_state.data = None

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
def app():
  st.title("Chart")
  df=None
  fisiere_de_incarcat=st.file_uploader(" ",type=["csv","json"])
  procesare_fisier( fisiere_de_incarcat)
  choice_of_which_chart_to_use=st.selectbox('What chart do you want your data to be displayed with?',('None','Bar Chart','Line Chart','Area Chart','Map Chart','Scatterplot Chart','Histograms','Pie Chart'))
  if choice_of_which_chart_to_use=='Bar Chart' :
    if st.session_state.data is not None:
     x=st.text_input("What column do you use for the x-axis:")
     y=st.text_input("What column do you use for the y-axis:")
     df=st.session_state.data
     if x and  y  and x in df.columns and y in df.columns :
      data=st.dataframe(df[[x,y]])
      x_label=st.text_input('x-label:')
      y_label=st.text_input('y label:')
      horizontal=st.text_input('Do you want the bars to be placed horizontally?')
      horizontal=True if  horizontal=='Yes' else False
      color=st.text_input('If you want collor you can only use RGA color code or HEX code:')
      if color=="None"or color=="No":
       color="#d59a75"
      grafic=st.bar_chart(data=df,x=x,y=y,color=color,horizontal=horizontal )
      fn='bar.png'
     plt.savefig(fn)
     with open(fn,"rb") as img:
      btn=st.download_button(
       label="Download image",
       data=img.read(),
       file_name=fn,
       mime="image/png"
      )
  elif choice_of_which_chart_to_use=='Line Chart' :
   if st.session_state.data is not None:
    x=st.text_input("What column do you use fot the x-axis:")
    y=st.text_input("What column do you use fot the y-axis:")
    df=st.session_state.data
    if x and  y  and x in df.columns and y in df.columns :
      data=st.dataframe(df[[x,y]])
      x_label=st.text_input('x-label:')
      y_label=st.text_input('y label:')
      color=st.text_input('If you want collor you can only use RGA color code or HEX code:')
      if color=="None"or color=="No":
       color="#d59a75"
       grafic=st.line_chart(data=df,x=x,y=y,color=color )
       fn='scatter.png'
       plt.savefig(fn)
       with open(fn,"rb") as img:
        btn=st.download_button(
        label="Download image",
        data=img.read(),
        file_name=fn,
        mime="image/png"
      )
  elif choice_of_which_chart_to_use=='Map Chart' :
   if st.session_state.data is not None:
    df=st.session_state.data
    latitude=st.selectbox("Latitude:",options=df.columns)
    longitude=st.selectbox("Longitude:",options=df.columns)
    df[latitude] = pd.to_numeric(df[latitude], errors='coerce')
    df[longitude] = pd.to_numeric(df[longitude], errors='coerce')
    if latitude in df.columns and longitude in df.columns :
      #data=(df[[latitude,longitude]].dropna().copy())
      #data.columns=['lat','lon']
      data={"lat":df[latitude],"lon":df[longitude]}
      data=pd.DataFrame(data)
      data.dropna()
      grafic=st.map(data)
      
      fn='map.png'
      plt.savefig(fn)
      with open(fn,"rb") as img:
        btn=st.download_button(
        label="Download image",
        data=img.read(),
        file_name=fn,
        mime="image/png"
      )
  elif choice_of_which_chart_to_use=='Histograms':
   if st.session_state is not None:
    df=st.session_state.data
    x=st.text_input("The values:")
    bins = st.number_input("Bins:", min_value=1, max_value=100, value=10, step=1)
    optiuni_avansate=st.checkbox("Advance Options")
    if optiuni_avansate==True:
      density = st.number('Density') 
      #range=st.number_input('Range:')
      histtype=st.selectbox("Default","barstacked","step","stepfilled")
      if histtype=="Default":
        histtype="bar"
      align=st.selectbox("low","mid","right")
      color=st.text_input("Color:")
      log=st.text_input("Log Scale:")
      if log=='yes' or log== 'Yes' :
        log=True
      elif log=='no'or log=='No':
        log=False
      plt.hist(df[x],bins=bins,color=color,histtype=histtype,align=align, log=log,density=density)
      title=st.text_input('Title:')
      label_x=st.text_input('Label for the values:')
      label_y=st.text_input('Label for the frequency:')
      plt.xlabel(label_x)
      plt.ylabel(label_y)
      st.pyplot(plt)
      
      fn='histogram.png'
      plt.savefig(fn)
      with open(fn,"rb") as img:
        btn=st.download_button(
         label="Download image",
         data=img.read(),
         file_name=fn,
         mime="image/png")
    else: 
      plt.hist(df[x],bins=bins)
      title=st.text_input('Title:')
      label_x=st.text_input('Label for the values:')
      label_y=st.text_input('Label for the frequency:')
      plt.xlabel(label_x)
      plt.ylabel(label_y)
      st.pyplot(plt)
      fn='histogram.png'
      plt.savefig(fn)
      with open(fn,"rb") as img:
        btn=st.download_button(
        label="Download image",
        data=img.read(),
        file_name=fn,
        mime="image/png"
      )
  elif choice_of_which_chart_to_use=='Pie Chart':
   if st.session_state is not None:
    df=st.session_state.data
    x=st.text_input("The values:")
    optiuni_avansate=st.checkbox("Advance Options")
    if optiuni_avansate==True:
      shadow = st.selectbox("Shadow",('Yes','No') )
      if shadow=='Yes':
        shadow=True
      else:
        shadow=False
      start_angle= st.number_input("Start angle:")
      color = st.text_input("Colors (separate with commas):")
      color = [c.strip() for c in color.split(',')] if color else None
      autopunct= '%1.1f%%'
      labels = st.text_input('Labels (separate with commas):')
      labels = [str(lbl).strip() for lbl in labels.split(',')] if labels else None
      plt.pie(data=df[x],color=color,autopct= autopunct,startangle=start_angle, labels=labels)
      title=st.text_input('Title:')
      st.pyplot(plt)
      fn='pie.png'
      plt.savefig(fn)
      with open(fn,"rb") as img:
        btn=st.download_button(
         label="Download image",
         data=img.read(),
         file_name=fn,
         mime="image/png")
    else:
      #labels = st.text_input('Labels (separate with commas):')
      title=st.text_input('Title:')
      labels=st.selectbox('Selecteaza coloana de etichete',options=df.columns)
      st.pyplot(plt,labels=labels)
      fn='pie_chart.png'
      plt.savefig(fn)
      with open(fn,"rb") as img:
        btn=st.download_button(
        label="Download image",
        data=img.read(),
        file_name=fn,
        mime="image/png"
      )
 
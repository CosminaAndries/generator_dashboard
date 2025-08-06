import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

st.title("DashBoard Generator")
st.markdown("<h3 style='font-size:24px'>Upload a date file:</h3>", unsafe_allow_html=True)

fisiere_de_incarcat = st.file_uploader(" ", type=["csv", "json"])


def procesare_fisier():
    try:
        if fisiere_de_incarcat is not None:
            if fisiere_de_incarcat.name.endswith(".json"):
                df = pd.read_json(fisiere_de_incarcat)
            else:
                df = pd.read_csv(fisiere_de_incarcat)

            st.write("The data found in the file:")
            st.session_state.data = df
            st.dataframe(df)
    except Exception as e:
        st.error(f"Eroare la incarcarea fisierului! {e}")


procesare_fisier()

page = st.sidebar.radio("Navigare", ["DataCleaning", "Visualization"])

if page == "Visualizations":
    choice_of_which_chart_to_use = st.selectbox(
        'What chart do you want your data to be displayed with?',
        ('None', 'Bar Chart', 'Line Chart', 'Area Chart', 'Map Chart', 'Scatterplot Chart', 'Histograms', 'Pie Chart')
    )

    if choice_of_which_chart_to_use == 'Bar Chart':
        if "data" in st.session_state:
            x = st.text_input("What column do you use for the x-axis:")
            y = st.text_input("What column do you use for the y-axis:")
            df = st.session_state.data

            if x and y and x in df.columns and y in df.columns:
                st.dataframe(df[[x, y]])
                x_label = st.text_input('x-label:')
                y_label = st.text_input('y-label:')
                horizontal = st.text_input('Do you want the bars to be placed horizontally? (Yes/No)')
                horizontal = True if horizontal == 'Yes' else False
                color = st.text_input('If you want color, use RGB or HEX code:')
                if not color or color.lower() in ["none", "no"]:
                    color = "#d59a75"

                st.bar_chart(data=df, x=x, y=y, color=color, horizontal=horizontal)
                fn = 'bar.png'
                plt.savefig(fn)
                with open(fn, "rb") as img:
                    st.download_button(
                        label="Download image",
                        data=img.read(),
                        file_name=fn,
                        mime="image/png"
                    )
    elif choice_of_which_chart_to_use == 'Line Chart':
        if "data" in st.session_state:
            x = st.text_input("What column do you use for the x-axis:")
            y = st.text_input("What column do you use for the y-axis:")
            df = st.session_state.data

            if x and y and x in df.columns and y in df.columns:
                st.dataframe(df[[x, y]])
                color = st.text_input('If you want color, use RGB or HEX code:')
                if not color or color.lower() in ["none", "no"]:
                    color = "#d59a75"

                st.line_chart(data=df, x=x, y=y, color=color)
                fn = 'line.png'
                plt.savefig(fn)
                with open(fn, "rb") as img:
                    st.download_button(
                        label="Download image",
                        data=img.read(),
                        file_name=fn,
                        mime="image/png"
                    )

    # MAP CHART
    elif choice_of_which_chart_to_use == 'Map Chart':
        if "data" in st.session_state:
            latitude = st.text_input("Latitude column:")
            longitude = st.text_input("Longitude column:")
            df = st.session_state.data

            if latitude and longitude and latitude in df.columns and longitude in df.columns:
                st.dataframe(df[[latitude, longitude]])
                st.map(df, latitude=latitude, longitude=longitude)
                fn = 'map.png'
                plt.savefig(fn)
                with open(fn, "rb") as img:
                    st.download_button(
                        label="Download image",
                        data=img.read(),
                        file_name=fn,
                        mime="image/png"
                    )

    # HISTOGRAMS
    elif choice_of_which_chart_to_use == 'Histograms':
        if "data" in st.session_state:
            df = st.session_state.data
            x = st.text_input("The values column:")
            bins = st.number_input("Bins:", min_value=1, max_value=100, value=10, step=1)
            optiuni_avansate = st.checkbox("Advance Options")

            if optiuni_avansate:
                density = st.checkbox('Density')
                histtype = st.selectbox("Histogram type", ["Default", "barstacked", "step", "stepfilled"])
                if histtype == "Default":
                    histtype = "bar"
                align = st.selectbox("Align", ["left", "mid", "right"])
                color = st.text_input("Color:")
                log = st.text_input("Log Scale (Yes/No):")
                log = True if log.lower() == 'yes' else False

                plt.hist(df[x], bins=bins, color=color, histtype=histtype, align=align, log=log, density=density)
            else:
                plt.hist(df[x], bins=bins)

            title = st.text_input('Title:')
            label_x = st.text_input('Label for the values:')
            label_y = st.text_input('Label for the frequency:')
            plt.xlabel(label_x)
            plt.ylabel(label_y)
            st.pyplot(plt)

            fn = 'histogram.png'
            plt.savefig(fn)
            with open(fn, "rb") as img:
                st.download_button(
                    label="Download image",
                    data=img.read(),
                    file_name=fn,
                    mime="image/png"
                )

    # PIE CHART
    elif choice_of_which_chart_to_use == 'Pie Chart':
        if "data" in st.session_state:
            df = st.session_state.data
            x = st.text_input("The values column:")
            optiuni_avansate = st.checkbox("Advance Options")

            if optiuni_avansate:
                shadow = st.selectbox("Shadow", ('Yes', 'No'))
                shadow = True if shadow == 'Yes' else False
                start_angle = st.number_input("Start angle:")
                color = st.text_input("Colors (separate with commas):")
                color = [c.strip() for c in color.split(',')] if color else None
                autopunct = '%1.1f%%'
                labels = st.text_input('Labels (separate with commas):')
                labels = [str(lbl).strip() for lbl in labels.split(',')] if labels else None

                plt.pie(df[x], colors=color, autopct=autopunct, startangle=start_angle, labels=labels, shadow=shadow)
            else:
                labels = st.text_input('Labels (separate with commas):')
                labels = [str(lbl).strip() for lbl in labels.split(',')] if labels else None
                plt.pie(df[x], labels=labels)

            title = st.text_input('Title:')
            st.pyplot(plt)

            fn = 'pie.png'
            plt.savefig(fn)
            with open(fn, "rb") as img:
                st.download_button(
                    label="Download image",
                    data=img.read(),
                    file_name=fn,
                    mime="image/png"
                )

      
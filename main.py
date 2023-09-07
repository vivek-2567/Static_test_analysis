import streamlit as st
from plotly.express import line
from pandas import read_csv
from scipy.integrate import simps
from numpy import trapz

st.set_page_config(page_title ="Static Test", layout="wide")

page_style = '''
                <style>
                footer {visibility: hidden;}
                </style>
            '''

st.markdown(page_style,unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: Dark Gray;'>Static Test Analysis</h1>",
            unsafe_allow_html=True)

file = st.file_uploader("Upload the csv file",type = 'csv')

if file:
    df = read_csv(file)
    c1,c2 = st.columns(2)
    with c1:
        st.subheader("Preview of the dataframe: ")
        st.dataframe(df)
    with c2:
        x_axis = st.selectbox("X-axis",df.columns)
        y_axis = st.selectbox("Y-axis",df.columns,index=1)
        x_axis_label = st.text_input("Label of x-axis",value = df.columns[0])
        y_axis_label = st.text_input("Label of y-axis",value = df.columns[1])
        title = st.text_input("Title of the Graph",value="Static Test plot")
        weight = int(st.text_input("Enter the weight of the propellent used in gms",value = 1))

a,b,c = st.columns(3)
with b:
    button = st.button("Make plot")


if button:
    fig = line(df, x=x_axis, y=y_axis, title=title,width = 1080, height = 720,
                    labels = {
                        x_axis:x_axis_label,
                        y_axis:y_axis_label
                    })
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Additional information:")
    impulse = trapz(df[y_axis],df[x_axis])/1000
    st.text("Impulse: "+str(impulse))
    spec_imp1 = trapz(df[y_axis],df[x_axis])/weight
    spec_imp2 = simps(df[y_axis],df[x_axis])/weight
    st.text("Specific Impulse Trapizoid Formula: "+str(spec_imp1))
    st.text("Specific Impulse Simpsons Formula: "+str(spec_imp2))
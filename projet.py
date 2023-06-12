import streamlit as st
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Manipulation and Visualization",layout="wide")

st.title("Data Manipulation and Visualization")

csv = st.file_uploader("Upload CSV: ")

if csv != None:
    df = pd.read_csv(csv)
    st.write(df.head())
    col1, col2 = st.columns(2)
    with col1:
        c = st.selectbox("Select column",options=df.columns)
    with col2:
        val = st.text_input("Valeur")
    sort_df = df[df[c].astype(str) == val]
    st.write(sort_df)
    st.subheader("Histogram")
    col3,col4 = st.columns(2)
    with col3:
        nc = st.slider("lignes",0,len(df),(0,100))
    with col4:
        x = st.selectbox("select x asis", options=df.columns)
    df_hist = df[x][nc[0]:nc[1]]
    plt.hist(df_hist)
    st.pyplot(plt)
    st.subheader("Chart")
    graph_name = st.selectbox("Graph type", ["ligne","barre","nuage de points"])
    col5,col6 = st.columns(2)
    with col5:
        x_axis = st.selectbox("select x asis", options=df.columns,key="789")
    with col6:
        y_axis = st.selectbox("select y asis", options=df.columns,key="779")
    
    fig, ax = plt.subplots()

    if graph_name == "ligne":
        ax.plot(x_axis, y_axis, data=df)
    if graph_name == "barre":
        ax.bar(x_axis, y_axis, data=df)
    if graph_name == "nuage de points":
        ax.scatter(x_axis, y_axis, data=df)

    ax.set(xlabel=x_axis, ylabel=y_axis)

    st.pyplot(fig)




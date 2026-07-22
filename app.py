import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import requests
st.set_page_config(page_title="Facebook Dashboard",layout="wide")

st.title("Facebook Dataset Interactive Dashboard")

# Load Dataset
df = pd.read_csv("dataset_Facebook.csv",sep=';')

# Sidebar
st.sidebar.header("Filters")

post_type = st.sidebar.selectbox(
    "Select Post Type",
    df["Type"].unique()
)

filtered = df[df["Type"]==post_type]

st.write("### Filtered Data")
st.dataframe(filtered)

###############################
# Chart 1
###############################

st.subheader("Average Likes")

likes = filtered.groupby("Category")["like"].mean()

fig,ax=plt.subplots()
likes.plot(kind="bar",ax=ax)
st.pyplot(fig)

###############################
# Chart 2
###############################

st.subheader("Comments Distribution")

fig,ax=plt.subplots()

ax.hist(filtered["comment"],bins=15)

st.pyplot(fig)

###############################
# Chart 3
###############################

st.subheader("Shares vs Likes")

fig,ax=plt.subplots()

ax.scatter(filtered["share"],filtered["like"])

ax.set_xlabel("Shares")
ax.set_ylabel("Likes")

st.pyplot(fig)

####################################
# LIVE API
####################################

st.subheader("Current Weather (London)")

url="https://api.open-meteo.com/v1/forecast?latitude=51.50&longitude=-0.12&current=temperature_2m"

response=requests.get(url)

weather=response.json()

temp=weather["current"]["temperature_2m"]

st.success(f"Current Temperature : {temp} °C")


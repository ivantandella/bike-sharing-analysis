import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
# sns.set(style='dark')

# Load data
def load_data():
    data = pd.read_csv("../Bike-sharing-dataset/hour.csv")
    return data

data = load_data()
data = pd.DataFrame(data)

# Set title
st.title("Bike Sharing Winter 2011")

# Sidebar
st.sidebar.title("Dashboard")
st.sidebar.markdown("Ivan Tandella")

# Filter data untuk tahun 2011 dan musim salju
winter_2011_df = data[(data["yr"] == 0) & (data["season"] == 4)]
total_rentals = winter_2011_df["cnt"].sum()

st.metric("Total Rental", value=total_rentals)

# Filter data untuk musim salju
winter_day_df = data[data["season"] == 4]

fig, ax = plt.subplots()
ax.bar(winter_day_df["weathersit"], winter_day_df["cnt"])
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda (Musim Salju)")
st.pyplot(fig)

# Filter data untuk pengguna biasa (casual) di musim salju
winter_casual_df = data[(data["season"] == 4) & (data["casual"] != 0)]

fig, ax = plt.subplots()
ax.bar(winter_casual_df["hr"], winter_casual_df["casual"])
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title('Pengaruh Jam terhadap Penyewaan Sepeda (Pengguna Biasa, Musim Salju)')
st.pyplot(fig)

fig, ax = plt.subplots()
ax.bar(winter_casual_df["weekday"], winter_casual_df["casual"])
ax.set_xlabel("Hari Kerja (0 = Minggu, 6 = Sabtu)")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Pengaruh Hari Kerja terhadap Penyewaan Sepeda (Pengguna Biasa, Musim Salju)")
st.pyplot(fig)
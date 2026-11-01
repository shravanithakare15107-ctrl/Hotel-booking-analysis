import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Hotel Booking Analysis Dashboard")
st.write("Analysis of hotel booking data using Python")

# Load dataset
df = pd.read_csv("hotel_bookings.csv")

# Sidebar filter
st.sidebar.header("Filters")

hotel_type = st.sidebar.selectbox(
    "Select Hotel Type",
    ["All"] + list(df["hotel"].unique())
)

if hotel_type != "All":
    df = df[df["hotel"] == hotel_type]

# Display total bookings
st.subheader("Booking Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Bookings", len(df))

col2.metric(
    "Cancelled Bookings",
    int(df["is_canceled"].sum())
)

cancellation_rate = (
    df["is_canceled"].mean() * 100
    if len(df) > 0 else 0
)

col3.metric(
    "Cancellation Rate",
    f"{cancellation_rate:.2f}%"
)

# Hotel booking chart
st.subheader("Hotel Type Analysis")

hotel_counts = df["hotel"].value_counts()

fig, ax = plt.subplots()
hotel_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Hotel Type")
ax.set_ylabel("Number of Bookings")
st.pyplot(fig)

# Monthly booking analysis
st.subheader("Monthly Booking Analysis")

monthly_data = df["arrival_date_month"].value_counts()

fig, ax = plt.subplots()
monthly_data.plot(kind="bar", ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("Bookings")
plt.xticks(rotation=45)
st.pyplot(fig)

# Market segment analysis
st.subheader("Market Segment Analysis")

segment_data = df["market_segment"].value_counts()

fig, ax = plt.subplots()
segment_data.plot(kind="bar", ax=ax)
ax.set_xlabel("Market Segment")
ax.set_ylabel("Bookings")
plt.xticks(rotation=45)
st.pyplot(fig)

# Dataset display
st.subheader("Hotel Booking Dataset")
st.dataframe(df)

# Download button
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Dataset",
    data=csv,
    file_name="hotel_bookings.csv",
    mime="text/csv"
)

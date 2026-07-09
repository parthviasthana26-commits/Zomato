import streamlit as st
import pandas as pd

# Page Title
st.set_page_config(page_title="Zomato Restaurant Explorer", page_icon="🍽️")

# Load Dataset
df = pd.read_csv("zomato.csv")

# Heading
st.title("🍽️ Zomato Restaurant Explorer")
st.write("Search your favourite restaurant")

# Restaurant Dropdown
restaurant = st.selectbox(
    "Select Restaurant",
    sorted(df["name"].unique())
)

# Selected Restaurant Data
result = df[df["name"] == restaurant].iloc[0]

# Show Details
st.subheader("Restaurant Details")

st.write("⭐ **Restaurant Name:**", result["name"])

if "rate" in df.columns:
    st.write("⭐ **Rating:**", result["rate"])

if "votes" in df.columns:
    st.write("👍 **Votes:**", result["votes"])

if "Cost2plates" in df.columns:
    st.write("💰 **Cost for 2 People:**", result["Cost2plates"])

if "Type" in df.columns:
    st.write("🍴 **Restaurant Type:**", result["Type"])

if "online_order" in df.columns:
    st.write("🛵 **Online Order:**", result["online_order"])

if "book_table" in df.columns:
    st.write("📅 **Table Booking:**", result["book_table"])

if "address" in df.columns:
    st.write("📍 **Address:**", result["address"])

if "url" in df.columns:
    st.markdown(f"🔗 [Open on Zomato]({result['url']})")
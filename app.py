import streamlit as st
import pandas as pd
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Fashion Designer",
    page_icon="🤵👗",
    layout="centered"
)

# ---------------- DATA ----------------
occasions = ["Wedding", "Party", "Casual", "Office"]
seasons = ["Summer", "Winter"]

male_outfits = {
    "Wedding": ["Sherwani", "Suit"],
    "Party": ["Blazer", "Kurta Set"],
    "Casual": ["Jeans & T-shirt"],
    "Office": ["Formal Shirt & Pants", "Blazer"]
}

female_outfits = {
    "Wedding": ["Lehenga", "Saree"],
    "Party": ["Dress", "Kurti Set"],
    "Casual": ["Top & Jeans", "Kurti"],
    "Office": ["Office Saree", "Formal Dress"]
}

fabrics = {
    "Summer": ["Cotton", "Linen"],
    "Winter": ["Wool", "Velvet"]
}

color_combinations = {
    "Black": ["White", "Beige"],
    "White": ["Blue", "Pastel"],
    "Blue": ["White", "Beige"],
    "Red": ["Black", "White"],
    "Pastel": ["White", "Beige"],
    "Beige": ["White", "Brown"]
}

colors = list(color_combinations.keys())

# ---------------- FUNCTIONS ----------------
def outfit_description(outfit, occasion, season):
    return (
        f"A stylish **{outfit}** designed for **{occasion.lower()} occasions**, "
        f"crafted to keep you comfortable and elegant during **{season.lower()}**."
    )

def fashion_trend(age):
    if age == "Teen":
        return "Bright colors and trendy silhouettes are popular among teens."
    elif age == "Adult":
        return "Minimal designs with balanced colors are trending."
    else:
        return "Elegant, comfortable, and timeless styles are preferred."

def sustainability_score(fabric):
    if fabric in ["Cotton", "Linen"]:
        return "⭐⭐⭐⭐⭐ Excellent eco-friendly choice"
    else:
        return "⭐⭐⭐ Moderate sustainability (warm & durable)"

# ---------------- SIDEBAR ----------------
st.sidebar.title("👤 User Preferences")
gender = st.sidebar.radio("Choose Gender", ["Male", "Female"])

# ---------------- MAIN UI ----------------
st.title("👗 AI Fashion Designer")
st.write("Smart outfit recommendations based on fashion logic and sustainability 🌱")

occasion = st.selectbox("Select Occasion", occasions)
season = st.selectbox("Select Season", seasons)
age_group = st.selectbox("Select Age Group", ["Teen", "Adult", "Senior"])

if st.button("✨ Get Outfit Recommendation"):
    outfit_pool = male_outfits if gender == "Male" else female_outfits

    outfit = random.choice(outfit_pool[occasion])
    fabric = random.choice(fabrics[season])
    color = random.choice(colors)

    st.success("👕 Recommended Outfit")
    st.markdown(f"**Outfit:** {outfit}")
    st.markdown(f"**Fabric:** {fabric}")
    st.markdown(f"**Primary Color:** {color}")

    # Description
    st.info("📝 Outfit Description")
    st.write(outfit_description(outfit, occasion, season))

    # Color Combinations
    st.info("🎨 Best Color Combinations")
    for c in color_combinations[color]:
        st.write(f"• {c}")

    # Fashion Trend
    st.warning("🔥 Fashion Trend Tip")
    st.write(fashion_trend(age_group))

    # Sustainability
    st.success("🌱 Sustainability Score")
    st.write(sustainability_score(fabric))
    st.write("✔ Prefer natural fabrics")
    st.write("✔ Avoid fast fashion")
    st.write("✔ Reuse & recycle clothing")

import streamlit as st
import pandas as pd
import random

# ---------------- DATASET ----------------
occasions = ["Wedding", "Party", "Casual", "Office"]
seasons = ["Summer", "Winter"]
genders = ["Male", "Female"]

outfits = {
    "Wedding": ["Sherwani", "Lehenga", "Saree", "Suit"],
    "Party": ["Dress", "Kurta Set", "Blazer"],
    "Casual": ["Jeans & T-shirt", "Kurti", "Top & Jeans"],
    "Office": ["Formal Shirt & Pants", "Blazer", "Office Saree"]
}

fabrics = {
    "Summer": ["Cotton", "Linen"],
    "Winter": ["Wool", "Velvet"]
}

colors = ["Black", "White", "Blue", "Red", "Pastel", "Beige"]

data = []
for _ in range(300):
    data.append([
        random.choice(occasions),
        random.choice(seasons),
        random.choice(genders),
        random.choice(outfits[random.choice(occasions)]),
        random.choice(fabrics[random.choice(seasons)]),
        random.choice(colors)
    ])

df = pd.DataFrame(data, columns=[
    "Occasion", "Season", "Gender",
    "Outfit", "Fabric", "Color"
])

# ---------------- EXTRA FEATURES ----------------
color_combinations = {
    "Black": ["White", "Red", "Beige"],
    "White": ["Blue", "Pastel", "Black"],
    "Blue": ["White", "Beige"],
    "Red": ["Black", "White"],
    "Pastel": ["White", "Beige"],
    "Beige": ["Brown", "White"]
}

def fashion_trends(age):
    if age == "Teen":
        return "Trendy outfits with bright colors are popular."
    elif age == "Adult":
        return "Minimal designs and neutral shades are trending."
    else:
        return "Comfortable and elegant styles are recommended."

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="AI Fashion Designer", layout="centered")

st.title("👗 AI Fashion Designer")
st.write("An AI-based system that recommends outfits based on user preferences.")

occasion = st.selectbox("Select Occasion", occasions)
season = st.selectbox("Select Season", seasons)
gender = st.selectbox("Select Gender", genders)
age_group = st.selectbox("Select Age Group", ["Teen", "Adult", "Senior"])

if st.button("Get Outfit Recommendation"):
    result = df[
        (df["Occasion"] == occasion) &
        (df["Season"] == season) &
        (df["Gender"] == gender)
    ].sample(1).iloc[0]

    st.success("👕 Outfit Recommendation")
    st.write("**Outfit:**", result["Outfit"])
    st.write("**Fabric:**", result["Fabric"])
    st.write("**Color:**", result["Color"])

    st.info("🎨 Color Combinations")
    st.write(color_combinations.get(result["Color"], "No suggestions available"))

    st.warning("🔥 Fashion Trend Tip")
    st.write(fashion_trends(age_group))

    st.success("🌱 Sustainable Fashion Tips")
    st.write("- Prefer cotton and linen fabrics")
    st.write("- Reuse and recycle clothes")
    st.write("- Avoid fast fashion")

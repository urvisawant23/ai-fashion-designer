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
    occ = random.choice(occasions)
    sea = random.choice(seasons)
    data.append([
        occ,
        sea,
        random.choice(genders),
        random.choice(outfits[occ]),
        random.choice(fabrics[sea]),
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
        return "Trendy outfits with vibrant colors and modern styles are popular."
    elif age == "Adult":
        return "Minimal designs with neutral and elegant shades are trending."
    else:
        return "Comfortable, classy, and easy-to-wear outfits are recommended."

def sustainable_tips(season):
    if season == "Summer":
        return [
            "Prefer breathable fabrics like cotton and linen",
            "Choose light colors to reduce heat absorption",
            "Avoid excessive synthetic materials"
        ]
    else:
        return [
            "Opt for wool and layered clothing",
            "Reuse winter wear across seasons",
            "Choose durable fabrics to reduce waste"
        ]

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
    combos = color_combinations.get(result["Color"], [])
    if combos:
        st.write(", ".join(combos))
    else:
        st.write("No suggestions available")

    st.warning("🔥 Fashion Trend Tip")
    st.write(fashion_trends(age_group))

    st.success("🌱 Sustainable Fashion Tips")
    for tip in sustainable_tips(season):
        st.write(f"- {tip}")

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# ---------------------
# 1. Load Data
# ---------------------
file_id = "1Al6xinS2lCk5zPIS4jt4lusZD4ml8_V0"
url = f"https://drive.google.com/uc?export=download&id={file_id}"


df = pd.read_csv(url)

# ---------------------
# 2. Feature Engineering
# ---------------------
# Map age to age_group (integer)
def age_group(age):
    if age <= 19:
        return 0  # Teen
    elif age <= 49:
        return 1  # Adult
    else:
        return 2  # Senior

df['age_group'] = df['age'].apply(age_group)

# Effort score
df['effort_score'] = df['heart_rate_avg'] * df['duration_min']

# Features & target
X = df.drop(columns=['calories_burned'])
y = df['calories_burned']

# Scaling numeric features
numerical_cols = ['age','duration_min','heart_rate_avg','steps','sleep_hours','weight_kg','effort_score']
scaler = StandardScaler()
X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

# Train Linear Regression
lr_model = LinearRegression()
lr_model.fit(X, y)

# ---------------------
# 3. Streamlit UI
# ---------------------
st.title("💪 Fitness Calories Predictor")

st.sidebar.header("Input Your Activity Details")

# User inputs
age_input = st.sidebar.number_input("Age", min_value=10, max_value=90, value=25)
gender_input = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
activity_input = st.sidebar.selectbox("Activity Type", ["Cycling", "Strength Training", "Swimming", "Yoga", "HIIT", "Walking", "Running"])
duration_input = st.sidebar.number_input("Duration (minutes)", min_value=1, max_value=300, value=30)
heart_rate_input = st.sidebar.number_input("Average Heart Rate", min_value=60, max_value=200, value=120)
steps_input = st.sidebar.number_input("Steps", min_value=0, max_value=50000, value=5000)
sleep_input = st.sidebar.number_input("Sleep Hours", min_value=0.0, max_value=12.0, value=7.0)
weight_input = st.sidebar.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)

# Map gender and activity_type to integers (matching model training)
gender_map_manual = {"Male": 0, "Female": 1, "Other": 2}
activity_map_manual = {
    "Cycling": 0,
    "Strength Training": 1,
    "Swimming": 2,
    "Yoga": 3,
    "HIIT": 4,
    "Walking": 5,
    "Running": 6
}

gender_int = gender_map_manual[gender_input]
activity_int = activity_map_manual[activity_input]
age_group_int = age_group(age_input)
effort_score_input = duration_input * heart_rate_input

# Build input DataFrame
input_df = pd.DataFrame({
    'age':[age_input],
    'gender':[gender_int],
    'activity_type':[activity_int],
    'duration_min':[duration_input],
    'heart_rate_avg':[heart_rate_input],
    'steps':[steps_input],
    'sleep_hours':[sleep_input],
    'weight_kg':[weight_input],
    'age_group':[age_group_int],
    'effort_score':[effort_score_input]
})

# Scale numeric features
input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

# Predict calories
predicted_calories = lr_model.predict(input_df)[0]
st.subheader("Predicted Calories Burned")
st.write(f"🔥 {predicted_calories:.2f} calories")

# ---------------------
# 4. EDA Plot
# ---------------------
st.subheader("Average Calories by Activity Type")
avg_calories = df.groupby('activity_type')['calories_burned'].mean().sort_values()
fig, ax = plt.subplots(figsize=(8,4))
bars = ax.bar(avg_calories.index, avg_calories.values, color='lightcoral', edgecolor='black')
ax.set_xlabel("Activity Type")
ax.set_ylabel("Average Calories Burned")
ax.set_xticklabels(avg_calories.index, rotation=45)

# Add labels
for bar, value in zip(bars, avg_calories.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, f'{value:.0f}', ha='center', va='bottom')

st.pyplot(fig)

# ---------------------
# 5. Guide for Users
# ---------------------
st.subheader("📝 Activity Type Reference")
st.write("""
0: Cycling  
1: Strength Training  
2: Swimming  
3: Yoga  
4: HIIT  
5: Walking  
6: Running
""")

st.subheader("📝 Gender Reference")
st.write("""
0: Male  
1: Female  
2: Other
""")

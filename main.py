import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('/Users/mariolaczajkowska/happiness_data/new_data/happiness_cleaned.csv')
df['Year'] = df['Year'].astype(int)

st.sidebar.header("Filters")
selected_country = st.sidebar.multiselect("Select Country:", options=df['Country'].unique(), default=df['Country'].unique())
selected_year = st.sidebar.multiselect("Select Year:", options=sorted(df['Year'].unique()), default=df['Year'].unique())

# Apply filters
filtered_df = df[df['Country'].isin(selected_country) & df['Year'].isin(selected_year)]

# Display data
st.title("World Happiness Data")
st.write("Filtered Data", filtered_df)
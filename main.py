import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('/Users/mariolaczajkowska/happiness_data/new_data/happiness_cleaned.csv', sep = ';')
df['Year'] = df['Year'].astype(int)

st.sidebar.header("Filters")
selected_country = st.sidebar.multiselect("Select Country:", options=df['Country'].unique(), default=df['Country'].unique())
selected_year = st.sidebar.multiselect("Select Year:", options=sorted(df['Year'].unique()), default=df['Year'].unique())

# Apply filters
filtered_df = df[df['Country'].isin(selected_country) & df['Year'].isin(selected_year)]

tab1, tab2 = st.tabs(["Filtered Data", "Charts"])

# Tab 1 – Data Table
with tab1:
    st.write("Filtered Data", filtered_df)

with tab2:
    st.title("Charts")

    if 'Score' in filtered_df.columns:
        #av score by country 
        avg_scores = filtered_df.groupby("Country")["Score"].mean().reset_index()
        fig_bar = px.bar(avg_scores, x="Country", y="Score", 
                         title="Average happiness score by country",
                         labels={"Score": "Average Score"})
        st.plotly_chart(fig_bar)
    else:
        st.warning("No 'Score' column found in the dataset.")

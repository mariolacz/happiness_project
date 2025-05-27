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
    if 'Score' in filtered_df.columns:
        #av score by country 
        avg_scores = filtered_df.groupby("Country")["Score"].mean().reset_index()
        fig_bar = px.bar(avg_scores, x="Country", y="Score", 
                         title="Average happiness score by country",
                         labels={"Score": "Average Score"})
        st.plotly_chart(fig_bar)
    else:
        st.warning("No 'Score' column found in the dataset.")

    if len(selected_year) == 1:
        year_df = filtered_df[filtered_df['Year'] == selected_year[0]]
        top_10 = year_df.sort_values(by="Score", ascending=False).head(10)
        fig_bar = px.bar(top_10, 
                        x="Score", 
                        y="Country", 
                        orientation="h", 
                        title=f"Top 10 happiest countries in {selected_year[0]}")
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("Select a single year to view top 10 countries.")

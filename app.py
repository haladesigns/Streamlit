import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
import scipy as sp


st.header('Car Ads')
st.write('Car Ads application. Placeholder.')


# Load the dataset
file_path = '../vehicles_us.csv'
df = pd.read_csv(file_path)

# Calculating percentage of missing values for each column
missing_values = df.isnull().sum()
missing_percentage = ((missing_values / len(df)) * 100).round(2)

# Creating a DataFrame for the raw markdown table
missing_values_df = pd.DataFrame({
    'Column': missing_values.index,
    'Missing Values': missing_values.values,
    'Percentage of Total (%)': missing_percentage.values
})

# Fill missing values
df['model_year'] = df['model_year'].fillna(df['model_year'].median())
df['cylinders'] = df['cylinders'].fillna(df['cylinders'].mode()[0])
df['odometer'] = df['odometer'].fillna(df['odometer'].median())
df['paint_color'] = df['paint_color'].fillna('unknown')

# Drop the 'is_4wd' column
df = df.drop(columns=['is_4wd'])

fig_hist = px.histogram(df, x='price', nbins=30, title='Distribution of Vehicle Prices')
#fig_hist.show()


st.write(fig_hist)
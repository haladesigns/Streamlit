import pandas as pd
import streamlit as st
import random
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
import scipy as sp


st.header('Car Ads')
st.write('Introductory text here')

# Load the dataset
file_path = './vehicles_us.csv'
df = pd.read_csv(file_path)

# Fill missing values
df['model_year'] = df['model_year'].fillna(df['model_year'].median())
df['cylinders'] = df['cylinders'].fillna(df['cylinders'].mode()[0])
df['odometer'] = df['odometer'].fillna(df['odometer'].median())
df['paint_color'] = df['paint_color'].fillna('unknown')

# Drop the 'is_4wd' column
df = df.drop(columns=['is_4wd'])

#--------------------SETTINGS-----------------
# Choose a template
templates = ["plotly", "ggplot2", "seaborn", "simple_white", "none"]

st.sidebar.header("Settings")
my_template = st.sidebar.radio("Choose a template", templates, key="template")
text_auto= st.sidebar.checkbox("Enable text")


#---------------------PLOTS-------------------
expand_all = False
expand = st.sidebar.button("Expand All", key="expandall")
minimize = st.sidebar.button("Minimize")

# Initialize session state
if 'expand_all' not in st.session_state:
    st.session_state.expand_all = False

if expand: 
    st.session_state.expand_all = True
elif minimize:
    st.session_state.expand_all = False

# Histogram - Distribution of Vehicle Prices
fig_hist_price = px.histogram(df, x='price', nbins=30, color='condition', text_auto=text_auto, template=my_template)
fig_hist_price.update_traces(textposition='outside')
fig_hist_price.update_layout(title_text='Distribution of Vehicle Prices', title_x=0.35)
#st.write(fig_hist_price)
my_histprice_expander = st.expander("Expand Distribution of Vehicle Prices", expanded=True)
with my_histprice_expander:
    st.write(fig_hist_price)

# Histogram of Odometer Readings: To visualize the distribution of odometer readings across the dataset.
fig_hist_odometer = px.histogram(df, x='odometer', nbins=30, color='condition', text_auto=text_auto, template=my_template)
fig_hist_odometer.update_layout(title_text='Distribution of Odometer Readings', title_x=0.35)
#st.write(fig_hist_odometer)
my_histodom_expander = st.expander("Expand Distribution of Odometer Readings", expanded=st.session_state.expand_all)
with my_histodom_expander:
    st.write(fig_hist_odometer)

# Histogram of Days Listed: To understand how long vehicles are typically listed for sale.
fig_hist_days_listed = px.histogram(df, x='days_listed', nbins=30, title='Distribution of Days Listed', color='condition', 
                                    text_auto=text_auto, template=my_template,)
fig_hist_days_listed.update_layout(title_text='Distribution of Vehicle Conditions', title_x=0.35)
#st.write(fig_hist_days_listed)
my_histdayslisted_expander = st.expander("Expand Distribution of Vehicle Conditions", expanded=st.session_state.expand_all)
with my_histdayslisted_expander:
    st.write(fig_hist_days_listed)

# Histogram of Vehicle Conditions: To understand the distribution of different vehicle conditions (categorical histogram).
fig_hist_condition = px.histogram(df, x='condition', color='condition', text_auto=text_auto, template=my_template, )
fig_hist_condition.update_layout(title_text='Distribution of Vehicle Conditions', title_x=0.35)
#st.write(fig_hist_condition)
my_histcondition_expander = st.expander("Expand Distribution of Vehicle Conditions" if not st.session_state.expand_all else "", expanded=st.session_state.expand_all)
with my_histcondition_expander:
    st.write(fig_hist_condition)


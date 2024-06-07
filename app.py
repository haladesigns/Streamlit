import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go


st.header('Car Sales Advertisements')

# Load the dataset  
file_path = './vehicles_us.csv'
df = pd.read_csv(file_path)

#--------------------EDA-----------------
# Fill missing values
df['model_year'] = df['model_year'].fillna(df['model_year'].median())
df['cylinders'] = df['cylinders'].fillna(df['cylinders'].mode()[0])
df['odometer'] = df['odometer'].fillna(df['odometer'].median())
df['paint_color'] = df['paint_color'].fillna('unknown')

# Drop the 'is_4wd' column
df = df.drop(columns=['is_4wd'])

#-------------------SIDEBAR------------------
# Choose a template
templates = ["plotly", "ggplot2", "seaborn", "simple_white", "none"]

st.sidebar.header("Settings")
my_template = st.sidebar.radio("Choose a template", templates, key="template")
text_auto= st.sidebar.checkbox("Enable Histogram text")

#-----------------NAVIGATION MENU-------------
selected = option_menu(None, ["Plots", "Correlations", "Contact", ], 
                       icons=['bar-chart', 'arrows-collapse', 'mailbox', ], 
                       menu_icon="cast", default_index=0, orientation="horizontal")

#---------------------PLOTS-------------------
expand_all = st.sidebar.button("Expand All", key="expandall")
minimize = st.sidebar.button("Minimize")

expanders = [
    'expand_price', 'expand_odometer', 'expand_days_listed',
    'expand_condition', 'expand_scatter_price_odom',
    'expand_scatter_price_cylinders'
]

# Initialize session state for each expander
for expander in expanders:
    if expander not in st.session_state: st.session_state[expander] = False

# Set expand_all state based on button clicks
if expand_all:
    for expander in expanders: st.session_state[expander] = True
if minimize:
    for expander in expanders: st.session_state[expander] = False

# func to handle the state of the expanders
def create_expander(label, state_key, content_func):
    expander = st.expander(label, expanded=st.session_state[state_key],)
    with expander:
        content_func()
    return expander

# Histogram factory
def create_histogram(df, x, title):
    fig = px.histogram(df, x=x, nbins=30, color='condition', text_auto=text_auto, template=my_template)
    fig.update_traces(textposition='outside')
    fig.update_layout(title_text=title, title_x=0.35)
    st.write(fig)
    
# Scatter plot factory
def create_scatter_plot(df, x, y, title):
    fig = px.scatter(df, x=x, y=y, title=title, opacity=0.5, color='condition', template=my_template)
    fig.update_layout(title_text=title, title_x=0.35)
    st.write(fig)

# Create histogram functions
def content_hist_price(): 
    """Histogram - Distribution of Vehicle Prices"""
    create_histogram(df, 'price', 'Distribution of Vehicle Prices')

def content_hist_odometer(): 
    """Histogram of Odometer Readings: Visualize the distribution of odometer readings across the dataset."""
    create_histogram(df, 'odometer', 'Distribution of Odometer Readings')

def content_hist_days_listed(): 
    """Histogram of Days Listed: Understand how long vehicles are typically listed for sale."""
    create_histogram(df, 'days_listed', 'Distribution of Days Listed')

def content_hist_condition(): 
    """ Histogram of Vehicle Conditions: Understand the distribution of different vehicle conditions (categorical histogram)."""
    create_histogram(df, 'condition', 'Distribution of Vehicle Conditions')

# Create scatter plot functions
def content_scatter_price_odom(): 
    """Scatter plot of price vs. Odometer Reading"""
    create_scatter_plot(df, 'odometer', 'price', 'Price vs. Odometer Reading')

def content_scatter_price_cylinders(): 
    """Scatter plot of price vs. cylinder count"""
    create_scatter_plot(df, 'cylinders', 'price', 'Price vs. Cylinder Count')

# Create expanders
create_expander("Distribution of Vehicle Prices (Histogram)", 'expand_price', content_hist_price)
create_expander("Distribution of Odometer Readings (Histogram)", 'expand_odometer', content_hist_odometer)
create_expander("Days Listed (Histogram)", 'expand_days_listed', content_hist_days_listed)
create_expander("Distribution of Vehicle Conditions (Histogram)", 'expand_condition', content_hist_condition)
create_expander("Price vs. Odometer Reading (Scatter)", 'expand_scatter_price_odom', content_scatter_price_odom)
create_expander("Price vs. Cylinder Count (Scatter)", 'expand_scatter_price_cylinders', content_scatter_price_cylinders)

import streamlit as st

# Title of the app
st.title('Urban Roof Drd Generator')

# Input fields
roof_type = st.selectbox('Select Roof Type:', ['Flat', 'Pitched'])

if roof_type == 'Flat':
    st.write('You selected a Flat roof. Please provide the dimensions.')
    length = st.number_input('Length (m):')
    width = st.number_input('Width (m):')
    # Add more inputs as required for Flat roof

elif roof_type == 'Pitched':
    st.write('You selected a Pitched roof. Please provide the dimensions.')
    length = st.number_input('Length (m):')
    height = st.number_input('Height (m):')
    # Add more inputs as required for Pitched roof

# Add calculation logic and results display based on inputs

# Run the application
if st.button('Generate'): 
    st.success('Generating DRD for selected roof type...')

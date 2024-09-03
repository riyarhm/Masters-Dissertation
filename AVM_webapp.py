#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import boto3
from io import BytesIO


# In[ ]:


# Load the dataset
@st.cache_data
def load_data():
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Replace with your bucket name and file key
    bucket_name = 'avmproject'
    file_key = 'final.csv'
    
    # Download the file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    
    # Load the CSV file into a DataFrame
    data_pd = pd.read_csv(BytesIO(response['Body'].read()))
    
    # Strip leading/trailing whitespaces and convert to upper case for consistency
    data_pd['postcode'] = data_pd['postcode'].str.strip().str.upper()
    data_pd['epc_address'] = data_pd['epc_address'].str.strip().str.upper()
    
    return data_pd



# In[ ]:


# Function to filter addresses by postcode
def get_addresses_by_postcode(data, postcode):
    postcode = postcode.strip().upper()  # Normalize the input postcode
    filtered_data = data[data['postcode'] == postcode]
    return filtered_data['epc_address'].unique(), filtered_data


# In[ ]:


# Main function to build the Streamlit app
def main():
    st.title("Automated Valuation Model (AVM) Web App")

    data = load_data()

    

    # Input postcode
    postcode = st.text_input("Enter the postcode:")

    if postcode:
        addresses, filtered_data = get_addresses_by_postcode(data, postcode)
        
        if len(addresses) > 0:
            epc_address = st.selectbox("Select your address", ["Select your address"] + list(addresses))
            if epc_address and epc_address != "Select your address":
                property_data = filtered_data[filtered_data['epc_address'] == epc_address]

                if not property_data.empty:
                    property_data = property_data.iloc[0]

                    # Display the results
                    st.subheader("Predicted Property Price")
                    st.write(f"£{property_data['prediction']:,.2f}")

                    st.subheader("Property Details")
                    st.write(f"Number of Rooms: {property_data['number_habitable_rooms']}")
                    st.write(f"Total Floor Area: {property_data['total_floor_area']} sqm")
                    st.write(f"Energy Rating: {property_data['current_energy_rating']}")
                    st.write(f"Tenure: {property_data['tenure']}")
                    st.write(f"Property Type: {property_data['property_type']}")
                    st.write(f"Build Form: {property_data['build_form']}")
                    st.write(f"Last Sold Date: {property_data['date_of_transfer']}")
                    st.write(f"Last Sold Price: {property_data['price']}")
                    st.write(f"Solar Panel: {property_data['is_solar_panel']}")

                    # Display the map
                    st.subheader("Property Location")
                    m = folium.Map(location=[property_data['lat'], property_data['lon']], zoom_start=16)
                    folium.Marker([property_data['lat'], property_data['lon']],
                                  popup=f"{epc_address}").add_to(m)
                    st_folium(m, width=700, height=500)
                else:
                    st.warning("Selected address not found in the data.")
        else:
            st.warning("No addresses found for the given postcode.")
    else:
        st.info("Please enter a postcode.")

if __name__ == "__main__":
    main()


import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(page_title="Flight Booking: HYD to GOI", page_icon="✈️", layout="wide")

# --- Data Setup ---
def get_flight_data():
    # Hyderabad to Goa
    outbound_data = {
        'Airline': ['IndiGo', 'SpiceJet', 'Air India', 'Vistara', 'Akasa Air'],
        'Flight No': ['6E-532', 'SG-102', 'AI-884', 'UK-992', 'QP-114'],
        'Departure': ['06:00 AM', '09:30 AM', '01:15 PM', '05:45 PM', '09:00 PM'],
        'Duration': ['1h 15m', '1h 20m', '1h 10m', '1h 25m', '1h 15m'],
        'Price': [4500, 4200, 5100, 6500, 3900]
    }
    
    # Goa to Hyderabad
    return_data = {
        'Airline': ['IndiGo', 'SpiceJet', 'Air India', 'Vistara', 'Akasa Air'],
        'Flight No': ['6E-539', 'SG-109', 'AI-889', 'UK-995', 'QP-119'],
        'Departure': ['08:00 AM', '11:30 AM', '03:15 PM', '07:45 PM', '10:30 PM'],
        'Duration': ['1h 15m', '1h 20m', '1h 10m', '1h 25m', '1h 15m'],
        'Price': [4800, 4300, 5200, 6700, 4100]
    }
    
    return pd.DataFrame(outbound_data), pd.DataFrame(return_data)

df_outbound, df_return = get_flight_data()

# --- UI Layout ---
st.title("✈️ Flight Booking: Hyderabad (HYD) ↔ Goa (GOI)")
st.markdown("Select your travel dates and flights to book your tickets instantly.")

# Sidebar for Dates
st.sidebar.header("🗓️ Travel Dates")
dept_date = st.sidebar.date_input("Departure Date", datetime.now() + timedelta(days=1))
return_date = st.sidebar.date_input("Return Date", datetime.now() + timedelta(days=4))

if return_date < dept_date:
    st.sidebar.error("Return date cannot be before departure date.")

# Main Content
col1, col2 = st.columns(2)

# Outbound Flights
with col1:
    st.subheader(f"🛫 HYD → GOI ({dept_date})")
    st.markdown("Select your outbound flight:")
    
    # Display as a table for reference
    st.dataframe(df_outbound[['Airline', 'Departure', 'Duration', 'Price']], hide_index=True, use_container_width=True)
    
    # Selection
    outbound_options = [f"{row['Airline']} ({row['Departure']}) - ₹{row['Price']}" for index, row in df_outbound.iterrows()]
    selected_outbound_str = st.radio("Choose Outbound Flight:", outbound_options, key="outbound")
    
    # Parse selection
    selected_outbound_idx = outbound_options.index(selected_outbound_str)
    selected_outbound_flight = df_outbound.iloc[selected_outbound_idx]

# Return Flights
with col2:
    st.subheader(f"🛬 GOI → HYD ({return_date})")
    st.markdown("Select your return flight:")
    
    # Display as a table for reference
    st.dataframe(df_return[['Airline', 'Departure', 'Duration', 'Price']], hide_index=True, use_container_width=True)
    
    # Selection
    return_options = [f"{row['Airline']} ({row['Departure']}) - ₹{row['Price']}" for index, row in df_return.iterrows()]
    selected_return_str = st.radio("Choose Return Flight:", return_options, key="return")
    
    # Parse selection
    selected_return_idx = return_options.index(selected_return_str)
    selected_return_flight = df_return.iloc[selected_return_idx]

# Total Price Calculation
total_price = selected_outbound_flight['Price'] + selected_return_flight['Price']

st.divider()

# Booking Section
st.subheader("💰 Booking Summary")
st.write(f"**Total Fare:** ₹{total_price}")

if st.button("Book Ticket 🎟️", type="primary"):
    if return_date < dept_date:
        st.error("Please correct the dates before booking.")
    else:
        st.success("🎉 Booking Confirmed! Have a safe trip.")
        
        # Summary Card
        with st.container():
            st.markdown("---")
            c1, c2 = st.columns(2)
            
            with c1:
                st.markdown("### 🛫 Outbound")
                st.write(f"**Date:** {dept_date}")
                st.write(f"**Airline:** {selected_outbound_flight['Airline']}")
                st.write(f"**Flight:** {selected_outbound_flight['Flight No']}")
                st.write(f"**Time:** {selected_outbound_flight['Departure']}")
                st.write(f"**Price:** ₹{selected_outbound_flight['Price']}")
            
            with c2:
                st.markdown("### 🛬 Return")
                st.write(f"**Date:** {return_date}")
                st.write(f"**Airline:** {selected_return_flight['Airline']}")
                st.write(f"**Flight:** {selected_return_flight['Flight No']}")
                st.write(f"**Time:** {selected_return_flight['Departure']}")
                st.write(f"**Price:** ₹{selected_return_flight['Price']}")
            
            st.markdown("---")
            st.markdown(f"### **Grand Total: ₹{total_price}**")

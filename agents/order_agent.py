import streamlit as st
import pandas as pd
from agents.email_agent import send_confirmation_email
import os
from datetime import datetime, timedelta

ORDER_FILE = os.path.abspath("orders.csv")

def handle_order():
    st.header("🛒 Place an Order")
    with st.form("order_form"):
        name = st.text_input("Your Name")
        item = st.text_input("Item to Order")
        quantity = st.number_input("Quantity", min_value=1)
        email = st.text_input("Your Email")
        submit = st.form_submit_button("Place Order")

        if submit:
            price_per_unit = 100  # Dummy price
            total_price = quantity * price_per_unit
            booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            estimated_delivery = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")

            order_data = {
                "Name": name,
                "Item": item,
                "Quantity": quantity,
                "PricePerUnit": price_per_unit,
                "TotalPrice": total_price,
                "BookingDate": booking_date,
                "EstimatedDelivery": estimated_delivery,
                "Email": email
            }

            if os.path.exists(ORDER_FILE):
                df = pd.read_csv(ORDER_FILE)
                df = pd.concat([df, pd.DataFrame([order_data])], ignore_index=True)
            else:
                df = pd.DataFrame([order_data])

            df.to_csv(ORDER_FILE, index=False)

            order_summary = f"Order placed by {name} for {quantity} x {item}."
            st.success(order_summary)
            send_confirmation_email(name, item, quantity, email)
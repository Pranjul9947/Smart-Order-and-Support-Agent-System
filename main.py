import streamlit as st
from agents.order_agent import handle_order
from agents.chatbot_agent import handle_chat
from agents.feedback_agent import handle_feedback
from agents.analysis_agent import analyze_feedback 

st.set_page_config(page_title="Smart Order & Support Bot", layout="centered")

st.title("🤖 Smart Order & Support System")

# ✅ Sidebar Menu
choice = st.sidebar.radio("Select Task", [
    "Place Order",
    "Customer Support Chat",
    "Leave Feedback",
    "Sentiment Dashboard"  
])

# ✅ Route each selection to its agent
if choice == "Place Order":
    handle_order()
elif choice == "Customer Support Chat":
    handle_chat()
elif choice == "Leave Feedback":
    handle_feedback()
elif choice == "Sentiment Dashboard":
    analyze_feedback()  

import pandas as pd
import os

# Define paths
ORDER_FILE = "data/orders.csv"
FEEDBACK_FILE = "data/feedback.csv"

def reset_csv(file_path, headers):
    df = pd.DataFrame(columns=headers)
    df.to_csv(file_path, index=False)

# UI Reset Button
if st.sidebar.button("🔁 Reset All Data"):
    reset_csv(ORDER_FILE, ["name", "item", "quantity", "price", "booking_date", "delivery_date"])
    reset_csv(FEEDBACK_FILE, ["rating", "feedback", "sentiment"])
    st.sidebar.success("✅ All data has been reset (headers preserved).")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

FEEDBACK_FILE = os.path.abspath("feedback.csv")

def analyze_feedback():
    st.header("📊 Customer Sentiment Dashboard")

    if not os.path.exists(FEEDBACK_FILE):
        st.warning("No feedback file found.")
        return

    # Read the feedback.csv using pandas
    try:
        df = pd.read_csv(FEEDBACK_FILE)

        if df.empty:
            st.info("No feedback entries yet.")
            return

        # Clean + Summary Stats
        st.subheader("📋 Summary")
        total = len(df)
        positive = (df['Sentiment'].str.lower() == "positive").sum()
        neutral = (df['Sentiment'].str.lower() == "neutral").sum()
        negative = (df['Sentiment'].str.lower() == "negative").sum()
        avg_rating = df["Rating"].mean()
        satisfaction = (positive / total) * 100

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Feedback", total)
        col2.metric("Avg. Rating", f"{avg_rating:.2f}")
        col3.metric("Satisfaction %", f"{satisfaction:.1f}%")

        # 📊 Sentiment Counts
        st.subheader("🧠 Sentiment Breakdown")
        sentiment_counts = df["Sentiment"].value_counts()
        fig1, ax1 = plt.subplots()
        sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="Set2", ax=ax1)
        ax1.set_ylabel("Count")
        ax1.set_title("Customer Sentiment Count")
        st.pyplot(fig1)

        # 📈 Rating Distribution
        st.subheader("⭐ Rating Distribution")
        fig2, ax2 = plt.subplots()
        sns.histplot(df["Rating"], bins=5, kde=True, ax=ax2, color='teal')
        ax2.set_title("Distribution of Ratings")
        st.pyplot(fig2)

        # 🧩 Rating vs Sentiment Boxplot
        st.subheader("📊 Rating vs Sentiment")
        fig3, ax3 = plt.subplots()
        sns.boxplot(x="Sentiment", y="Rating", data=df, palette="Pastel1", ax=ax3)
        ax3.set_title("Rating by Sentiment")
        st.pyplot(fig3)

    except Exception as e:
        st.error(f"Error reading feedback.csv: {e}")


import streamlit as st
import pandas as pd
import os
from PIL import Image
import plotly.express as px

# -------------------------
# CONFIG
# -------------------------
BASE_PATH = "C:/Users/Thanusha/Desktop/project2"

st.set_page_config(layout="wide")
st.title("🗳️ Suspicious Voter Monitoring System")

# -------------------------
# IMAGE LOADER
# -------------------------
def load_image(path):
    if pd.isna(path):
        return None

    path = str(path).replace("\\", "/")
    full_path = os.path.join(BASE_PATH, path)
    full_path = os.path.normpath(full_path)

    if os.path.exists(full_path):
        return Image.open(full_path)
    return None

# -------------------------
# LOAD CSV
# -------------------------
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # Fix paths
    df['voted_image_path'] = df['voted_image_path'].astype(str).str.replace("\\", "/", regex=False)
    df['original_image_path'] = df['original_image_path'].astype(str).str.replace("\\", "/", regex=False)

    st.success("File Loaded Successfully")

    # -------------------------
    # TOP STATS
    # -------------------------
    st.subheader("📊 Overview Statistics")

    col1, col2, col3, col4, col5 = st.columns(5)

    total_votes = len(df)
    legit_votes = len(df[df['fraud_type'] == "legitimate"])
    suspicious_votes = len(df[df['is_suspicious'] == True])
    unique_voters = df['actual_voter_id'].nunique()
    fraud_rate = (suspicious_votes / total_votes) * 100

    col1.metric("Total Votes", total_votes)
    col2.metric("Legitimate", legit_votes)
    col3.metric("Suspicious", suspicious_votes)
    col4.metric("Unique Voters", unique_voters)
    col5.metric("Fraud Rate", f"{fraud_rate:.1f}%")

    st.markdown("---")

    # -------------------------
    # LAYOUT
    # -------------------------
    left, right = st.columns([2, 2])

    # =========================
    # LEFT SIDE
    # =========================
    with left:

        st.subheader("🚨 Suspicious Voter Categories")

        fraud_types = df['fraud_type'].unique()
        selected_type = st.selectbox("Select a suspicious activity type", fraud_types)

        filtered_df = df[df['fraud_type'] == selected_type]

        voter_ids = filtered_df['actual_voter_id'].unique()
        selected_voter = st.selectbox("Select a voter ID", voter_ids)

        voter_data = df[df['actual_voter_id'] == selected_voter]

        # -------------------------
        # DETAILS TABLE (UPDATED)
        # -------------------------
        st.subheader(f"📋 Details for Voter ID: {selected_voter}")

        st.dataframe(voter_data[[
            'actual_voter_id',          # ✅ REGISTERED
            'claimed_voter_id',
            'registered_constituency',
            'voting_constituency',
            'fraud_type'
        ]])

        st.markdown("---")

        # -------------------------
        # FACE COMPARISON
        # -------------------------
        st.subheader("🧑‍🤝‍🧑 Face Comparison")

        for _, row in voter_data.iterrows():

            actual_id = row['actual_voter_id']
            claimed_id = row['claimed_voter_id']

            original_img = load_image(row['original_image_path'])
            detected_img = load_image(row['voted_image_path'])

            c1, c2 = st.columns(2)

            with c1:
                st.markdown("**Original Voter**")
                st.caption(f"Registered ID: {claimed_id}")
                if original_img:
                    st.image(original_img, width=220)
                else:
                    st.error("Not found")

            with c2:
                st.markdown("**Detected Face**")
                st.caption(f"Detected ID: {actual_id}")
                if detected_img:
                    st.image(detected_img, width=220)
                else:
                    st.error("Not found")

            if row['fraud_type'] != "legitimate":
                st.error(f"🚨 Fraud: {actual_id} impersonating {claimed_id}")
            else:
                st.success("✅ Legitimate")

            st.markdown("---")

    # =========================
    # RIGHT SIDE
    # =========================
    with right:

        st.subheader("📊 Fraud Type Distribution")

        fraud_counts = df['fraud_type'].value_counts().reset_index()
        fraud_counts.columns = ['Fraud Type', 'Count']

        fig_pie = px.pie(fraud_counts, values='Count', names='Fraud Type')
        st.plotly_chart(fig_pie, use_container_width=True)

        st.subheader("🗺️ Constituency-wise Suspicious Votes")

        suspicious_df = df[df['is_suspicious'] == True]

        if len(suspicious_df) > 0:

            constituency_counts = (
                suspicious_df.groupby('voting_constituency')['actual_voter_id']
                .nunique()
                .reset_index()
            )

            constituency_counts.columns = ['Constituency', 'Suspicious Voters']

            fig_bar = px.bar(
                constituency_counts,
                x='Constituency',
                y='Suspicious Voters',
                color='Suspicious Voters'
            )

            st.plotly_chart(fig_bar, use_container_width=True)

        else:
            st.info("No suspicious votes found")

else:
    st.info("Upload your CSV to start")
import streamlit as st

st.set_page_config(page_title="Lots", page_icon="⛃", layout="centered")
with st.sidebar:    
    st.title("⛃ Lots")
    st.caption("Split the bill equitably.")
    st.markdown("---")
    st.markdown("[GitHub Repo](https://github.com/josequiceno2000/lots)")

with st.form("tip_form"):
    total = st.number_input("What was the total bill?", min_value=0.0, step=0.01, format="%.2f")
    tip_percent = st.selectbox("How much tip would you like to give?", [10, 12, 15, 20, 25])
    people = st.number_input("How many people to split the bill?", min_value=1, step=1)

    submitted = st.form_submit_button("Calculate split cost")

if submitted and total > 0:
    tip_amount = total * (tip_percent / 100)
    total_with_tip = total + tip_amount
    split_amount = total_with_tip / people

    st.subheader("Each person should pay:")
    st.success(f"${split_amount:.2f}")
import streamlit as st

st.set_page_config(
    page_title="SmartNest Profit Calculator",
    page_icon="💡",
    layout="centered"
)
st.markdown("""
<style>
.stApp {
    background-color: #FFFFFF;
}

h1, h2, h3 {
    color: #0B1933 !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px;
}

.stButton > button {
    background-color: #D4A843;
    color: #14213D;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    padding: 10px 20px;
}

.stButton > button:hover {
    background-color: #BD9235;
    color: #FFFFFF;
}
/* Make general text darker and clearer */
.stApp p,
.stApp label,
.stApp span,
.stMarkdown {
    color: #17243B !important;
    font-weight: 500 !important;
}

/* Make input labels stronger */
.stNumberInput label {
    color: #101D35 !important;
    font-weight: 700 !important;
}

/* Improve the tagline */
.stCaption {
    color: #A47719 !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("SmartNest Business Profit Calculator")
st.caption("Learn • Build • Grow")

st.write(
    "A simple business tool to help you understand "
    "your sales, expenses and profit."
)
st.write(
    "Calculate your business revenue, expenses and profit easily."
)
st.subheader("Your Business Results")

col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Revenue", f"₦{total_revenue:,.2f}")
        st.metric("Total Profit", f"₦{total_profit:,.2f}")

    with col2:
        st.metric("Total Expenses", f"₦{total_cost:,.2f}")
        st.metric("Profit Margin", f"{profit_margin:.2f}%")

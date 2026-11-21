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
st.subheader("Enter Your Business Details")

cost_per_item = st.number_input(
    "Cost Price per Item (₦)", min_value=0.0, value=0.0
)

selling_price = st.number_input(
    "Selling Price per Item (₦)", min_value=0.0, value=0.0
)

quantity_sold = st.number_input(
    "Quantity Sold", min_value=0, step=1
)

other_expenses = st.number_input(
    "Additional Expenses (₦)", min_value=0.0, value=0.0
)

total_revenue = selling_price * quantity_sold

total_cost = (cost_per_item * quantity_sold) + other_expenses

total_profit = total_revenue - total_cost

if total_revenue > 0:
    profit_margin = (total_profit / total_revenue) * 100
else:
    profit_margin = 0
    
st.subheader("Your Business Results")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Revenue", f"₦{total_revenue:,.2f}")
    st.metric("Total Profit", f"₦{total_profit:,.2f}")

with col2:
    st.metric("Total Expenses", f"₦{total_cost:,.2f}")
    st.metric("Profit Margin", f"{profit_margin:.2f}%")

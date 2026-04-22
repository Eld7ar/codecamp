import streamlit as st

st.title('Personal Money Management 💰', anchor=False)
st.subheader('Track your expenses, set budgets, and manage your finances effectively.')
if "expenses" not in st.session_state:
    st.session_state.expenses = []
with st.form("expense_form"):
    st.write("Add a new expense:")
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    date = st.date_input("Date")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        st.session_state.expenses.append({"description": description, "amount": amount, "date": date})
        st.success("Expense added successfully!")
if st.session_state.expenses:
    st.subheader("Your Expenses:")
    for expense in st.session_state.expenses:
        st.write(f"{expense['date']}: {expense['description']} - ${expense['amount']:.2f}")
else:    st.info("No expenses added yet. Start by adding your first expense!")

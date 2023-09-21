import streamlit as st

if "EXPENSES_TO_SUBMIT" not in list(st.session_state.keys()):
    st.session_state["EXPENSE_INDEX"] = 0
    st.session_state["EXPENSES_TO_SUBMIT"] = {}


def add_expense_to_list():
    expense = {
        "requester_name": st.session_state["requester_name"],
        "expense_name": st.session_state["expense_name"],
        "expense_description": st.session_state["expense_description"],
        "expense_date": st.session_state["expense_date"],
        "expense_amount": st.session_state["expense_amount"],
        "reimbursement_amount": st.session_state["reimbursement_amount"],
        "file_data": st.session_state["file_data"],
    }

    for k in list(expense.keys()):
        if expense[k] == "" or expense[k] == 0:
            st.error(f"Please enter value for {k} in expense. Showing {expense[k]}")
    else:
        expense = {st.session_state["EXPENSE_INDEX"]: expense}

        st.session_state["EXPENSES_TO_SUBMIT"] = {
            **st.session_state["EXPENSES_TO_SUBMIT"],
            **expense,
        }
        st.session_state["EXPENSE_INDEX"] = st.session_state["EXPENSE_INDEX"] + 1


st.title("Submit Your Expense for Reimbursement by the Foundation")
st.title("Submit Your Expenses:")
st.write("Total Expenses submitted thus far:", st.session_state["EXPENSE_INDEX"])

st.text_input("Requester Name", "", key="requester_name")
st.text_input(label="Expense Name", key="expense_name")
st.text_area(label="Expense Description", key="expense_description")
st.date_input(label="Expense Date", key="expense_date")
st.number_input(label="Expense Amount", key="expense_amount")
st.number_input(label="Reimbursement Amount Requested", key="reimbursement_amount")
st.file_uploader("Upload Image of Receipt", key="file_data")

# st.form_submit_button(
st.button(
    "Add to expenses to submit",
    use_container_width=True,
    on_click=add_expense_to_list,
    type="primary",
)


st.title("Submitted Expenses:")
# st.write(st.session_state["EXPENSES_TO_SUBMIT"])

if len(st.session_state["EXPENSES_TO_SUBMIT"].keys()) != 0:
    for idx in st.session_state["EXPENSES_TO_SUBMIT"].keys():
        st.markdown(
            f""" 
            ```
            Requester Name: {st.session_state['EXPENSES_TO_SUBMIT'][idx]["requester_name"]}
            Expense Date: {st.session_state['EXPENSES_TO_SUBMIT'][idx]["expense_date"]}
            Expense Name: {st.session_state['EXPENSES_TO_SUBMIT'][idx]["expense_name"]}
            Expense Amount: {st.session_state['EXPENSES_TO_SUBMIT'][idx]["expense_amount"]}
            Reimbursement Amount: {st.session_state['EXPENSES_TO_SUBMIT'][idx]["reimbursement_amount"]}
            File Upload Data: {st.session_state['EXPENSES_TO_SUBMIT'][idx]["file_data"] is not None}
            ```
            """
        )

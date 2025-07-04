import streamlit as st
import pandas as pd

# Load the data
final_report = pd.read_csv('Updated_Fiscal_Years_Data_Report.csv')
summary_report = pd.read_csv('Summary_Fiscal_Years_Data_Report.csv')

# Define chatbot function
def financial_chatbot(user_query, company_input, fiscal_year):
    try:
        if user_query == "What is the total revenue?":
            revenue = final_report[
                (final_report['Year'] == fiscal_year) & 
                (final_report['Company'] == company_input)
            ]['Total Revenue'].values[0]
            return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue}"
        
        elif user_query == "What is the Net Income?":
            net_income = final_report[
                (final_report['Year'] == fiscal_year) & 
                (final_report['Company'] == company_input)
            ]['Net Income'].values[0]
            return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {net_income}"
        
        elif user_query == "What is the sum of total assets?":
            total_assets = final_report[
                (final_report['Year'] == fiscal_year) & 
                (final_report['Company'] == company_input)
            ]['Total Assets'].values[0]
            return f"The sum of Total Assets for {company_input} for fiscal year {fiscal_year} is $ {total_assets}"
        
        elif user_query == "What is the sum of total liabilities?":
            total_liabilities = final_report[
                (final_report['Year'] == fiscal_year) & 
                (final_report['Company'] == company_input)
            ]['Total Liabilities'].values[0]
            return f"The sum of Total Liabilities for {company_input} for fiscal year {fiscal_year} is $ {total_liabilities}"
        
        elif user_query == "What is cash flow from operating activities?":
            cash_ops = final_report[
                (final_report['Year'] == fiscal_year) & 
                (final_report['Company'] == company_input)
            ]['Cash Flow from Operating Activities'].values[0]
            return f"The Cash Flow from Operating Activities for {company_input} for fiscal year {fiscal_year} is $ {cash_ops}"
        
        elif user_query == "What is the revenue growth(%) ?":
            revenue_growth = final_report[
                (final_report['Year'] == fiscal_year) & 
                (final_report['Company'] == company_input)
            ]['Revenue Growth (%)'].values[0].round(4)
            return f"The Revenue Growth(%) for {company_input} for fiscal year {fiscal_year} is {revenue_growth}(%)"
        
        elif user_query == "What is the net income growth(%) ?":
            net_income_growth = final_report[
                (final_report['Year'] == fiscal_year) & 
                (final_report['Company'] == company_input)
            ]['Net Income Growth (%)'].values[0].round(4)
            return f"The Net Income Growth(%) for {company_input} for fiscal year {fiscal_year} is {net_income_growth}(%)"
        
        elif user_query == "What is the year by year average revenue growth rate(%)?":
            year_avg_revenue_growth = summary_report[
                summary_report['Company'] == company_input
            ]['Revenue Growth (%)'].values[0].round(4)
            return f"The Year By Year Average Revenue Growth Rate(%) for {company_input} is {year_avg_revenue_growth}(%)"
        
        else:
            return "Sorry, I cannot process your query. Please ask something else."
    except Exception as e:
        return "Error: Please check the company name, fiscal year, or your query."

# Streamlit UI
st.title("AI-Driven Financial Chatbot")
st.write("This chatbot can answer your financial queries based on company data.")

# Company selection
company_input = st.selectbox(
    "Select the Company",
    options=['Microsoft', 'Tesla', 'Apple']
)

# Fiscal year selection
fiscal_year = st.selectbox(
    "Select the Fiscal Year",
    options=[2023, 2022, 2021]
)

# User query
user_query = st.text_input(
    "Enter your query",
    help="Example queries: What is the total revenue?, What is the Net Income?"
)

# Submit button
if st.button("Submit"):
    if user_query:
        response = financial_chatbot(user_query, company_input, fiscal_year)
        st.success(response)
    else:
        st.error("Please enter a query.")

import streamlit as st

# Predefined dataset
faq_data = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "Tell me about Thoughtful AI's Agents.",
        "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "question": "What are the benefits of using Thoughtful AI's agents?",
        "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }
]

# Function to find the most relevant answer
def get_answer(user_input):
    user_input_lower = user_input.lower()
    for item in faq_data:
        if all(word.lower() in user_input_lower for word in item["question"].split() if len(word) > 3):
            return item["answer"]
    return "I'm sorry, I don't have a specific answer for that. Can you please rephrase your question?"

# Streamlit UI
st.title("Thoughtful AI Customer Support Agent")
st.write("Ask me anything about Thoughtful AI's Agents!")

user_question = st.text_input("Your Question:")

if user_question:
    answer = get_answer(user_question)
    st.markdown(f"**Answer:** {answer}")

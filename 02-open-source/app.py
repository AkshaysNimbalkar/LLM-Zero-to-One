import streamlit as st
import time  # For simulating a delay

# Example RAG function (replace this with your actual function)
def rag_function(query):
    time.sleep(2)  # Simulate a delay
    return f"Processed result for query: {query}"

# Streamlit app
st.title("RAG Query App")

# Input box
query = st.text_input("Enter your query:")

# Button to invoke RAG function
if st.button("Ask"):
    with st.spinner("Processing..."):
        result = rag_function(query)
        st.success("Done!")
        st.write(result)

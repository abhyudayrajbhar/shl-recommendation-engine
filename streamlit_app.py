import streamlit as st
from recommend import get_recommendations

st.set_page_config(page_title="Assessment Recommendation")

st.title("Assessment Recommendation Engine")

query = st.text_input("Enter a Job Description or Query:")

if st.button("Get Recommendations"):
    if query:
        with st.spinner("Fetching recommendations..."):
            results = get_recommendations(query)
            if not results.empty:
                st.dataframe(results[['Assessment Name', 'URL', 'Remote Testing', 'Adaptive Support', 'Duration', 'Test Type']])
            else:
                st.warning("No matching assessments found.")
    else:
        st.warning("Please enter a query.")

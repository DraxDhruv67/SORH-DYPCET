import streamlit as st

st.set_page_config(page_title="SORH – DYPCET")

st.title("DYPCET Smart Opportunity & Resource Hub")

name = st.text_input("Enter your name")
skills = st.text_input("Your skills")
interest = st.selectbox("Interest", ["Hackathons","Internships","Startups","Placements"])

if st.button("Get Opportunities"):
    st.success("Top Recommended Opportunity:")
    st.write("Web Development Internship – Match Score: 87%")
    st.write("Reason: Matches your skills and interest")

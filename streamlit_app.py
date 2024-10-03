import streamlit as st
import pandas as pd
import re

# Apply custom CSS for enhanced aesthetics with vibrant and pastel colors
st.markdown(
    """
    <style>
    /* Overall Background */
    body {
        background-color: #FFF8F0; /* Soft pastel background */
    }
    /* Title Styling */
    .title {
        color: #FF6F61; /* Vibrant coral */
        font-size: 48px;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        margin-bottom: 10px;
    }
    /* Subtitle Styling */
    .subtitle {
        color: #6B5B95; /* Muted purple */
        font-size: 24px;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        margin-bottom: 30px;
    }
    /* Team Members List */
    .names-list {
        color: #2C3E50;
        font-size: 20px;
        list-style-type: none;
        padding: 0;
        text-align: center;
    }
    .names-list li {
        padding: 5px 0;
    }
    /* Section Headers */
    .section-header {
        color: #ECBDC4; /* Fresh green */
        font-size: 32px;
        margin-top: 40px;
        border-bottom: 3px solid #ECBDC4;
        padding-bottom: 10px;
        font-family: 'Poppins', sans-serif;
    }
    /* Input Fields Styling */
    textarea textarea {
        background-color: #FFFFFF;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    /* Contribution Table */
    .contribution-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }
    .contribution-table th, .contribution-table td {
        border: 1px solid #A8A8A8;
        text-align: left;
        padding: 12px;
    }
    .contribution-table th {
        background-color: #ECBDC4;
        color: white;
    }
    /* Footer Styling */
    .footer {
        text-align: center;
        color: #A8A8A8;
        margin-top: 50px;
        font-size: 14px;
        font-family: 'Poppins', sans-serif;
    }
    /* Button Styling */
    .stButton button {
        background-color: #FF6F61;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #e65c54;
    }
    /* Collapsible Sections */
    .streamlit-expanderHeader {
        font-size: 20px;
        font-weight: bold;
        color: #6B5B95;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Subtitle
st.markdown('<div class="title">Fall 2024 ML Project</div>', unsafe_allow_html=True)

# Team Members
st.markdown("### **Team Members**", unsafe_allow_html=True)
names = ["Erin Tan", "Eileen Yang", "Wesley Tam", "Tong Jing", "Steven Li"]
st.markdown(
    "<ul class='names-list'>" +
    "".join([f"<li>{name}</li>" for name in names]) +
    "</ul>",
    unsafe_allow_html=True
)

# Project Proposal Section
st.markdown('<div class="section-header">Project Proposal</div>', unsafe_allow_html=True)

# YouTube Video Embed
with st.container():
    st.markdown("#### **Project Overview Video**")
    youtube_url = st.text_input("Paste your YouTube video URL here:")
    if youtube_url:
        # Extract the video ID from the URL
        match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', youtube_url)
        if match:
            video_id = match.group(1)
            embed_url = f"https://www.youtube.com/embed/{video_id}"
            st.video(embed_url)
        else:
            st.warning("Please enter a valid YouTube URL.")

# Subsections with Collapsible Containers for Better Organization
subsections = [
    "Introduction & Background",
    "Problem Definition",
    "Methods",
    "Potential Results & Discussions",
    "References",
    "Gantt Chart"
]

for subsection in subsections:
    with st.expander(f"**{subsection}**", expanded=False):
        st.text_area(f"Enter content for {subsection.lower()} here...", height=150)

# Contribution Table
st.markdown('<div class="section-header">Contributions</div>', unsafe_allow_html=True)

# Create a DataFrame for contributions
contribution_data = {
    "Team Member": names,
    "Contribution": [""] * len(names)
}
df = pd.DataFrame(contribution_data)

# Style the table using HTML
def table_to_html(df):
    return df.to_html(index=False, classes='contribution-table')

st.markdown(table_to_html(df), unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        &copy; 2024 Fall ML Project Team. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)

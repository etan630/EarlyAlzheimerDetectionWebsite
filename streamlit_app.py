import streamlit as st
import pandas as pd
import re

# Apply custom CSS for enhanced aesthetics with modern colors for light and dark modes
st.markdown(
    """
    <style>
    /* Import 'Poppins' font from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Common Styles */
    body {
        font-family: 'Poppins', sans-serif;
    }
    .title {
        font-size: 48px;
        text-align: center;
        margin-bottom: 10px;
        font-weight: 600;
    }
    .subtitle {
        font-size: 24px;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 400;
    }
    .names-list {
        font-size: 20px;
        list-style-type: none;
        padding: 0;
        text-align: center;
        margin-bottom: 40px;
    }
    .names-list li {
        padding: 5px 0;
        font-weight: 500;
    }
    .section-header {
        font-size: 32px;
        margin-top: 40px;
        border-bottom: 3px solid;
        padding-bottom: 10px;
        font-weight: 600;
    }
    textarea textarea {
        background-color: #FFFFFF;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
    }
    .contribution-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        font-family: 'Poppins', sans-serif;
    }
    .contribution-table th, .contribution-table td {
        border: 1px solid;
        text-align: left;
        padding: 12px;
    }
    .contribution-table th {
        font-weight: 600;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #A0AEC0;
    }
    .stButton button {
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        font-family: 'Poppins', sans-serif;
        transition: background-color 0.3s ease;
    }
    .streamlit-expanderHeader {
        font-size: 20px;
        font-weight: bold;
    }

    /* Light Mode Styles */
    @media (prefers-color-scheme: light) {
        body {
            background-color: #F5F7FA; /* Light neutral background */
            color: #2D3748; /* Dark slate text */
        }
        .title {
            color: #1A202C; /* Darker shade for titles */
        }
        .subtitle {
            color: #4A5568; /* Slate gray for subtitles */
        }
        .names-list {
            color: #1A202C; /* Dark color for names in light mode */
        }
        .section-header {
            color: #2B6CB0; /* Blue for section headers */
            border-color: #2B6CB0;
        }
        .contribution-table th {
            background-color: #2B6CB0; /* Blue header */
            color: white;
            border-color: #CBD5E0;
        }
        .contribution-table td {
            border-color: #CBD5E0;
        }
        .contribution-table tr:nth-child(even) {
            background-color: #EDF2F7; /* Light gray for even rows */
        }
        .footer {
            color: #A0AEC0;
        }
        .stButton button {
            background-color: #2B6CB0; /* Blue button */
            color: white;
        }
        .stButton button:hover {
            background-color: #2C5282; /* Darker blue on hover */
        }
        /* Collapsible Sections */
        .streamlit-expanderHeader {
            color: #2B6CB0; /* Blue for headers */
        }
    }

    /* Dark Mode Styles */
    @media (prefers-color-scheme: dark) {
        body {
            background-color: #1A202C; /* Dark background */
            color: #E2E8F0; /* Light text */
        }
        .title {
            color: #63B3ED; /* Light blue for titles */
        }
        .subtitle {
            color: #A0AEC0; /* Grayish blue for subtitles */
        }
        .names-list {
            color: #E2E8F0; /* Keep same light color in dark mode */
        }
        .section-header {
            color: #90CDF4; /* Light blue for section headers */
            border-color: #90CDF4;
        }
        .contribution-table th {
            background-color: #63B3ED; /* Light blue header */
            color: white;
            border-color: #4A5568;
        }
        .contribution-table td {
            border-color: #4A5568;
        }
        .contribution-table tr:nth-child(even) {
            background-color: #2D3748; /* Darker gray for even rows */
        }
        .footer {
            color: #A0AEC0;
        }
        .stButton button {
            background-color: #63B3ED; /* Light blue button */
            color: white;
        }
        .stButton button:hover {
            background-color: #4299E1; /* Darker blue on hover */
        }
        /* Collapsible Sections */
        .streamlit-expanderHeader {
            color: #63B3ED; /* Light blue for headers */
        }
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
    youtube_url = st.text_input("Youtube Video Here:")
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

# Create a DataFrame for contributions with specified entries
contribution_data = {
    "Team Member": names,
    "Contribution": [
        "- Created, organized, and managed website <br> - Organized meetings <br> - References <br> - Potential Results & Discussions.",
        "- Introduction & Background <br> - Potential Results & Discussions.",
        "- Problem Definition <br> - Methods",
        "- Methods <br> - References",
        "- Introduction & Background <br> - Problem Definition."
    ]
}
df = pd.DataFrame(contribution_data)

# Style the table using HTML
def table_to_html(df):
    return df.to_html(index=False, classes='contribution-table', escape=False)

st.markdown(table_to_html(df), unsafe_allow_html=True)


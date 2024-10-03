import streamlit as st
import pandas as pd
import re

# -------------------- Custom CSS --------------------
def apply_custom_css():
    """
    Applies custom CSS to enhance the aesthetics of the Streamlit app.
    Includes styles for light and dark modes, typography, buttons, tables, and more.
    """
    css = """
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
            background-color: #F5F7FA !important; /* Light neutral background */
            color: #2D3748 !important; /* Dark slate text */
        }
        .title {
            color: #1A202C !important; /* Darker shade for titles */
        }
        .subtitle {
            color: #4A5568 !important; /* Slate gray for subtitles */
        }
        .names-list {
            color: #1A202C !important; /* Dark color for names in light mode */
        }
        .section-header {
            color: #2B6CB0 !important; /* Blue for section headers */
            border-color: #2B6CB0 !important;
        }
        .contribution-table th {
            background-color: #2B6CB0 !important; /* Blue header */
            color: white !important;
            border-color: #CBD5E0 !important;
        }
        .contribution-table td {
            border-color: #CBD5E0 !important;
        }
        .contribution-table tr:nth-child(even) {
            background-color: #EDF2F7 !important; /* Light gray for even rows */
        }
        .footer {
            color: #A0AEC0 !important;
        }
        .stButton button {
            background-color: #2B6CB0 !important; /* Blue button */
            color: white !important;
        }
        .stButton button:hover {
            background-color: #2C5282 !important; /* Darker blue on hover */
        }
        /* Collapsible Sections */
        .streamlit-expanderHeader {
            color: #2B6CB0 !important; /* Blue for headers */
        }
    }

    /* Dark Mode Styles */
    @media (prefers-color-scheme: dark) {
        body {
            background-color: #1A202C !important; /* Dark background */
            color: #E2E8F0 !important; /* Light text */
        }
        .title {
            color: #63B3ED !important; /* Light blue for titles */
        }
        .subtitle {
            color: #A0AEC0 !important; /* Grayish blue for subtitles */
        }
        .names-list {
            color: #E2E8F0 !important; /* Keep same light color in dark mode */
        }
        .section-header {
            color: #90CDF4 !important; /* Light blue for section headers */
            border-color: #90CDF4 !important;
        }
        .contribution-table th {
            background-color: #63B3ED !important; /* Light blue header */
            color: white !important;
            border-color: #4A5568 !important;
        }
        .contribution-table td {
            border-color: #4A5568 !important;
        }
        .contribution-table tr:nth-child(even) {
            background-color: #2D3748 !important; /* Darker gray for even rows */
        }
        .footer {
            color: #A0AEC0 !important;
        }
        .stButton button {
            background-color: #63B3ED !important; /* Light blue button */
            color: white !important;
        }
        .stButton button:hover {
            background-color: #4299E1 !important; /* Darker blue on hover */
        }
        /* Collapsible Sections */
        .streamlit-expanderHeader {
            color: #63B3ED !important; /* Light blue for headers */
        }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# -------------------- Header Section --------------------
def display_header():
    """
    Displays the main title and subtitle of the application.
    """
    st.markdown('<div class="title">Fall 2024 ML Project</div>', unsafe_allow_html=True)

# -------------------- Team Members Section --------------------
def display_team_members(names):
    """
    Displays the list of team members in a styled list.

    Args:
        names (list): List of team member names.
    """
    st.markdown("### **Team Members**", unsafe_allow_html=True)
    st.markdown(
        "<ul class='names-list'>" +
        "".join([f"<li>{name}</li>" for name in names]) +
        "</ul>",
        unsafe_allow_html=True
    )

# -------------------- Project Proposal Section --------------------
def display_project_proposal():
    """
    Displays the Project Proposal section, including an embedded YouTube video
    and collapsible subsections for detailed content.
    """
    st.markdown('<div class="section-header">Project Proposal</div>', unsafe_allow_html=True)

    # Project Overview Video
    st.markdown("#### **Project Overview Video**")
    youtube_url = st.text_input("Paste your YouTube video URL here:")
    if youtube_url:
        video_id = extract_youtube_id(youtube_url)
        if video_id:
            embed_url = f"https://www.youtube.com/embed/{video_id}"
            st.video(embed_url)
        else:
            st.warning("Please enter a valid YouTube URL.")

    # Collapsible Subsections
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

# -------------------- Contribution Section --------------------
def display_contributions(names):
    """
    Displays the Contributions section with a styled table.

    Args:
        names (list): List of team member names.
    """
    st.markdown('<div class="section-header">Contributions</div>', unsafe_allow_html=True)
    
    # Define contribution details for each team member
    contribution_data = {
        "Team Member": names,
        "Contribution": [
            "- Created, organized, and managed website<br>"
            "- Organized meetings<br>"
            "- References<br>"
            "- Potential Results & Discussions",
            "- Introduction & Background<br>"
            "- Potential Results & Discussions",
            "- Problem Definition<br>"
            "- Methods",
            "- Methods<br>"
            "- References",
            "- Introduction & Background<br>"
            "- Problem Definition"
        ]
    }
    df = pd.DataFrame(contribution_data)
    
    # Convert DataFrame to HTML with custom classes
    def table_to_html(df):
        return df.to_html(index=False, classes='contribution-table', escape=False)
    
    st.markdown(table_to_html(df), unsafe_allow_html=True)

# -------------------- Footer Section --------------------
def display_footer():
    """
    Displays the footer of the application.
    """
    st.markdown('<div class="footer">© 2024 ML Project Team. All rights reserved.</div>', unsafe_allow_html=True)

# -------------------- Helper Functions --------------------
def extract_youtube_id(url):
    """
    Extracts the YouTube video ID from a given URL.

    Args:
        url (str): YouTube video URL.

    Returns:
        str or None: Extracted video ID if valid, else None.
    """
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    return match.group(1) if match else None

# -------------------- Main Application --------------------
def main():
    """
    Main function to run the Streamlit application.
    """
    # Apply custom CSS
    apply_custom_css()

    # Display Header
    display_header()

    # Define team members
    team_members = ["Erin Tan", "Eileen Yang", "Wesley Tam", "Tong Jing", "Steven Li"]
    display_team_members(team_members)

    # Display Project Proposal
    display_project_proposal()

    # Display Contributions
    display_contributions(team_members)

    # Display Footer
    display_footer()

if __name__ == "__main__":
    main()

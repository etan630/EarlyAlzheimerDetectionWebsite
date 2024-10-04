import streamlit as st
import pandas as pd
import re

# -------------------- Custom CSS --------------------
def apply_custom_css():
    """
    Applies custom CSS to enhance the aesthetics of the Streamlit app.
    Includes styles for light mode only, typography, buttons, tables, and more.
    """
    css = """
    <style>
    /* Import 'Poppins' font from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Common Styles */
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #F5F7FA; /* Light neutral background */
        color: #2D3748; /* Dark slate text */
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
    .names-list span {
        padding: 5px 15px; /* Add padding for better spacing */
        font-weight: 500;
    }
    .section-header {
        font-size: 32px;
        margin-top: 40px;
        border-bottom: 3px solid #2B6CB0; /* Blue for section headers */
        padding-bottom: 10px;
        font-weight: 600;
        color: #2B6CB0; /* Color for section headers */
    }
    .contribution-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        font-family: 'Poppins', sans-serif;
    }
    .contribution-table th, .contribution-table td {
        border: 1px solid #CBD5E0; /* Light border color */
        text-align: left;
        padding: 12px;
    }
    .contribution-table th {
        background-color: #2B6CB0; /* Blue header */
        color: white;
        font-weight: 600;
    }
    .contribution-table tr:nth-child(even) {
        background-color: #EDF2F7; /* Light gray for even rows */
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
        background-color: #2B6CB0; /* Blue button */
        color: white;
    }
    .stButton button:hover {
        background-color: #2C5282; /* Darker blue on hover */
    }
    .streamlit-expanderHeader {
        font-size: 20px;
        font-weight: bold;
        color: #2B6CB0; /* Blue for headers */
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# -------------------- Header Section --------------------
def display_header():
    """
    Displays the main title and subtitle of the application.
    """
    st.markdown('<div class="title">Alzheimer Detection</div>', unsafe_allow_html=True)

# -------------------- Team Members Section --------------------
def display_team_members(names, links):
    """
    Displays the list of team members in a styled line.

    Args:
        names (list): List of team member names.
    """
    st.markdown("### <a id='team-members'></a>**Team Members**", unsafe_allow_html=True)
    st.markdown(
        "<div class='names-list'>" +
        " ".join([f"<span><a href='{link}'>{name}</a></span>" for name, link in zip(names, links)]) +
        "</div>",
        unsafe_allow_html=True
    )

# -------------------- Project Proposal Section --------------------
def display_project_proposal():
    """
    Displays the Project Proposal section, including an embedded YouTube video
    and subsections for detailed content.
    """
    st.markdown('<div class="section-header" id="project-proposal">Project Proposal</div>', unsafe_allow_html=True)

    # Project Overview Video
    st.markdown("#### **Project Overview Video**")
    youtube_url = st.text_input("Youtube Video Here:")
    if youtube_url:
        video_id = extract_youtube_id(youtube_url)
        if video_id:
            embed_url = f"https://www.youtube.com/embed/{video_id}"
            st.video(embed_url)
        else:
            st.warning("Please enter a valid YouTube URL.")

    # Subsections with direct content
    st.markdown("### <a id='introduction'></a>**Introduction & Background**</h3>", unsafe_allow_html=True)
    st.markdown("Enter content for introduction and background here...")

    st.markdown("### <a id='problem-definition'></a>**Problem Definition**</h3>", unsafe_allow_html=True)
    st.markdown(
        "**The Problem**<br>"
        "Alzheimer’s disease is a progressive neurodegenerative disorder, and early detection is critical for patient care, yet it is often diagnosed too late due to the difficulty of identifying subtle early-stage brain degeneration.<br><br>"
        "**The Solution**<br>"
        "We propose developing a machine learning model to analyze MRI images for early-stage Alzheimer’s detection, identifying subtle patterns in brain degeneration that may be missed by the human eye.<br><br>"
        "**How it Differs from Prior Literature**<br>"
        "Existing machine learning models mainly focus on detecting moderate to advanced stages of Alzheimer’s when brain degeneration is more pronounced. Our approach targets early-stage detection, which is harder to identify but crucial for improving patient outcomes by allowing timely clinical trials and treatments.",
        unsafe_allow_html=True
    )

    st.markdown("### <a id='methods'></a>**Methods**</h3>", unsafe_allow_html=True)
    st.markdown(
        "We will use the [OASIS MRI dataset](https://www.kaggle.com/datasets/ninadaithal/imagesoasis), which consists of 80,000 MRI brain scans, labeled according to the progression of Alzheimer’s present in the patient.<br><br>"
        "<b>Preprocessing Methods:</b><br>"
        "1. **Image Resizing**: All images will be resized to ensure they have the same dimensions, allowing for consistent feature space across all data points.<br>"
        "2. **Principal Component Analysis (PCA)**: We will apply PCA to reduce the dimensionality of our feature space, helping to prevent overfitting and decrease training times.<br>"
        "3. **Feature Standardization**: To ensure the viability of l1 and l2 penalties in our models, we will standardize the pixel values of our images before training.<br><br>"
        "<b>ML Algorithms:</b><br>"
        "1. **Multiclass Logistic Regression**: We will use logistic regression with possible l1 and/or l2 penalties for regularization, helping to improve generalization.<br>"
        "2. **Naive Bayes**: This algorithm assumes independence between features, which makes it efficient and robust, especially in high-dimensional feature spaces like image data.<br>"
        "3. **Convolutional Neural Networks (CNN)**: CNNs are well-suited for image classification tasks, as each layer can detect features and patterns through the use of sliding kernels, progressively recognizing larger and more complex patterns in the images.",
        unsafe_allow_html=True
    )

    st.markdown("### <a id='potential-results'></a>**Potential Results & Discussions**</h3>", unsafe_allow_html=True)
    st.markdown("Enter content for potential results and discussions here...")

    st.markdown("### <a id='references'></a>**References**</h3>", unsafe_allow_html=True)
    st.markdown("Enter references here...")

    st.markdown("### <a id='gantt-chart'></a>**Gantt Chart**</h3>", unsafe_allow_html=True)
    st.image("gantt_chart.png", caption='Gantt Chart', use_column_width=True)

# -------------------- Contribution Section --------------------
def display_contributions(names):
    """
    Displays the Contributions section with a styled table.

    Args:
        names (list): List of team member names.
    """
    st.markdown('<div class="section-header" id="contributions">Contributions</div>', unsafe_allow_html=True)
    
    # Define contribution details for each team member
    contribution_data = {
        "Team Member": names,
        "Contribution": [
            "- Managed website<br>"
            "- Organized meetings<br>"
            "- Problem Definition<br>"
            "- Potential Results & Discussions",
            "- Introduction & Background<br>"
            "- Potential Results & Discussions",
            "- Problem Definition<br>"
            "- Methods",
            "- Methods<br>"
            "- References",
            "- Introduction & Background<br>"
            "- References"
        ]
    }
    df = pd.DataFrame(contribution_data)
    
    # Convert DataFrame to HTML with custom classes
    def table_to_html(df):
        return df.to_html(index=False, classes='contribution-table', escape=False)
    
    st.markdown(table_to_html(df), unsafe_allow_html=True)

# -------------------- Git Repo Section --------------------
def display_gitrepo():
    """
    Displays the GitHub Repository link as an embedded badge.
    """
    st.markdown(
        "[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/etan630/Alzheimer-Detection)",
        unsafe_allow_html=True
    )

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

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    st.sidebar.markdown("[Team Members](#team-members)")
    st.sidebar.markdown("[Project Proposal](#project-proposal)")
    st.sidebar.markdown("[Introduction & Background](#introduction)")
    st.sidebar.markdown("[Problem Definition](#problem-definition)")
    st.sidebar.markdown("[Methods](#methods)")
    st.sidebar.markdown("[Potential Results & Discussions](#potential-results)")
    st.sidebar.markdown("[References](#references)")
    st.sidebar.markdown("[Gantt Chart](#gantt-chart)")
    st.sidebar.markdown("[Contributions](#contributions)")

    # Define team members
    team_members = ["Erin Tan", "Eileen Yang", "Wesley Tam", "Tong Jing", "Steven Li"]

    # Display sections
    team_members = ["Erin Tan", "Eileen Yang", "Wesley Tam", "Tong Jing", "Steven Li"]
    team_links = [
        "https://www.linkedin.com/in/erinctan/",
        "https://www.linkedin.com/in/eileenyang10/",
        "https://www.linkedin.com/in/wesley-tam-64a83b271/",
        "https://www.linkedin.com/in/tong-jing-05y/",
        "https://www.linkedin.com/in/stevenliii/"
    ]

    # Call the function with the team members and their links
    display_team_members(team_members, team_links)

    display_project_proposal()
    display_contributions(team_members)

    # Display Github Repo
    display_gitrepo()

if __name__ == "__main__":
    main()

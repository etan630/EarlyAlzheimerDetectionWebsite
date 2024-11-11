import streamlit as st
import pandas as pd
from PIL import Image  # Importing Image from PIL
import os  # Importing os for file path handling
# import re

# CSS stuff
def apply_custom_css():
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
    /* Carousel Button Styles */
    .carousel-button {
        background-color: #2B6CB0; /* Blue background */
        color: white; /* White text */
        border: none;
        border-radius: 50px; /* Rounded buttons */
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        margin: 10px; /* Space between buttons */
        transition: background-color 0.3s ease;
    }

    .carousel-button:hover {
        background-color: #2C5282; /* Darker blue on hover */
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Debugging Section 
def list_cnn_images():
    image_dir = "cnn_images"
    st.markdown("### **Debugging: List of Images in `cnn_images` Directory**")
    
    if not os.path.exists(image_dir):
        st.error(f"The directory `{image_dir}` does not exist.")
        return
    
    files = os.listdir(image_dir)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    if not image_files:
        st.warning(f"No image files found in `{image_dir}`.")
    else:
        st.write("**Available Images:**")
        for img in image_files:
            st.write(f"- {img}")

# Header Section 
def display_header():
    st.markdown('<div class="title">Alzheimer Detection</div>', unsafe_allow_html=True)

# Team Members Section 
def display_team_members(names, links):
    """
        names (list): List of team member names.
        links (list): List of URLs corresponding to each team member.
    """
    st.markdown("### <a id='team-members'></a>**Team Members**", unsafe_allow_html=True)
    st.markdown(
        "<div class='names-list'>" +
        " ".join([f"<span><a href='{link}' target='_blank'>{name}</a></span>" for name, link in zip(names, links)]) +
        "</div>",
        unsafe_allow_html=True
    )

# Project Proposal Section 
def display_project_proposal():
    st.markdown('<div class="section-header" id="project-proposal">Project Proposal</div>', unsafe_allow_html=True)
    
    # Project Overview Video
    st.markdown("### <a id='project-overview-video'></a>**Project Overview Video**", unsafe_allow_html=True)
    st.video("https://youtu.be/5lw-qKBNyoA") 

    # Midpoint Check Section
    st.markdown('<div class="section-header" id="midpoint-check">Midpoint Check</div>', unsafe_allow_html=True)

    # Introduction & Background
    st.markdown("#### <a id='introduction'></a>**Introduction & Background**", unsafe_allow_html=True)
    st.markdown(
        """
        Computer Aided Diagnosis (CAD) is a useful application of technology in the medical industry [3]. The use of CAD has the potential to improve and apply to many fields of medicine, especially Alzheimer’s disease. If detected early, the prognosis can be greatly improved, but early diagnosis with CAD can be inconsistent given the characteristics of the disease, with accuracy rates spanning 70-95% across various models [1]. Using various classification techniques, studies have been able to detect Alzheimer’s with results exceeding 90% accuracy with differentiation [2].

        The MRI scans from this [dataset](https://www.kaggle.com/datasets/ninadaithal/imagesoasis/data) are categorized by the level of dementia of each patient: Mild, Moderate, Very Mild, and Non-Demented Dementia.
        """,
        unsafe_allow_html=True
    )

    # Problem Definition
    st.markdown("#### <a id='problem-definition'></a>**Problem Definition**", unsafe_allow_html=True)
    st.markdown(
        "**The Problem**<br>"
        "Alzheimer’s disease is a progressive neurodegenerative disorder, and early detection is critical for patient care, yet it is often diagnosed too late due to the difficulty of identifying subtle early-stage brain degeneration.<br><br>"
        "**The Solution**<br>"
        "We propose a machine learning model to analyze images for early-stage Alzheimer’s detection, focusing on subtle patterns of brain degeneration that may be overlooked by doctors.<br><br>"
        "**How it Differs from Prior Literature**<br>"
        "While existing models primarily detect moderate to advanced Alzheimer’s stages, our approach emphasizes early detection, which is vital for timely clinical trials and treatments.",
        unsafe_allow_html=True
    )

    # Methods
    st.markdown("#### <a id='methods'></a>**Methods**", unsafe_allow_html=True)
    st.markdown(
        """
        **Dataset:**
        We will use the [OASIS MRI dataset](https://www.kaggle.com/datasets/ninadaithal/imagesoasis), which consists of 80,000 MRI brain scans, labeled according to the progression of Alzheimer’s present in the patient.
        """,
        unsafe_allow_html=True
    )

    # CNN Model
    st.markdown("##### <a id='cnn-model'></a>**CNN Model**", unsafe_allow_html=True)
    st.markdown(
        """
        **Progress During Midterm Checkpoint:**
        During this midterm checkpoint, we worked on implementing Convolutional Neural Networks (CNN).

        **Preprocessing Methods:**
        1. **Feature Standardization**: We normalized the pixel values by dividing by 255, bringing values to a range [0,1].
        2. **Brightness Adjustment**: Randomly adjusted the brightness to between 80% - 120% of the original to vary the lighting conditions.
        3. **Zoom Range**: Randomly zoomed 1% either in or out.
        4. **Horizontal Flip**: Flipped the photos horizontally for more variety.

        **Machine Learning Algorithms:**
        - **Convolutional Neural Networks (CNN)**: We chose CNN because CNNs are well-suited for image classification tasks, as each layer can detect features and patterns through the use of sliding kernels, progressively recognizing larger and more complex patterns in the images.
        - **Data Splitting**: We split the data into 70% training, 20% testing, and 10% validation.

        **Defining the CNN Model Layers:**
        1. **Rescaling (Rescaling)**: Rescales the input data.
        2. **Conv2D (Conv2D)**: Applies convolutional layers to extract features.
        3. **MaxPooling2D (MaxPooling2D)**: Reduces spatial dimensions.
        4. **Flatten (Flatten)**: Flattens the input.
        5. **Dense (Dense)**: Fully connected layers for classification.
        """,
        unsafe_allow_html=True
    )

    # Upcoming Models to Implement
    st.markdown("##### <a id='upcoming-models'></a>**Upcoming Models to Implement**", unsafe_allow_html=True)
    st.markdown(
        """
        - **Support Vector Machine (SVM):**
            SVMs are known for their performance with high-dimensional data, making them well-suited for classification tasks like determining the stage of Alzheimer’s in image scans. Their ability to handle complex decision boundaries makes them ideal for challenging classification problems in the dataset.
        - **Logistic Regression:**
            Logistic Regression would provide a baseline image classification, particularly when combined with feature extraction from the CNN model. It’s faster and more efficient than SVM, making it a great model for quick iterations. It would require careful feature preprocessing to capture the patterns effectively.
        """,
        unsafe_allow_html=True
    )

    # Results & Discussion Section 
    st.markdown("#### <a id='results-discussion'></a>**Results & Discussion**", unsafe_allow_html=True)

    # CNN Results & Discussion Subsection
    st.markdown("##### <a id='cnn-results-discussion'></a>**CNN Results & Discussion**", unsafe_allow_html=True)

    st.markdown(
        """
        At the outset, we predicted that CNNs would perform the best out of the three models that we seek to implement. We implemented our CNN first to serve as a benchmark for the models that we expect to perform worse. Our CNN shows the following performance metrics when executed on a 10% testing dataset of images:

        Refer to Section **Model Performance Evaluation and Visualization** in our `/notebooks/1_CNN.ipynb` file in our GitHub repository!
        """,
        unsafe_allow_html=True
    )

    try:
        image_path = "cnn_images/cnn_performance_metrics.png"  # Ensure the folder is named 'cnn_images'
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        image = Image.open(image_path)
        st.image(image, caption='CNN Performance Metrics', use_column_width=True)
    except Exception as e:
        st.error(f"Error loading image {image_path}: {e}")

    # Create a table with metrics and values
    cnn_metrics = {
        "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
        "Value": [0.9997108322248569, 0.9996747459096856, 0.9995429616087752, 0.9996085761354763]
    }
    df_cnn_metrics = pd.DataFrame(cnn_metrics)

    def table_to_html(df):
        return df.to_html(index=False, classes='contribution-table', escape=False)

    st.markdown("**Performance Metrics:**", unsafe_allow_html=True)
    st.markdown(table_to_html(df_cnn_metrics), unsafe_allow_html=True)

    # Explanations for each metric
    st.markdown(
        """
        We see from the metrics that the model performed extremely well on the test data, with values greater than 0.999 across all metrics. The interpretations of each metric are as follows:
        
        - **Accuracy**: Out of all predictions made by the model, >99.9% of predictions were correct classifications of the brain scan.
        - **Precision**: Averaged across each class, out of all positive predictions made by the model for that class, >99.9% of them were correct classifications of the brain scan.
        - **Recall**: Averaged across each class, out of all brain scans that were truly of that class, the model correctly classified them 99.9% of the time.
        - **F1 Score**: There is a near perfect balance between precision and recall, indicating that the model is relatively free of bias.
        """,
        unsafe_allow_html=True
    )

    # Debugging: List images
    # list_cnn_images()

    st.markdown("**Additional Visualizations:**", unsafe_allow_html=True)

    carousel_images = [
        "cnn_images/roc_per_class.png",
        "cnn_images/prob_mild.png",
        "cnn_images/prob_mod.png",
        "cnn_images/prob_non.png",
        "cnn_images/prob_verymild.png",
        "cnn_images/learning_loss_curve.png"
    ]

    if 'carousel_index' not in st.session_state:
        st.session_state.carousel_index = 0

    total_images = len(carousel_images)

    # Display the current image
    current_image_path = carousel_images[st.session_state.carousel_index]
    try:
        if not os.path.exists(current_image_path):
            raise FileNotFoundError(f"Image not found at path: {current_image_path}")
        current_image = Image.open(current_image_path)
        st.image(current_image, caption=os.path.basename(current_image_path), use_column_width=True)
    except Exception as e:
        st.error(f"Error loading image {current_image_path}: {e}")

    # Create three columns: empty, buttons, empty for centering
    button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

    with button_col1:
        pass  # Empty column for spacing

    with button_col2:
        # Previous Button
        if st.button("Previous", key="prev_button"):
            st.session_state.carousel_index = (st.session_state.carousel_index - 1) % total_images

    with button_col3:
        # Next Button
        if st.button("Next", key="next_button"):
            st.session_state.carousel_index = (st.session_state.carousel_index + 1) % total_images

    # Concluding paragraph
    st.markdown(
        """
        The model produced unexpectedly perfect results as shown by the metrics and visualizations, raising suspicions of overfitting as it may be following training data too closely. However, these high performing metrics and results were produced when the model was run on the testing data and not the training data, which provides evidence against overfitting. We believe that this high performance is a result of all of our brain scan images coming from the same data set, which contains very similar images and very consistent labeling schemes that allows the model to succeed with the given training and testing data.
        """,
        unsafe_allow_html=True
    )

    # References Section 
    st.markdown("### <a id='references'></a>**References**", unsafe_allow_html=True)
    st.markdown(
        "[1] A. Bhandarkar et al., “Deep learning based computer aided diagnosis of Alzheimer’s disease: A snapshot of last 5 years, gaps, and future directions,” Artificial Intelligence Review, vol. 57, no. 2, Feb. 2024. doi:10.1007/s10462-023-10644-8 <br><br>"
        "[2] A. Borji, A. Seifi, and T. H. Hejazi, “An efficient method for detection of Alzheimer’s disease using high-dimensional PET scan images,” Intelligent Decision Technologies, vol. 17, no. 3, pp. 729–749, Jul. 2023. doi:10.3233/idt-220315 <br><br>"
        "[3] H.-P. Chan, R. K. Samala, L. M. Hadjiiski, and C. Zhou, “Deep learning in medical image analysis,” Advances in Experimental Medicine and Biology, pp. 3–21, 2020. doi:10.1007/978-3-030-33128-3_1",
        unsafe_allow_html=True
    )

    st.markdown("### <a id='gantt-chart'></a>**Gantt Chart**", unsafe_allow_html=True)
    st.image("gantt_chart.png", caption='Gantt Chart', use_column_width=True)

# Contribution Section 
def display_contributions(names):
    """
    Displays the Contributions section with two styled tables:
    1. Midpoint Contributions
    2. Proposal Contributions

    Args:
        names (list): List of team member names.
    """
    st.markdown('<div class="section-header" id="contributions">Contributions</div>', unsafe_allow_html=True)
    
    # Midpoint Contributions
    st.markdown("#### <a id='midpoint-contributions'></a>**Midpoint Contributions**", unsafe_allow_html=True)
    
    midpoint_contribution_data = {
        "Team Member": names,
        "Contribution": [
            "• Managed Website<br>"
            "• Preprocessing Implementation<br>"
            "• Method Analysis",
            "• Data Visualization<br>"
            "• Results and Discussions<br>"
            "• Method Analysis",
            "• Preprocessing Implementation",
            "• Environment Setup<br>"
            "• Preprocessing Implementation<br>"
            "• CNN Implementation",
            "• Data Visualization<br>"
            "• Results and Discussions<br>"
            "• Method Analysis"
        ]
    }
    df_midpoint = pd.DataFrame(midpoint_contribution_data)
    
    def table_to_html(df):
        return df.to_html(index=False, classes='contribution-table', escape=False)
    
    st.markdown(table_to_html(df_midpoint), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)  # Add some space between tables

    # Proposal Contributions 
    st.markdown("#### <a id='proposal-contributions'></a>**Proposal Contributions**", unsafe_allow_html=True)
    
    proposal_contribution_data = {
        "Team Member": names,
        "Contribution": [
            "• Managed website<br>"
            "• Problem Definition<br>"
            "• Potential Results & Discussions",
            "• Introduction & Background<br>"
            "• Potential Results & Discussions",
            "• Problem Definition<br>"
            "• Methods",
            "• Methods<br>"
            "• References",
            "• Introduction & Background<br>"
            "• References"
        ]
    }
    df_proposal = pd.DataFrame(proposal_contribution_data)
    
    st.markdown(table_to_html(df_proposal), unsafe_allow_html=True)

# Git Repo Section 
def display_gitrepo():
    """
    Displays the GitHub Repository link as an embedded badge.
    """
    st.markdown("### <a id='git-repo'></a>**GitHub Repository**", unsafe_allow_html=True)
    st.markdown(
        "[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/etan630/Alzheimer-Detection)",
        unsafe_allow_html=True
    )

# Main Application
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
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Project Overview Video](#project-overview-video)")
    st.sidebar.markdown("[Midpoint Check](#midpoint-check)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Introduction & Background](#introduction)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Problem Definition](#problem-definition)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Methods](#methods)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CNN Model](#cnn-model)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Upcoming Models](#upcoming-models)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Results & Discussion](#results-discussion)")
    st.sidebar.markdown("[References](#references)")
    st.sidebar.markdown("[Gantt Chart](#gantt-chart)")
    st.sidebar.markdown("[Contributions](#contributions)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Midpoint Contributions](#midpoint-contributions)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Proposal Contributions](#proposal-contributions)")
    st.sidebar.markdown("[GitHub Repository](#git-repo)")

    # Define team members
    team_members = ["Erin Tan", "Eileen Yang", "Wesley Tam", "Tong Jing", "Steven Li"]
    team_links = [
        "https://www.linkedin.com/in/erinctan/",
        "https://www.linkedin.com/in/eileenyang10/",
        "https://www.linkedin.com/in/wesley-tam-64a83b271/",
        "https://www.linkedin.com/in/tong-jing-05y/",
        "https://www.linkedin.com/in/stevenliii/"
    ]

    # Display sections
    display_team_members(team_members, team_links)
    display_project_proposal()
    display_contributions(team_members)

    # Display Github Repo
    display_gitrepo()

if __name__ == "__main__":
    main()

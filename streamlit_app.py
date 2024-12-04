import streamlit as st
import pandas as pd
from PIL import Image  # Importing Image from PIL
import os  # Importing os for file path handling


# ---------------------------
# Helper Functions
# ---------------------------
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
    .title {
        font-size: 40px; /* Increased font size for main sections */
        text-align: center;
        margin-top: 40px;
        margin-bottom: 20px;
        border-bottom: 3px solid #2B6CB0; /* Blue for section headers */
        padding-bottom: 10px;
        font-weight: 600;
        color: #2B6CB0;
    }
    .section-header {
        font-size: 28px;
        margin-top: 0px;
        font-weight: 500;
        color: #2B6CB0; 
    }
    .subsection-header {
        font-size: 20px;
        margin-top: 0px;
        font-weight: 400;
        color: #2B6CB0; 
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

# --------------------
# Display Functions
# --------------------
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
    st.markdown('<div class="title" id="project-proposal">Project Proposal</div>', unsafe_allow_html=True)
    
    # Project Overview Video
    st.markdown('<div class="section-header" id="project-overview-video">Project Overview Video</div>', unsafe_allow_html=True)
    st.video("https://youtu.be/5lw-qKBNyoA") 

    # Final Findings
    st.markdown('<div class="title" id="final-findings">Final Findings</div>', unsafe_allow_html=True)

    # Introduction & Background
    st.markdown('<div class="section-header" id="introduction">Introduction & Background</div>', unsafe_allow_html=True)
    st.markdown(
        """
        Computer Aided Diagnosis (CAD) is a useful application of technology in the medical industry [3]. The use of CAD has the potential to improve and apply to many fields of medicine, especially Alzheimer’s disease. If detected early, the prognosis can be greatly improved, but early diagnosis with CAD can be inconsistent given the characteristics of the disease, with accuracy rates spanning 70-95% across various models [1]. Using various classification techniques, studies have been able to detect Alzheimer’s with results exceeding 90% accuracy with differentiation [2].

        The MRI scans from this [dataset](https://www.kaggle.com/datasets/ninadaithal/imagesoasis/data) are categorized by the level of dementia of each patient: Mild, Moderate, Very Mild, and Non-Demented Dementia.
        """,
        unsafe_allow_html=True
    )

    # Problem Definition
    st.markdown('<div class="section-header" id="problem-definition">Problem Definition</div>', unsafe_allow_html=True)
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
    st.markdown('<div class="section-header" id="methods">Methods</div>', unsafe_allow_html=True)
    st.markdown(
        """
        **Dataset:**
        We will use the [OASIS MRI dataset](https://www.kaggle.com/datasets/ninadaithal/imagesoasis), which consists of 80,000 MRI brain scans, labeled according to the progression of Alzheimer’s present in the patient.
        **Data Splitting**: We split all data for each model into 70% training, 20% testing, and 10% validation.
        """,
        unsafe_allow_html=True
    )

    # CNN Model
    st.markdown('<div class="subsection-header" id="cnn-model">CNN Model</div>', unsafe_allow_html=True)
    st.markdown(
        """
        **Preprocessing Methods:**
        1. **Feature Standardization**: We normalized the pixel values by dividing by 255, bringing values to a range [0,1].
        2. **Brightness Adjustment**: Randomly adjusted the brightness to between 80% - 120% of the original to vary the lighting conditions.
        3. **Zoom Range**: Randomly zoomed 1% either in or out.
        4. **Horizontal Flip**: Flipped the photos horizontally for more variety.

        **Why This Algorithm?**
        - **Convolutional Neural Networks (CNN)**: We chose CNN because CNNs are well-suited for image classification tasks, as each layer can detect features and patterns through the use of sliding kernels, progressively recognizing larger and more complex patterns in the images.

        **Defining the CNN Model Layers:**
        1. **Rescaling**: Rescales the input data.
        2. **Conv2D**: Applies convolutional layers to extract features.
        3. **MaxPooling2D**: Reduces spatial dimensions.
        4. **Flatten**: Flattens the input.
        5. **Dense**: Fully connected layers for classification.
        """,
        unsafe_allow_html=True
    )

    # logistic regression
    st.markdown('<div class="subsection-header" id="logistic-regression-model">Logistic Regression Model</div>', unsafe_allow_html=True)
    st.markdown(
        """
        **Progress During Midterm Checkpoint:**
        During this midterm checkpoint, we worked on implementing Convolutional Neural Networks (CNN).

        **Preprocessing Methods:**
        1. **preprocessing 1**:
        2. **preprocessing 2**:  

        **Why This Algorithm?**
        - **Logistic Regression**: We chose Logistic Regression because it provided a baseline image classification, particularly when combined with feature extraction from the CNN model. It’s faster and more efficient than SVM, making a great model for quick model iteration.
        """,
        unsafe_allow_html=True
    )

    # svm
    st.markdown('<div class="subsection-header" id="svm-model">SVM Model</div>', unsafe_allow_html=True)
    st.markdown(
        """
        **Preprocessing Methods:**
        1. **Grayscale Conversion**: Reduced complexity by having a single color channel instead of RGB.
        2. **Normalization**: Converted 2D image arrays into 1D feature vectors.
        3. **Data Type Conversion**: Converted data from float64 to float32 to half the memory consumption.
        4. **Undersampling**: Reduced the number of samples in majority classes to prevent the model from being biased towards majority classes.
        5. **PCA**: Reduced the number of features by transforming the high-dimensional data into a lower-dimensional space while retaining variance.

        **Why This Algorithm?**
        - **Support Vector Machine (SVM)**: SVMs are known for its performance with high-dimensional data, making it well-suited for classification tasks like determining the stage of Alzheimer’s in image scans. Its ability to handle complex decision boundaries would make it a good model for challenging classification problems in the datasets. Furthermore, using class weighting as a parameter adjusted the weights inversely proportional to class frequencies, allowing for more attention to minority classes.
        - We specifically chose to use LinearSVC since it processed large-scale data with high dimensions faster and offered more flexible regularization options. Using SVC was first attempted due to its suitability for both linear and non-linear classification tasks; however, it was highly inefficient on the large dataset.
        """,
        unsafe_allow_html=True
    )

    # Results & Discussion Section 
    st.markdown('<div class="section-header" id="results-discussion">Results & Discussion</div>', unsafe_allow_html=True)

    # CNN Results & Discussion Subsection
    st.markdown('<div class="subsection-header" id="cnn-results-discussion">CNN Results & Discussion</div>', unsafe_allow_html=True)

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
        st.image(image, caption='CNN Performance Metrics', use_container_width=True)
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
    st.markdown("**GradCam:**", unsafe_allow_html=True)
    st.markdown(
        """
        After running a gradcam algorithm on the last convolutional layer of the model, we find that the model seems to focus heavily on specific locations around the brain to determine the presence of Alzheimers, as shown in the following figures:
        """,
        unsafe_allow_html=True
    )
    try:
        image_path = "cnn_images/grad_cam1.png"  # Ensure the folder is named 'cnn_images'
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        image = Image.open(image_path)
        st.image(image, caption='GradCam Example 1', use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image {image_path}: {e}")

    try:
        image_path = "cnn_images/grad_cam2.png"  # Ensure the folder is named 'cnn_images'
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        image = Image.open(image_path)
        st.image(image, caption='GradCam Example 2', use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image {image_path}: {e}")

    st.markdown(
        """
        These figures all highlight the frontal lobe of the brain which shows that the model seems to realize that demented patients have a different brain size and frontal lobe than healthy patients. The gradcam also confirms that the model isn’t looking for watermarks in the image that would label the image.
        """,
        unsafe_allow_html=True
    )
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
        st.image(current_image, caption=os.path.basename(current_image_path), use_container_width=True)
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
        Examining the curves, we see that when plotting true positive rate against false positive rate, we obtain a visualization of the sensitivity-specificity tradeoff in multiple ROC curves (one for each class). We note that the area under the curve for all of them is essentially 1, with the curve very closely approaching a near 100% true positive rate and a near 0% false positive rate, suggesting a highly effective model that maximizes correct positive predictions while minimizing incorrect positive predictions to a near perfect rate such that nearly all positive brain scans for a given class have a higher likelihood assignment than negative scans. This is demonstrated by the probability distributions of true positive and false positive curves, where it is evident that thresholds very close to 0 will still correctly classify nearly all positive cases. Furthermore, the learning curve and loss curve show distinctly rapid improvement, approaching the validation accuracy within the first few epochs. 

        The model produced unexpectedly perfect results as shown by the metrics and visualizations, raising suspicions of overfitting as it may be following training data too closely. However, these high performing metrics and results were produced when the model was run on the testing data and not the training data, which provides evidence against overfitting. We believe that this high performance is a result of all of our brain scan images coming from the same data set, which contains very similar images and very consistent labeling schemes that allows the model to succeed with the given training and testing data. As we move forward, we plan to possibly introduce a dataset with more diversity, training our model on more varied and realistic data.

        """,
        unsafe_allow_html=True
    )

    # Logistic Regression Results & Discussion Subsection
    st.markdown('<div class="subsection-header" id="logistic-results-discussion">Logistic Regression Results & Discussion</div>', unsafe_allow_html=True)
    st.markdown(
        """
        Logistic Regression models are good and efficient at classifying the differences between classes. We wanted to see if Logistic Regression would compare to our CNN model. We first trained a model on the original data (before balancing), then we trained a model on a balanced subset of the data(after balancing). The reasons for this are outlined in the **Comparisons and Aside on Error** section. Our Logistic Regression model shows the following performance metrics when executed on a 10% testing dataset of images:

        """,
        unsafe_allow_html=True
    )

    try:
        image_path = "logistic_images/logistic_performance_metrics.png"  # Ensure the folder is named 'cnn_images'
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        image = Image.open(image_path)
        st.image(image, caption='Logistic Regression Performance Metrics', use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image {image_path}: {e}")

    # Create a table with metrics and values
    logistic_metrics = {
        "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
        "Value Before": [0.9243, 0.9217, 0.9013, 0.9114],
        "Value After": [0.9044, 0.9328, 0.9347, 0.9337]
    }
    df_logistic_metrics = pd.DataFrame(logistic_metrics)

    def table_to_html(df):
        return df.to_html(index=False, classes='contribution-table', escape=False)

    st.markdown("**Performance Metrics:**", unsafe_allow_html=True)
    st.markdown(table_to_html(df_logistic_metrics), unsafe_allow_html=True)

    # Explanations for each metric
    st.markdown(
        """
        We see from the metrics that the model achieved a very good performance on the test data before and after we balanced the dataset, with values scoring around 0.91 across all metrics. The interpretations of each metric are as follows:
        
        - **Accuracy**: Out of all predictions made by the model, 91% of predictions were correct classifications of the brain scan.
        - **Precision**: Averaged across each class, out of all positive predictions made by the model for that class, 91% of them were correct classifications of the brain scan.
        - **Recall**: Averaged across each class, out of all brain scans that were truly of that class, the model correctly classified them 91% of the time.
        - **F1 Score**: The high F1 score indicates a good balance between precision and recall. 
        """,
        unsafe_allow_html=True
    )

    st.markdown("**Additional Visualizations:**", unsafe_allow_html=True)

    # Define logistic regression carousel images
    logistic_carousel_images = [
        "logistic_images/log_roc_before.png",
        "logistic_images/log_confusion_before.png",
        "logistic_images/log_roc_after.png",
        "logistic_images/log_confusion_after.png"
    ]

    # Initialize session state for logistic carousel if not already set
    if 'logistic_carousel_index' not in st.session_state:
        st.session_state.logistic_carousel_index = 0

    logistic_total_images = len(logistic_carousel_images)

    # Display the current logistic regression image
    current_logistic_image_path = logistic_carousel_images[st.session_state.logistic_carousel_index]
    try:
        if not os.path.exists(current_logistic_image_path):
            raise FileNotFoundError(f"Image not found at path: {current_logistic_image_path}")
        current_logistic_image = Image.open(current_logistic_image_path)
        st.image(current_logistic_image, caption=os.path.basename(current_logistic_image_path), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image {current_logistic_image_path}: {e}")

    # Create three columns for navigation buttons (Previous, Spacer, Next)
    logistic_button_col1, logistic_button_col2, logistic_button_col3 = st.columns([1, 2, 1])

    with logistic_button_col1:
        pass  # Empty column for spacing

    with logistic_button_col2:
        # Previous Button
        if st.button("Previous (Logistic)", key="log_prev_button"):
            st.session_state.logistic_carousel_index = (st.session_state.logistic_carousel_index - 1) % logistic_total_images

    with logistic_button_col3:
        # Next Button
        if st.button("Next (Logistic)", key="log_next_button"):
            st.session_state.logistic_carousel_index = (st.session_state.logistic_carousel_index + 1) % logistic_total_images
    
    # Concluding paragraph
    st.markdown(
        """
        Above we see the ROC curve produced for each class, plotting true positive rate against false positive rate. 

The moderate dementia class had a near perfect area under the curve and the best performance, suggesting that the model was highly effective at identifying patients with moderate dementia. This is evident in the confusion matrix, where we see that there were no false negatives when examining moderately demented patients. For the other classes, they show poorer but still fair performance, with mildly demented patients with the second highest area under the curve followed by non-demented patients then finally patients with very mild dementia.

From the results, it is evident that the model is more effective at identifying certain stages of dementia than others in a pattern very similar to what we see in the logistic regression model. Based on the AOC values, the model can identify moderate and mild dementia relatively well with high sensitivity and specificity. It performs significantly worse with non-demented and very mildly demented patients, which is evident in the confusion matrix as the very mildly demented and nondemented cells show significant mispredictions; the model frequently classified nondemented patients as very mildly demented and very mildly demented patients as nondemented. This pattern makes sense, and similarly to the logistic regression model, we theorize that the pattern is related to magnitude of difference between various classes; non demented and very mildly dementia likely have a very low magnitude of difference between images while mild dementia and moderate dementia are both more distinct, resulting in a relatively higher misclassification rate for nondemented and very mildly demented compared to mild and moderate dementia. The model is likely under fitted for non demented and very mildly demented classes.

Note that this model was trained on a slightly modified dataset, the reasons for which we discuss in the next section.

        """,
        unsafe_allow_html=True
    )


    # SVM Regression Results & Discussion Subsection
    st.markdown('<div class="subsection-header" id="svm-results-discussion">SVM Results & Discussion</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        We chose to implement SVM because it can handle high dimension data, and separate different classes with clear margins. SVMs are also less prone to overfitting than neural networks, so we wanted to include the model in our project. Our SVM model shows the following performance metrics when executed on a 20% testing dataset of images:
        """,
        unsafe_allow_html=True
    )

    try:
        image_path = "svm_images/svm_performance_metrics.png"  # Ensure the folder is named 'cnn_images'
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        image = Image.open(image_path)
        st.image(image, caption='SVM Performance Metrics', use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image {image_path}: {e}")

    # Create a table with metrics and values
    svm_metrics = {
        "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
        "Value": [0.7646, 0.8463, 0.7646, 0.7858]
    }
    df_svm_metrics = pd.DataFrame(svm_metrics)

    def table_to_html(df):
        return df.to_html(index=False, classes='contribution-table', escape=False)

    st.markdown("**Performance Metrics:**", unsafe_allow_html=True)
    st.markdown(table_to_html(df_svm_metrics), unsafe_allow_html=True)

    # Explanations for each metric
    st.markdown(
        """
        We see from the metrics that the model achieved a fair performance on the test data, with values hovering between 0.75 and 0.85 across all metrics. The interpretations of each metric are as follows:
        
        - **Accuracy**: Out of all predictions made by the model, 76.46% of predictions were correct classifications of the brain scan.
        - **Precision**: Averaged across each class, out of all positive predictions made by the model for that class, 84.63% of them were correct classifications of the brain scan.
        - **Recall**: Averaged across each class, out of all brain scans that were truly of that class, the model correctly classified them 76.46% of the time.
        - **F1 Score**: The moderately high F1 score indicates a relatively good balance between precision and recall.
        """,
        unsafe_allow_html=True
    )

    st.markdown("**Additional Visualizations:**", unsafe_allow_html=True)

    # Define SVM images
    svm_carousel_images = [
        "svm_images/svm_roc.png",
        "svm_images/svm_confusion_matrix.png"
    ]

    # Use a unique session state for the SVM carousel
    if 'svm_carousel_index' not in st.session_state:
        st.session_state.svm_carousel_index = 0

    svm_total_images = len(svm_carousel_images)

    # Display the current image
    current_svm_image_path = svm_carousel_images[st.session_state.svm_carousel_index]
    try:
        if not os.path.exists(current_svm_image_path):
            raise FileNotFoundError(f"Image not found at path: {current_svm_image_path}")
        current_svm_image = Image.open(current_svm_image_path)
        st.image(current_svm_image, caption=os.path.basename(current_svm_image_path), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image {current_svm_image_path}: {e}")

    # Create two columns for navigation buttons
    svm_button_col1, svm_button_col2, svm_button_col3 = st.columns([1, 2, 1])

    with svm_button_col1:
        pass

    with svm_button_col2:
        if st.button("Previous (SVM)", key="svm_prev_button"):
            st.session_state.svm_carousel_index = (st.session_state.svm_carousel_index - 1) % svm_total_images

    with svm_button_col3:
        if st.button("Next (SVM)", key="svm_next_button"):
            st.session_state.svm_carousel_index = (st.session_state.svm_carousel_index + 1) % svm_total_images

    # Concluding paragraph
    st.markdown(
        """
        Above we see the ROC curve produced for each class, plotting true positive rate against false positive rate. 

The moderate dementia class had a near perfect area under the curve and the best performance, suggesting that the model was highly effective at identifying patients with moderate dementia. This is evident in the confusion matrix, where we see that there were no false negatives when examining moderately demented patients. For the other classes, they show poorer but still fair performance, with mildly demented patients with the second highest area under the curve followed by non-demented patients then finally patients with very mild dementia.

From the results, it is evident that the model is more effective at identifying certain stages of dementia than others in a pattern very similar to what we see in the logistic regression model. Based on the AOC values, the model can identify moderate and mild dementia relatively well with high sensitivity and specificity. It performs significantly worse with non-demented and very mildly demented patients, which is evident in the confusion matrix as the very mildly demented and nondemented cells show significant mispredictions; the model frequently classified nondemented patients as very mildly demented and very mildly demented patients as nondemented. This pattern makes sense, and similarly to the logistic regression model, we theorize that the pattern is related to magnitude of difference between various classes; non demented and very mildly dementia likely have a very low magnitude of difference between images while mild dementia and moderate dementia are both more distinct, resulting in a relatively higher misclassification rate for nondemented and very mildly demented compared to mild and moderate dementia. The model is likely under fitted for non demented and very mildly demented classes.

Note that this model was trained on a slightly modified dataset, the reasons for which we discuss in the next section.

        """,
        unsafe_allow_html=True
    )

    # Comparison Results & Discussion Subsection
    st.markdown('<div class="subsection-header" id="comparison-results-discussion">Comparison and an Aside on Error</div>', unsafe_allow_html=True)
    st.markdown(
        """
        Before continuing with our analysis, we would like to note that after obtaining results for the CNN, we sought explanations for the causes of the highly accurate performance. We investigated data leakage as a possible cause, but we see from the image divisions  below that there was no leakage.
        """,
        unsafe_allow_html=True
    )

    try:
        image_path = "comparison_images/leakage_investigation.png"  # Ensure the folder is named 'cnn_images'
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path: {image_path}")
        image = Image.open(image_path)
        st.image(image, caption='Leakage Investigation', use_container_width=True)
    except Exception as e:
        st.error(f"Error loading image {image_path}: {e}")

    st.markdown(
        """
        We noticed that the dataset was highly skewed toward nondemented images, with the class containing 137 times more images than the smallest class. This would explain the highly accurate performance, wherein the other classes are “drowned out” and the model is able to accurately predict most of the time. Hence, to control for this bias, we decided to train and test logistic regression and SVM on a smaller subset of the largest class to reduce the disparity. This had a notable effect on the final performance of both logistic regression and SVM. Thus, from this point on, we will compare logistic regression and SVM more directly since they were both trained on balanced datasets, and we will consider CNNs separately.
 
Overall, based purely on metrics, our initial prediction that CNN would perform the best was correct, followed by logistic regression, then SVM. Comparing the CNN with the other models, the CNN had significantly better performance, encroaching on nearly perfect accuracy. Even with the CNN being trained on a skewed dataset that boosted its accuracy, the degree to which it approached perfect reflects the strengths of CNNs’ learning mechanisms for image classification relative to other models. CNNs use hidden layers and are better at capturing complex patterns, details, and features, especially when it comes to classifying images that are filled with intricate details. Hence, this magnitude of difference between the CNN model and the other models makes sense.

Comparing the logistic regression and SVM, which were both trained on the balanced dataset, the logistic regression model had significantly better performance, encroaching on accuracy nearing 0.9 compared to 0.75 for the SVM mode. The poorer performance of the SVM was likely due to the use of a linear kernel that kept the data points linearly inseparable, producing a greater degree of misclassification. Additionally, both models had lower areas under the ROC curve for nondemented and very mild dementia classes, indicating that they both had the same problem with misclassifying very mild dementia as nondemented and nondemented as very mild dementia. This provides further evidence to support our theory that very mild dementia and nondemented images have very similar features.

As expected, the SVM and logistic regression models performed worse than the CNN model due to being trained on realistic, balanced data sets; however, their performance is not necessarily poor, with metrics hovering around 0.93 for the logistic regression model and 0.75-0.85 for the SVM model. When used to predict dementia on another separate dataset, we expect SVM and logistic regression to retain a greater degree of performance compared to the CNN. This is because being trained on a skewed dataset, CNN is less generalizable and is likely to experience a larger decline in performance when predicting on fresh testing data, whereas SVM and logistic regression will be more robust. If all three models were trained on the same balanced dataset, we hypothesize that CNNs would likely perform better than both logistic regression and SVM due to the levels of feature complexity learning that CNNs can achieve.

        """,
        unsafe_allow_html=True
    )


    # Next Steps Results & Discussion Subsection
    st.markdown('<div class="subsection-header" id="next-steps-results-discussion">Next Steps</div>', unsafe_allow_html=True)
    st.markdown(
        """
        We realized while implementing the SVM model that the near perfect performance of the first two models was likely a result of the skewed dataset we were working with. As we mentioned above, this was not corrected for in the CNN but was in the logistic regression and SVM model. In the future, it may be valuable to retrain our model on a completely separate, less skewed dataset and compare its performance to this dataset. We expect that metrics will decline for CNNs and logistic regression, but it will be much more realistic and accurate in practice. We also ran into problems with our computer performance not being able to handle the complexity of some models, specifically the SVM model. We ended up using SVC instead of SVM which definitely could have affected some performance. In the future, we can invest/borrow the school’s more powerful computers to train the model that will definitely be able to handle the large datasets. 
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
    st.image("gantt_chart.png", caption='Gantt Chart', use_container_width=True)

# Contribution Section 
def display_contributions(names):
    """
    Displays the Contributions section with two styled tables:
    1. Midpoint Contributions
    2. Proposal Contributions

    Args:
        names (list): List of team member names.
    """
    st.markdown('<div class="title" id="contributions">Contributions</div>', unsafe_allow_html=True)
    
    # Final Contributions
    st.markdown("#### <a id='final-contributions'></a>**Final Contributions**", unsafe_allow_html=True)

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
    st.sidebar.markdown("[Final Findings](#final-findings)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Introduction & Background](#introduction)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Problem Definition](#problem-definition)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Methods](#methods)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CNN Model](#cnn-model)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Logistic Regression Model](#logistic-regression-model)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SVM Model](#svm-model)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Results & Discussion](#results-discussion)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CNN Results & Discussion](#cnn-results-discussion)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Logistic Regression Results & Discussion](#logistic-results-discussion)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SVM Results & Discussion](#svm-results-discussion)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Comparison and an Aside on Error](#comparison-results-discussion)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Next Steps](#next-steps-results-discussion)")
    st.sidebar.markdown("[References](#references)")
    st.sidebar.markdown("[Gantt Chart](#gantt-chart)")
    st.sidebar.markdown("[Contributions](#contributions)")
    st.sidebar.markdown("&nbsp;&nbsp;&nbsp;[Final Contributions](#final-contributions)")
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

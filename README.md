
# Student Performance Analysis and Prediction Dashboard

This repository contains the code and resources for a project focused on analyzing student performance and building a predictive model to estimate final exam scores.

## Project Overview

This project is divided into several key phases:

1.  **Data Preparation:**
    * Loading and inspecting a large student performance dataset.
    * Cleaning the data by handling missing values and duplicates.
    * Converting categorical variables to appropriate data types.
2.  **Exploratory Data Analysis (EDA):**
    * Visualizing the distribution of numerical and categorical variables.
    * Performing correlation analysis to understand relationships between features.
    * Examining the relationship between study hours and exam scores.
    * Analyzing performance based on learning styles.
    * Investigating the impact of sleep and social media usage on exam scores.
3.  **Statistical Analysis:**
    * Conducting hypothesis testing to determine the effect of participation in discussions.
    * Performing ANOVA to compare exam scores across different learning styles.
    * Using a chi-squared test to analyze the relationship between learning styles and final grades.
4.  **Predictive Modeling:**
    * Preparing the data for machine learning by splitting it into training and testing sets.
    * Building and evaluating a Linear Regression model.
    * Building and evaluating a Random Forest Regressor model.
    * Performing feature importance analysis to identify key factors influencing exam scores.
5.  **Advanced Visualizations:**
    * Creating interactive plots using Plotly to enhance data exploration.
6.  **Findings and Report Creation:**
    * Compiling key findings and saving them in a text file.
7.  **Dashboard Creation:**
    * Creating a streamlit dashboard to predict student performance.

## Repository Contents

* `student_performance_large_dataset.csv`: The dataset used for analysis and modeling.
* `studentperformace.ipynb`: Jupyter Notebook containing the data analysis, modeling, and visualization code.
* `train_and_save_model.py`: Python script to train and save the Random Forest model.
* `finalapp.py`: Python script for the Streamlit dashboard.
* `outputs/`: Directory to store generated plots, models, and findings.
    * `plots/`: Contains saved plots (histograms, correlation matrix, scatter plots, etc.).
    * `models/`: Contains the saved machine learning models (`linear_regression_model.pkl`, `random_forest_model.pkl`, `rf_model.pkl`).
    * `interactive/`: Contains interactive plots generated with Plotly.
    * `key_findings.txt`: Text file summarizing the key findings of the analysis.
* `models/`: directory that will contain the saved model from train_and_save_model.py.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

2.  **Create a virtual environment (recommended):**
    python -m venv venv
   # Activate the virtual environment
   # For Windows:
   venv\Scripts\activate
   # For macOS/Linux:
   source venv/bin/activate

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a requirements.txt file, you can install the necessary libraries manually:

    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn plotly scipy streamlit joblib
    ```
    
4.  ***Navigate to project directory**
    cd Student_Performance_Prediction
    
5.  **Run the Jupyter Notebook:**

    ```bash
    jupyter notebook studentperformace.ipynb
    ```

6.  **To train and save the model run:**

    ```bash
    python TrainAndSaveModels.py
    ```

7.  **To run the Streamlit dashboard:**

    ```bash
    streamlit run finalapp.py
    ```

## Usage

1.  **Data Analysis and Modeling:**
    * Open and run the `studentperformace.ipynb` notebook to reproduce the analysis and modeling steps.
    * Ensure that you have ran the train_and_save_model.py file first, to generate the model that the streamlit app uses.
2.  **Dashboard:**
    * Run `streamlit run finalapp.py` to launch the dashboard.
    * Enter student data in the input fields.
    * Click the "Predict Final Score" button to see the predicted score and visualizations.

## Key Findings

The `outputs/key_findings.txt` file contains a summary of the key findings, including:

* Correlations between variables.
* Analysis of exam scores based on learning styles.
* Impact of participation in discussions.
* Analysis of exam scores based on study hours.
* Model performance metrics (R² scores).
* Top 5 most important features.

## Contributing

Contributions to this project are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License.

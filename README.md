# Development of an Open Source Automated Valuation Model (AVM) for Property Prices

## Overview

This project is focused on developing an open-source Automated Valuation Model (AVM) for property prices, which incorporates energy efficiency upgrades. The AVM is designed to predict property prices by considering a variety of factors, including traditional property features and energy efficiency metrics. The model is built using advanced machine learning techniques, with the goal of providing accurate and transparent property valuations.

## Project Structure

The project is organized into several key sections:

- **Data Preparation and Cleaning:** This section handles the loading, cleaning, and preprocessing of raw property data. It involves removing duplicates, handling missing values, and feature engineering.
- **Exploratory Data Analysis (EDA):** Here, various statistical and visual analyses are performed to understand the data distribution and relationships between features.
- **Modeling:** This section includes the selection, implementation, and evaluation of multiple machine learning models such as Linear Regression, Decision Tree, Random Forest, and Gradient Boosting.
- **Model Evaluation and Comparison:** The performance of each model is assessed using metrics like RMSE, MAE, and R². The best-performing model is selected based on a comparative analysis.
- **Benchmarking:** The final model is benchmarked against industry standards like RightMove and Zoopla to evaluate its real-world applicability.
- **App Development:**  The predictions from the model is implemented within a Streamlit-powered web application, allowing end-users to interactively see predicted property prices and other important features.

## Setup and Prerequisites

To set up the project locally, you'll need the following:

### Prerequisites

- Python
- Java
- Apache Spark
- Jupyter Notebook
- PySpark
- Pandas, NumPy, Matplotlib, Seaborn
- SciPy
- Streamlit (for deployment)

### Project Code Files

The order of the files in the project is crucial for understanding the flow and structure of the code. The files should be used in the following sequence:

1. **AVM Code Part1**: This file contains the initial steps for data loading, cleaning, preprocessing, exploration, model training, and evaluation. It includes scripts for handling raw data and preparing it for analysis, as well as the implementation of various machine learning models and their respective evaluations.

2. **AVM Code Part2**: This file builds upon the prepared predicted data, focusing on merging the predictions with the data needed for display in the web app and benchmarking the selected model against industry standards.

3. **AVM Web App**: This file contains the App development scripts. The predicted data from the model developed in the previous steps are integrated into a web application using Streamlit, allowing users to interact with the property and their valuation.

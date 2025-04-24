🏦 German Credit Risk Analysis - Data Preprocessing & EDA
This project focuses on analyzing and preparing the German Credit Dataset for credit risk classification. It includes exploratory data analysis, preprocessing, unsupervised clustering, and supervised model training.

📄 Dataset Source
The dataset is sourced from Kaggle:
German Credit Data on Kaggle

It provides anonymized information about individuals applying for credit, such as demographic details and financial status.

📦 Requirements
Install dependencies with:

bash
Copy
Edit
pip install numpy pandas matplotlib seaborn scikit-learn xgboost
📊 Project Workflow
✔️ 1. Importing Libraries
All required libraries for data manipulation, visualization, clustering, and modeling are imported at the start.

✔️ 2. Data Loading & Cleaning
The dataset is read using pandas

Dropped redundant columns like Unnamed: 0

Missing values are handled appropriately

Categorical variables are encoded using LabelEncoder and frequency encoding

✔️ 3. Exploratory Data Analysis (EDA)
Visualized features like Saving accounts, Checking account, Housing, and Purpose

Used seaborn for bar plots and count plots to understand feature distributions

✔️ 4. From Unsupervised to Supervised
Since the dataset does not include explicit labels for "good" or "bad" credit risk:

🧠 KMeans Clustering (n_clusters=2) was applied to segment the data into two clusters.

These clusters were then used as pseudo-labels, allowing for supervised model training.

This approach leverages unsupervised learning to create a labeled dataset from unlabeled data.

✔️ 5. Model Training
After labeling via KMeans, we trained:

XGBoost Classifier

Random Forest Classifier

Both models were evaluated using accuracy scores and classification reports.

📌 Key Insight
By converting an unsupervised problem into a supervised one using KMeans, we were able to apply powerful classifiers like XGBoost and Random Forest — even in the absence of true labels.

🙌 Acknowledgments
Dataset: [German Credit Data - Kaggle](https://www.kaggle.com/datasets/uciml/german-credit)

# 🏦 German Credit Risk Classification (Kaggle Dataset)

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Made with 💡](https://img.shields.io/badge/Made%20with-%F0%9F%92%A1-blueviolet)](#)

A machine learning project to predict **credit risk** using the **German Credit Data** from Kaggle. This repo covers data preprocessing, exploratory data analysis, unsupervised clustering (KMeans), and supervised classification models like **XGBoost** and **Random Forest**.

---

## 📁 Dataset

Dataset used: [German Credit Data - Kaggle](https://www.kaggle.com/datasets/uciml/german-credit)

This dataset contains anonymized information about customers applying for credit, including demographics, account status, and financial history.

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/german-credit-risk.git
cd german-credit-risk
pip install -r requirements.txt
```

📊 Project Workflow
✅ 1. Data Loading & Cleaning
Loaded the CSV dataset

Dropped unnecessary columns (e.g., Unnamed: 0)

Handled missing values

Encoded categorical variables with LabelEncoder & frequency encoding

✅ 2. Exploratory Data Analysis (EDA)
Visualized feature distributions using bar plots and count plots

Key features analyzed: Saving accounts, Checking account, Purpose, Housing, etc.

✅ 3. Unsupervised to Supervised Conversion
Since the dataset lacks explicit labels for creditworthiness:

Applied KMeans Clustering with n_clusters=2 to segment data

Cluster assignments were used as pseudo-labels

This allowed us to apply supervised learning methods on an originally unlabeled dataset

✅ 4. Model Training
Trained the following supervised models on the KMeans-labeled data:

🌲 Random Forest Classifier

⚡ XGBoost Classifier

Evaluation was done using accuracy, classification report, and confusion matrix.

📌 Key Insight
We transformed an unlabeled credit risk dataset into a supervised classification problem using KMeans, unlocking the ability to train powerful models like XGBoost and Random Forest.

🙏 Acknowledgments
Dataset: German Credit Data - Kaggle

Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, xgboost

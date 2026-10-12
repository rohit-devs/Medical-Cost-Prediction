<div align="center">

# 🏥 Medical Insurance Cost Prediction

**Estimate an individual's medical insurance charges with Machine Learning, served through a Flask web app.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Random%20Forest-F7931E?logo=scikitlearn&logoColor=white)
![Status](https://img.shields.io/badge/Purpose-Educational-orange)

<img src="https://github.com/SahilChachra/Medical-Cost-Prediction/blob/master/sampleImages/doc.gif?raw=true" alt="Demo of the Medical Insurance Cost Prediction app" width="750">

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Dataset](#-dataset)
- [Analysis and Screenshots](#-analysis-and-screenshots)
- [Model Results](#-model-results)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Disclaimer](#-disclaimer)
- [Author and Attribution](#-author-and-attribution)

---

## 📌 Overview

This project estimates medical insurance charges from six personal factors: **age, sex, BMI, number of children, smoking status, and region**.

It covers the full workflow: exploring the data, comparing regression algorithms, tuning the best model, saving it, and serving predictions through a Flask web interface.

**Motivation:** to understand how personal characteristics influence insurance costs, and to turn that analysis into a usable predictive application.

## ✨ Features

- 📊 Exploratory Data Analysis (EDA) with correlation heatmaps and plots
- 🧹 Data preparation and categorical feature encoding
- 📈 Skewness and kurtosis analysis
- 🤖 Model comparison: Linear Regression, SVR, Ridge Regression, Random Forest Regressor
- ⚙️ Hyperparameter tuning of the best model
- 💾 Trained model saved with Pickle
- 🌐 Flask web app: enter details, get an estimated cost

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Pandas, NumPy | Data manipulation and numerical computing |
| Matplotlib, Seaborn | Visualization |
| Scikit-learn | Modeling and evaluation |
| Flask | Web application |
| HTML & CSS | User interface |
| Pickle | Model persistence |

## 📂 Project Structure

```text
Medical-Cost-Prediction/
├── app.py                        # Flask application
├── insurance.csv                 # Dataset
├── rf_tuned.pkl                  # Trained Random Forest model
├── requirements.txt              # Python dependencies
├── Medical Cost Insurance.ipynb  # EDA, training, tuning
├── templates/
│   ├── home.html                 # Input form
│   └── op.html                   # Prediction output
├── static/                       # CSS and assets
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/rohit-devs/Medical-Cost-Prediction.git
cd Medical-Cost-Prediction
```

### 2. Create and activate a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Open **http://127.0.0.1:5000/** in your browser.

## 💡 Usage

1. Open the home page.
2. Enter **age**, **sex**, **BMI**, **number of children**, **smoker status**, and **region**.
3. Submit the form to see the estimated insurance charge.

## 📊 Dataset

[Medical Cost Personal Dataset on Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance)

| Column | Description |
|---|---|
| `age` | Age of the primary beneficiary |
| `sex` | Gender of the beneficiary |
| `bmi` | Body mass index |
| `children` | Number of dependents covered |
| `smoker` | Smoking status |
| `region` | Residential region |
| `charges` | Medical insurance charges (**target**) |

## 📉 Analysis and Screenshots

### Correlation Heatmap

![Correlation Heatmap](https://github.com/SahilChachra/Medical-Cost-Prediction/blob/master/sampleImages/Cor.png?raw=true)

### Age vs. Insurance Charges

![Age vs Charges](https://github.com/SahilChachra/Medical-Cost-Prediction/blob/master/sampleImages/AgevsCharges.png?raw=true)

### Application

| Input form | Prediction |
|---|---|
| <img src="https://github.com/user-attachments/assets/e6c00b4e-45a5-4590-8f37-a2902d93c649" alt="Application screenshot 1" width="420"> | <img src="https://github.com/user-attachments/assets/a11a1007-80a8-452a-9929-21144ee824ca" alt="Application screenshot 2" width="420"> |

## 📈 Model Results

The original project reports roughly **86% accuracy** for the tuned Random Forest Regressor. For a regression task this most likely refers to the **R² score**, and it has not been independently re-verified here.

To evaluate properly, rerun the notebook and report:

| Metric | Value |
|---|---|
| R² | _fill in after rerunning_ |
| MAE | _fill in after rerunning_ |
| RMSE | _fill in after rerunning_ |

## 🧯 Troubleshooting

| Problem | Fix |
|---|---|
| `pip install` fails on old pinned versions | Install versions compatible with your Python, or relax the pins in `requirements.txt` |
| Error loading `rf_tuned.pkl` (version mismatch) | Pickles are tied to the scikit-learn version that created them. Retrain with the notebook and re-save the model |
| `Activate.ps1` blocked on Windows | Run `Set-ExecutionPolicy -Scope Process RemoteSigned`, then activate again |
| Port 5000 already in use | Change the port in `app.py`, e.g. `app.run(port=5001)` |

## 🔮 Roadmap

- [ ] Modernize the UI with a responsive orange-and-white design
- [ ] Improve input validation and error handling
- [ ] Reproducible training pipeline (script plus pinned versions)
- [ ] Show evaluation metrics (R², MAE, RMSE) in the app
- [ ] Add automated tests
- [ ] Add deployment configuration and deploy to a cloud platform

## ⚠️ Disclaimer

This project is for **educational and demonstration purposes only**. Predictions are estimates and are not official insurance quotes, financial advice, or medical advice.

## 👨‍💻 Author and Attribution

Maintained by [Rohit D. Mohotkar](https://github.com/rohit-devs).

This repository is based on the original [Medical-Cost-Prediction](https://github.com/SahilChachra/Medical-Cost-Prediction) project by Sahil Chachra. Original attribution and applicable license terms are preserved.

---

<div align="center">

Made with ❤️ using Python, Machine Learning, and Flask.

</div>

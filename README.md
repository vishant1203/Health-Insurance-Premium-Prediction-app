# 🏥 Predictive Health Insurance Premium Model  

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)  
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen.svg)   

A machine learning project to predict **health insurance premiums** based on factors like **age, BMI, smoking habits, and medical history**.  

🔗 **Live Demo** → [Health Insurance Premium Calculator](https://health-insurance-premium-calculation.streamlit.app/)  

---

## 📚 Table of Contents  
- [Project Overview](#project-high-level-overview)  
- [Business Process Evolution](#business-process-evolution)  
  - [Before IT Systems (~2008)](#before-it-systems--2008)  
  - [After IT Systems (~2009 onwards)](#after-it-systems--2009-onwards)  
  - [Machine Learning Era (~2015 onwards)](#current-approach-machine-learning-era-2015-onwards)  
- [Objectives](#objectives)  
- [Key Features](#key-features)  
- [Tech Stack](#tech-stack)  
- [Live Demo](#live-demo) 

---

## 📌 Project High Level Overview  
This project was developed for **Shield Insurance** by **AtliQ AI** with the objective of building a predictive model that can accurately estimate health insurance premiums.  

The solution has two phases:  
- **Phase 1 (MVP)** – Build and deploy a predictive model with a Streamlit application.  

---

## 📌 Business Process Evolution  

### 📄 Before IT Systems – ~2008  
1. Applicant fills out a **paper application**.  
2. Insurance agent submits the application & documents.  
3. Imaging team scans the paper form into the system.  
4. Data entry team manually creates an application in the internal system.  
5. Underwriter reviews the application → approves or rejects.  
6. Fulfillment team prints and mails the result to the applicant.  

💡 **Premium Calculation in this Era**  
- Done manually by **actuaries** and underwriters.  
- Based on **mortality/morbidity tables**, historical claims, and simple statistical methods.  
- Premiums were **rule-of-thumb**, not automated.  

---

### 💻 After IT Systems – ~2009 onwards  
1. Applicant submits application via **website/online portal**.  
2. Underwriter reviews the application → approves or rejects.  
3. Results are **emailed** to the applicant.  

💡 **Premium Calculation in this Era**  
- Early **rule-based systems** inside IT platforms.  
- Example: Smoker → +40%, High BMI → +25%.  
- Later, **Generalized Linear Models (GLMs)** were widely adopted.  
- GLMs were **regulator-friendly, explainable, and industry standard**.  

**Example Formula:**  
--Premium = Base Rate + β1(Age) + β2(Smoker) + β3(BMI) + β4(Pre-existing condition)

---

### 🤖 Current Approach (Machine Learning Era – 2015 onwards)  
With machine learning, insurers can:  
- Use **large datasets** (demographics, lifestyle, medical history, IoT, wearables).  
- Apply **non-linear algorithms** (XGBoost, Random Forest, Neural Nets).  
- Achieve **higher accuracy** and more personalized pricing.  

💡 **In this Project**  
- Built a predictive ML model for health insurance premiums.  
- Deployed as a **Streamlit app** for real-time use by underwriters.  

---

## 🎯 Objectives  
- Achieve **>97% accuracy** in premium prediction.  
- Ensure **95% of predictions** fall within **±10% error**.  
- Provide an **interactive Streamlit app** for instant predictions.  

---

## ⚙️ Key Features  
- Data preprocessing & EDA on insurance datasets.  
- Training & optimization of ML models.  
- Interactive **Streamlit web app** for premium calculation.  
- Cloud deployment → accessible from anywhere.  

---

## 🛠️ Tech Stack  
- **Python**  
- **Scikit-learn / XGBoost / RandomForest**  
- **Pandas, NumPy, Matplotlib, Seaborn**  
- **Streamlit** (deployment & UI)  

---

## ⚡Live Demo
https://health-insurance-premium-calculation.streamlit.app/

*Try out the model directly here →* [Health Insurance Premium Calculator](https://health-insurance-premium-calculation.streamlit.app/)
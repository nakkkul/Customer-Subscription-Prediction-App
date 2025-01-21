## Customer Subscription Prediction Web Application

### 📜 Overview
The Customer Subscription Prediction Web App is a machine learning-powered tool that helps determine the likelihood of a customer subscribing based on input data. Built with Flask and a robust predictive model, the application provides instant insights to aid targeted marketing and customer engagement strategies. The app is deployed on Render, ensuring accessibility and seamless integration with business workflows.

### 🎯 Purpose
This project aims to simplify subscription prediction through a user-friendly web interface. By leveraging machine learning, it assists businesses in identifying potential customers more efficiently, optimizing marketing efforts, and improving customer acquisition rates.

### 🚀 Key Features
- **Instant Predictions:** Users can input customer details and receive real-time subscription likelihood predictions.
- **Machine Learning Model:** A high-accuracy predictive model trained to distinguish between potential subscribers and non-subscribers.
- **User-Friendly Interface:** A minimalistic HTML-based UI that ensures ease of use.
- **Cloud Deployment:** Hosted on Render for stability and wide accessibility.
- **Performance Metrics:** Achieves strong classification performance with a test accuracy of 90.3% and an ROC AUC score of 0.93.

### 🏗️ Project Architecture
- **Frontend:** HTML for a simple and intuitive input interface.
- **Backend:** Flask handles request processing and model inference.
- **Model Integration:** A trained machine learning model processes user inputs and generates predictions.
- **Hosting:** The app is deployed on Render, allowing users to access it online without setup hassles.

### 📊 Model Performance
- **Test Accuracy:** 90.3%
- **ROC AUC Score:** 0.93
- **Optimizations:** Applied feature engineering and hyperparameter tuning to enhance model efficiency.

### 📸 Interface Preview
![App Interface](./images/inter.png)

### ⚙️ Setup Instructions

**Prerequisites:**
Ensure that your system has the following installed:
- Python 3.7+
- pip (Python package manager)

#### Installation Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/nakkkul/Customer-Subscription-Prediction-App.git
   cd Customer-Subscription-Prediction-App
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
4. **Access the web app:**
   Open your browser and go to `http://127.0.0.1:5000`.

### 🌐 Live Deployment
Try the live version here: [Customer Subscription Prediction App](https://customer-subscription-prediction-app.onrender.com)

### 📂 Repository Structure
```
Customer-Subscription-Prediction-App/
│
├── app.py               # Flask application
├── model/               # Trained model and preprocessing scripts
├── static/              # CSS and other static assets
├── templates/           # HTML templates
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation
```

### 🔮 Future Enhancements
- Expanding the dataset for better model generalization.
- Implementing an API to integrate predictions into external systems.
- Adding visualization features for better customer insights.

### 🤝 Acknowledgments
A special thanks to open-source datasets and machine learning frameworks that made this project possible, including scikit-learn and Flask.

*Cumulative research comparing machine learning models on breast cancer classification(bengin, malignant, normal) without using regions of interests(ROI) which are often used in breast cancer classification*

# Paper linked below: 

https://www.linkedin.com/in/krishbadri/overlay/1746309580828/single-media-viewer/?profileId=ACoAADRpDbUBEGPHO37bSNhW4jKnYFjgw8Uji6g

# **Breast Cancer Classification with Machine Learning**  
🎓 *Spring 2024 Research Project*  
📍 *By Krish Badri, Leah Parparov, and Jeffrey Xie*  

---

## **📜 Abstract**
This project explores the efficacy of **Scikit-Learn** machine learning models for classifying breast cancer from **ultrasound images** without regions of interest (ROI) masks. Designed for **resource-limited settings**, our research evaluates five classifiers—**Logistic Regression**, **MLP Classifier**, **Support Vector Classifier**, **Random Forest**, and **Gradient Boosting**—on a dataset of 780 images.  
- **Best Model**: Random Forest  
- **Accuracy**: 78.43%  
- **AUC-ROC**: 0.86  

Our findings highlight the potential of simpler ML frameworks for affordable, accessible diagnostic tools in underserved medical regions.

---

## **📂 Dataset**  
- **Source**: 780 ultrasound images labeled as **normal**, **benign**, or **malignant**.  
- **Preprocessing**:
  - Cropped and resized to **300x300 pixels**.  
  - Converted to grayscale for simplicity.  
  - Labels numerically encoded:  
    - `0 = Benign`  
    - `1 = Malignant`  
    - `2 = Normal`  

---

## **⚙️ Methodology**
- **Models Tested**:
  1. Logistic Regression  
  2. MLP Classifier (Neural Network)  
  3. Support Vector Classifier  
  4. Random Forest  
  5. Gradient Boosting  

- **Evaluation Metrics**:
  - Accuracy  
  - Precision  
  - Recall  
  - F1 Score  
  - ROC-AUC  

- **Techniques**:
  - **5-Fold Cross-Validation** to address overfitting.  
  - **Confusion Matrices** and **ROC Curves** for visualization.  

---

## **🔍 Key Results**
| Model                 | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|-----------------------|----------|-----------|--------|----------|---------|
| Random Forest         | 78.43%  | 75.37%    | 74.50% | 73.69%   | 0.86    |
| MLP Classifier (NN)   | 74.50%  | 84.25%    | 74.50% | 74.36%   | 0.72    |
| Logistic Regression   | 72.00%  | 73.49%    | 72.00% | 70.48%   | 0.77    |
| Support Vector Machine| 71.50%  | 72.30%    | 71.50% | 69.62%   | 0.84    |
| Gradient Boosting     | 72.00%  | 73.18%    | 72.00% | 70.65%   | 0.84    |

**Visualizations**:  
- **Confusion Matrices** for each model.  
- **ROC Curve** comparing classifier performance.  

---

## **🌟 Highlights**
- **Impact**: Developed for **underserved regions** lacking ROI capabilities and advanced computational resources.  
- **Future Improvements**:
  - Addressing class imbalance using **SMOTE**.  
  - Exploring deeper frameworks like **PyTorch** or **TensorFlow**.  
  - Adding contextual patient data for enhanced predictive capabilities.  

---

## **🛠️ Technologies Used**
- **Languages**: Python  
- **Libraries**: Scikit-Learn, NumPy, Pandas, Matplotlib  

---

## **👥 Team Contributions**
- **Jeffrey Xie**: Random Forest, Logistic Regression, and MLP implementations; K-Fold algorithm; results analysis and visualizations; abstract and discussion writing.  
- **Leah Parparov**: Literature review; ethical analysis; conclusion writing.  
- **Krish Badri**: SVM and Gradient Boost implementations; introduction; LaTeX formatting.  

---

## **📈 Repository Contents**
- **`/data`**: Dataset files and preprocessing scripts.  
- **`/models`**: Code for training and evaluating the five classifiers.  
- **`/results`**: ROC curves, confusion matrices, and model performance metrics.  

---

## **📫 Contact**
For inquiries, reach out at **kbadri2@illinois.edu**.  


# 🏠 California House Price Predictor

This is a **Streamlit-based web app** that uses a **Linear Regression model** trained on the official [California Housing Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) to predict the **median house price** for a location in California based on multiple real-world factors.

🔗 **Live App**: [https://california-house-price-predictor-minimal-version.streamlit.app/](https://california-house-price-predictor-minimal-version.streamlit.app/)

## 📌 Features

- ✅ Real-world dataset (from Scikit-learn)
- ✅ Custom-trained Linear Regression model (no libraries like `sklearn.linear_model`)
- ✅ User-friendly input interface with clear feature descriptions
- ✅ Automatic input normalization using training-time statistics
- ✅ Predictions only appear after clicking the **Predict** button
- ✅ Fully deployed on Streamlit Cloud

## 📊 Model Inputs

| Feature | Description |
|--------|-------------|
| Median Income | Median income in block (in 10k USD) |
| House Age | Median age of houses in the block |
| Ave Rooms | Average number of rooms per household |
| Ave Bedrooms | Average number of bedrooms per household |
| Population | Block population |
| Ave Occupancy | Average number of household members |
| Latitude | Geographic latitude |
| Longitude | Geographic longitude |

## 🔮 Output

The app predicts **Median House Value** in **100,000s of USD**.  
For example, a prediction of `$2.35` means approximately **$235,000**.

## 🧠 How the Model Works

- Trained using **pure Python + NumPy** (no sklearn training)
- Features are normalized using training set statistics
- Learned weights and bias are hardcoded into the app for prediction
- Evaluation metrics:
  - 📉 RMSE: **0.7437**
  - 📈 R² Score: **0.5847**

## 📂 Files

- `streamlit_app.py` – Streamlit app code
- `README.md` – Project overview
- `requirements.txt` – Python dependencies

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
````

## 👨‍💻 Author

**Shivam Rathod**

* 🔗 GitHub: [@shivamr021](https://github.com/shivamr021)
* 💼 LinkedIn: [@shivamrathod021](https://www.linkedin.com/in/shivamrathod021)

---


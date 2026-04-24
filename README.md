# 🍎 AAPL Stock Dashboard

An interactive stock dashboard built with **Python** and **Streamlit** to analyze Apple Inc. (AAPL) stock performance from 2016 to 2026.

---

## 📸 Preview

> A clean, interactive dashboard with yearly filters, metric cards, and price/volume charts.

---

## 📊 Features

- 🗓️ **Year Filter** — Explore stock data by a specific year (2016–2026)
- 📈 **Metric Cards** — Max High, Min Low, and Highest Close for the selected year
- 📉 **Line Chart** — Daily High price trend for the selected year
- 📊 **Bar Chart** — Daily trading volume for the selected year
- 📋 **Raw Data Toggle** — View the underlying data with a checkbox
- ⬇️ **CSV Download** — Export the full dataset directly from the dashboard
- 📌 **About Section** — Dataset info, column descriptions, date coverage and tools used

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Pandas** | Data loading and manipulation |
| **Streamlit** | Dashboard framework and visualizations |

---

## 📁 Project Structure

```
aapl-dashboard/
├── app.py                 # Main Streamlit dashboard
├── aapl_cleaned.csv       # Cleaned AAPL stock data
├── analysis.ipynb         # Data cleaning and analysis notebook
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/bedahmilton/your-repo.git
cd your-repo
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## 📦 Key Dependencies

```
streamlit
pandas
```

> Full dependency list available in `requirements.txt`

---

## 📅 Dataset

| Field | Details |
|-------|---------|
| **Ticker** | AAPL (Apple Inc.) |
| **Exchange** | NASDAQ |
| **Currency** | USD |
| **Data Range** | 2016 – 2026 |
| **Frequency** | Daily |
| **Source** | Yahoo Finance |

---

## 🧹 Data Cleaning

Data was cleaned and prepared in [`analysis.ipynb`](analysis.ipynb). The notebook covers:

- Loading raw AAPL data from Yahoo Finance
- Handling multi-level column headers
- Parsing date index to datetime format
- Exporting the cleaned dataset as `aapl_cleaned.csv`

---

## 👤 Author

**Milton Bedah**

- 🐙 GitHub: [bedahmilton](https://github.com/bedahmilton)
- 📧 Email: bedah.dev@gmail.com

---

## 📄 License

© 2026 Milton Bedah. All Rights Reserved.

> Data sourced from Yahoo Finance. For educational purposes only.
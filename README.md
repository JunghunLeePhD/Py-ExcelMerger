---
title: Excel Manipulator
emoji: 📊
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 6.5.1
app_file: app.py
pinned: false
---

# 📊 Excel Manipulator (Web App)

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Open%20in%20Spaces-blue)](https://huggingface.co/spaces/JunghunleePhD/Py-ExcelManipulator)

A powerful, user-friendly web application to **merge, group, and aggregate** multiple Excel files automatically. Built with **Python** and **Gradio**, it replaces the legacy command-line tool with a modern graphical interface.

## 🚀 Features

* **📂 Batch Processing:** Upload multiple Excel files (`.xlsx`, `.xls`) at once.
* **🔗 Auto-Merge:** Automatically combines all uploaded files into a single dataset.
* **🧠 Smart Aggregation:**
    * **Numeric Columns:** Automatically **Sums** the values (e.g., Sales, Hours).
    * **Text Columns:** Automatically finds the **Mode** (Most Frequent Value).
* **🖱️ Interactive UI:** Select your "Grouping ID" and "Data Columns" using simple checkboxes and dropdowns.
* **⚡ Fast & Secure:** Processes data efficiently using Pandas and handles multiple users safely with temporary file isolation.
* **⬇️ Export:** Download your summarized report as a CSV file immediately.

---

## 🌐 Live Demo

Try the app directly on Hugging Face Spaces:
**[👉 Click here to open Excel Manipulator](https://huggingface.co/spaces/JunghunleePhD/Py-ExcelManipulator)**

---

## 🛠️ Installation (Run Locally)

If you prefer to run the app on your own computer instead of the cloud, follow these steps.

### **Prerequisites**
* Python 3.10 or higher
* Git

### **1. Clone the Repository**

```bash
git clone [https://github.com/JunghunLeePhD/Py-ExcelManipulator.git](https://github.com/JunghunLeePhD/Py-ExcelManipulator.git)
cd Py-ExcelManipulator
```

### **2. Set Up Virtual Environment (Recommended)**

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

```bash
# Windows
python -m venv venv
venv\Scripts\activate
```


### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run the App**

```bash
python app.py
```

The app will launch in your browser at: `http://127.0.0.1:7860`

## **📖 How to Use**

1. **Upload Files:** Drag and drop your Excel files into the upload box.

1. **Select Columns to Aggregate:** Check the boxes for the data you want to analyze (e.g., "Amount", "Category").

1. **Select Grouping ID:** Choose the unique identifier to group by (e.g., "EmployeeID", "Email").

- *Note: The dropdown automatically filters based on your checkbox selections.*


1. **Process:** Click the **"Process Files 🚀"** button.

1. **Download:** Preview the result on the right and click **"Download CSV"** to save it.


## **☁️ Deployment**

This repository is configured for **Continuous Deployment** to Hugging Face Spaces using GitHub Actions.

- **Push to Main:** Any change pushed to the `main` branch will automatically trigger a rebuild of the Space.

- **Configuration:** The deployment logic is handled in `.github/workflows/sync_to_hub.yml`.


## **📦 Tech Stack**

- **Python:** Core logic.


- **Pandas:** High-performance data manipulation.


- **Gradio:** Web interface and interactivity.


- **OpenPyXL:** Excel file reading engine.


## **📜 License**

[MIT](https://www.google.com/search?q=LICENSE)

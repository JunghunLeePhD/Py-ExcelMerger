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

# 📊 Excel Manipulator

A Python-based command-line tool that automates the processing, merging, and aggregation of Excel data. It allows users to interactively select grouping columns and data columns to generate a summarized report.

## 🚀 Features

* **Batch Processing:** Automatically reads and merges all Excel files located in the `assets/` folder.
* **Interactive CLI:** Lists all available columns and allows the user to select them by ID.
* **Smart Aggregation:**
    * **Numeric columns:** Automatically sums the values.
    * **Text/Categorical columns:** Automatically calculates the mode (most frequent value).
* **Cross-Platform:** Works as a raw Python script or a compiled executable (macOS/Windows).

---

## **📖 User Guide (How to Run the App)**

**Follow these steps if you just want to use the tool without writing any code.**

### **1. Download the App**

1. On this GitHub page, look for the **Releases** section (usually on the right side).
2. Click on the latest version (e.g., `Release v10`).
3. Under **Assets**, download the file named **`ExcelManipulator_macOS`**.

### **2. Run the App (Important for Mac Users)**

Because this app is not signed by Apple, you must follow these steps the **first time** you open it:

1. **Right-click (or Control-click)** the `ExcelManipulator` file.
2. Select **Open** from the menu.
3. A warning will appear: *"macOS cannot verify the developer..."*. Click **Open** again.

- *Note: If you just double-click normally, macOS might block it. Use Right-click -> Open.*

### **3. How to Use**

1. **Run:** Open the `ExcelManipulator` app.
2. **Add Files:** Put your Excel files (`.xlsx` or `.xls`) inside the **`assets`** folder that came with the app.
3. **Select Columns:**
    - The app will list all columns found in your files.
    - Type the ID numbers of the columns you want.
    - *Example:* Type `0 4 5` to group by Column 0 and sum up Columns 4 and 5.
4. **Save:** When finished, type `y` to save. The result will be in the **`output`** folder.
---

## 🛠️ Installation & Setup (Development)

This project is developed using **Python 3.11**. Follow these steps to set up your local environment.

### 1. Clone the Repository

```bash
git clone git@github.com:JunghunLeePhD/Py-ExcelManipulator.git
cd Py-ExcelManipulator
```

### **2. Set up Virtual Environment**

It is recommended to use a virtual environment (`venv`) to manage dependencies.

**macOS / Linux:**

```bash
python3.11 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

## **📂 Usage**

### **1. Prepare Your Data**

1. The script looks for Excel files in the `./assets` folder.

2. If the folder doesn't exist, the script will create it for you.

3. Place your `.xlsx` or `.xls` files into `./assets/`.

### **2. Run the Script**

Ensure your virtual environment is activated, then run:

```bash
python main.py
```

### **3. Follow the Prompts**

1. **Column List:** The script will display all columns found in your Excel files.

2. **Selection:** Enter the indices of the columns you want to use.

    - **First Index:** This will be the "ID" or "Group By" column.


    - **Subsequent Indices:** These are the data columns to aggregate.


    - *Example:* Entering `0 3 5` will group by Column 0, and aggregate data from Column 3 and 5.

3. **Save:** Confirm `y` to save the result to `./output/result.csv`.

## **🤖 GitHub Actions & Releases**

This project uses **GitHub Actions** to automatically build the standalone macOS application. You do not need to install Python to run the release version.

### **1. Trigger the Build**

1. Go to the **Actions** tab in this repository.
2. Select **Build macOS App** from the left sidebar.
3. Click the **Run workflow** dropdown button.
4. Select the branch (usually `main`) and click **Run workflow**.

### **2. Download the App**

1. Wait for the action to complete (approx. 2-5 minutes).
2. Go to the **Releases** section (on the right sidebar of the main code page).
3. Download the latest asset: `ExcelManipulator_macOS.zip`.

### **3. Run on macOS (Important)**

Because this app is not signed by Apple, you must follow these steps to open it:

1. **Unzip** the downloaded file.
2. Open the `ExcelManipulator` folder.
3. **Right-click (Control-click)** the `ExcelManipulator` executable (black icon).
4. Select **Open** from the context menu.
5. A dialog will appear saying *"macOS cannot verify the developer..."*. Click **Open** again.

- *Note: If you just double-click normally, macOS may block the app entirely. You only need to do the Right-click step once.*


## **📦 Building Locally (Optional)**

If you want to build the executable yourself instead of using GitHub Actions:

### **Build Command**

You can convert this script into a standalone application using **PyInstaller**.

### **1. Install PyInstaller**

```bash
pip install pyinstaller
```

### **2. Build the App**

Run the following command in your terminal (ensure `venv` is active):

```bash
pyinstaller --noconfirm --onedir --clean --name "ExcelManipulator" main.py
```

- `--onedir`: Creates a folder distribution (starts up faster than `--onefile`).
- `--clean`: Clears PyInstaller cache.
- `--name`: Sets the output name.

### **Running the Built App (macOS)**

1. Go to the `dist/ExcelManipulator` folder.
2. Ensure the `assets` folder exists inside `dist/ExcelManipulator/` (or create it and add your Excel files there).
3. Run the executable:

```bash
./dist/ExcelManipulator/ExcelManipulator
```

## **📁 Project Structure**

```plaintext
.
├── main.py                # Main application script
├── lib/
│   ├── __init__.py
│   └── utils.py           # Helper functions (show, creat_folder, read_excel_files)
├── assets/                # Input folder for Excel files (auto-created)
├── output/                # Output folder for CSV results (auto-created)
└── README.md
```

## **⚠️ Common Issues**

**1. "No data found" Error:** Ensure your Excel files are actually inside the `assets` folder relative to where you are running the script.

**2. Permission Denied on macOS:** If the executable doesn't run, you may need to grant it execution rights:

```bash
chmod +x dist/ExcelManipulator/ExcelManipulator
```

## **📜 License**

[MIT](https://choosealicense.com/licenses/mit/)

# Health-an-fitness-Tracker

Here’s a complete **README.md** content for your GitHub repository for the **Health & Fitness Tracker** project:

---

# 🏃‍♂️ Health & Fitness Tracker

A simple full-stack project that helps users track their daily health metrics like **steps**, **calories**, and **sleep hours**, using a web-based form built with **HTML/CSS**, a **Python Flask** backend, and a **MySQL** database. The project also includes a chart-reporting module using **Matplotlib** for data visualization.

---

## 📌 Features

* 📅 Log daily health metrics
* 📊 View visual trends using graphs
* 🐍 Backend powered by Flask (Python)
* 🗃 Data stored in MySQL database
* 💻 Clean and responsive web UI
* 🔒 Local deployment, no internet required

---

## 🚀 Technologies Used

| Layer    | Technologies           |
| -------- | ---------------------- |
| Frontend | HTML, CSS              |
| Backend  | Python (Flask)         |
| Database | MySQL, MySQL Connector |
| Charting | Matplotlib             |
| IDE      | VS Code / PyCharm      |

---

## 🏗️ Project Structure

```
health-fitness-tracker/
├── index.html          # Frontend Form
├── style.css           # Form styling
├── submit.py           # Flask backend to handle form & store data
├── report.py           # Data reporting and visualization
├── requirements.txt    # Python dependencies
└── README.md           # Project Documentation
```

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites

* Python 3.x installed
* MySQL server installed
* Git & a code editor (VS Code recommended)

### 📥 Step-by-Step Setup

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/health-fitness-tracker.git
cd health-fitness-tracker
```

2. **Install Python Dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up MySQL Database**

```sql
CREATE DATABASE health_tracker;
USE health_tracker;
CREATE TABLE records (
  id INT AUTO_INCREMENT PRIMARY KEY,
  date DATE,
  steps INT,
  calories INT,
  sleep_hours FLOAT
);
```

4. **Run the Flask App**

```bash
python submit.py
```

Open your browser and go to:
👉 `http://127.0.0.1:5000`

5. **View Report Graphs**

```bash
python report.py
```

---

## 🖼️ Screenshots

> ![Form Screenshot](screenshots/form.png)
> ![Chart Screenshot](screenshots/chart.png)

---

## 📈 Sample Output Graph

* X-axis: Dates
* Y-axis: Metrics (steps, calories, sleep)
* Shows daily progress and trends.

---

## 🧪 Testing

* Tested form input with valid/invalid values
* Verified database insertion using MySQL Workbench
* Charts tested for multiple record types and timelines

---

## ✅ Future Improvements

* User login system
* API integration with fitness devices
* Weekly/monthly reports
* PDF export option
* Cloud hosting (e.g., Heroku/AWS)

---

## 📚 References

* [Flask Documentation](https://flask.palletsprojects.com)
* [Matplotlib](https://matplotlib.org)
* [MySQL Docs](https://dev.mysql.com/doc/)
* [W3Schools HTML/CSS](https://www.w3schools.com)

---

## 🙌 Author

**Abhigya**
Class: A-1 (IP)
Roll No: 2311981018

---

Let me know if you'd like this as a `.md` file to download or edit!

# 📊 Log Analyzer with CI/CD & GitHub Actions

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerized-green?logo=docker)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-blue?logo=githubactions)
![Status](https://img.shields.io/badge/Status-Automated-brightgreen)

## 📌 Project Overview

This project showcases a fully automated **log analysis and reporting system** using modern DevOps practices.

- 📜 Parses structured web server logs
- 📊 Generates analytics report (CSV & Graph)
- ⚙️ Automates analysis with GitHub Actions CI/CD
- 🐳 Dockerized Python application
- 🔁 Workflow runs on every code or log update

---

## 🚀 Features

- ✅ Real-time log parsing and summary reporting
- ✅ Error trend visualization (line chart)
- ✅ Auto CI/CD via GitHub Actions
- ✅ Docker-based reproducibility
- ✅ Structured codebase with modular design

---

## 🧱 Tech Stack

| Layer            | Tools / Services                      |
|------------------|----------------------------------------|
| Language         | Python 3.12                            |
| Libraries        | `pandas`, `matplotlib`, `re`, `os`     |
| Containerization | Docker                                 |
| CI/CD Pipeline   | GitHub Actions                         |
| Reports          | CSV & PNG file output                  |
| Triggering       | Push to main branch or `logs/` folder  |

---

## 🧪 How It Works

### 📝 Log Format (Apache-style)

27.0.0.1 - - [16/Jul/2025:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024



### 🔍 Analyzer Functions

- Extracts: IP, Time, Method, Endpoint, Status Code, Response Size
- Summarizes:
  - Total Requests
  - Error Counts (4xx & 5xx)
  - Error Rate (%)
- Visualizes: Errors over time (HH:MM)

  
## ⚙️ CI/CD Workflow

### 📥 On Push to `main`, GitHub Actions:

1. 📦 **Checks out repo**
2. 🐍 **Installs dependencies**
3. 🧪 **Runs log analyzer**
4. 📁 **Uploads summary and chart as artifacts**

> Trigger Paths:
``yaml
on:
  push:
    branches:
      - main

##  🐳 Docker Support
🔧 Build the image
bash
Copy
Edit
docker build -t log-analyzer .
▶️ Run the container
bash
Copy
Edit
docker run --rm log-analyzer
📂 Folder Structure
pgsql
Copy
Edit
├── analyzer/
│   └── analyze.py
├── logs/
│   └── sample.log
├── reports/
│   ├── summary.csv
│   └── error_graph.png
├── .github/
│   └── workflows/
│       └── analyze.yml
├── Dockerfile
├── requirements.txt
└── README.md

## 🧠 Learning Outcome
CI/CD workflow integration via GitHub Actions

Automating Python log analysis

Handling time formats and regex parsing

Dockerizing analytics tools

Working with GitHub artifact uploads

🙌 Acknowledgements
Log format inspired by Apache HTTPD Logs

DevOps Automation implemented by Adharsh

📣 Contact
📧 Adharsh – LinkedIn
🌍 GitHub – adharsh277

python
Copy
Edit

---

Let me know if you'd like this as a downloadable `README.md` file or added to your repo automatically. You're ready to proudly showcase this, Captain! 🫡

























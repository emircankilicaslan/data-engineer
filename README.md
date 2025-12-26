# Data Engineering Case Study

This repository contains the solution for the Data Engineering Case. It features a backend API for Clan Management and a Data Analysis pipeline using DBT concepts.

## 🚀 Part 1: Clan API & Deployment
- **Tech Stack:** Python (FastAPI), PostgreSQL, Docker.
- **Deployment:** Render.com (Containerized Web Service).
- **Database:** PostgreSQL (Cloud hosted).

### API Usage
The API allows creating, listing, searching, and deleting clans.
- **Live URL:** https://data-engineer-xjxn.onrender.com
- **Documentation:** https://data-engineer-xjxn.onrender.com/docs



## 📊 Part 2: DBT Model & Visualization
- **Data Warehouse:** Google BigQuery.
- **Modeling:** `daily_metrics.sql` aggregates raw user data into daily KPIs (DAU, ARPDAU, Win Rates).
- **Visualization:** Google Looker Studio.

### Key Findings
- **DAU & Revenue:** Aggregated by Country and Platform to track daily performance.
- **Game Balance:** Win/Defeat ratios calculated to monitor game difficulty.

# Vertigo Games Data Engineering Case Study

This repository contains the solution for the Vertigo Games Data Engineering Case. It features a backend API for Clan Management and a Data Analysis pipeline using DBT concepts.

## 🚀 Part 1: Clan API & Deployment
- **Tech Stack:** Python (FastAPI), PostgreSQL, Docker.
- **Deployment:** Render.com (Containerized Web Service).
- **Database:** PostgreSQL (Cloud hosted).

### API Usage
The API allows creating, listing, searching, and deleting clans.
- **Live URL:** https://data-engineer-xjxn.onrender.com
- **Documentation:** https://data-engineer-xjxn.onrender.com/docs



## 📊 Part 2: DBT Model & Visualization
- **Data Warehouse:** Google BigQuery.
- **Modeling:** `daily_metrics.sql` aggregates raw user data into daily KPIs (DAU, ARPDAU, Win Rates).
- **Visualization:** Google Looker Studio.

### Key Findings
- **DAU & Revenue:** Aggregated by Country and Platform to track daily performance.
- **Game Balance:** Win/Defeat ratios calculated to monitor game difficulty.

<img width="1082" height="673" alt="image" src="https://github.com/user-attachments/assets/ec5019c6-4eb7-4b07-b9c8-90780f747916" />


## 🛠️ How to Run Locally
1. Clone the repo.
2. Build Docker image:
   ```bash
   docker build -t clan-api .



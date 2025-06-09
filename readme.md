# **Learning Path to Become a Data Analyst in the Microsoft Stack**

Notes on becoming a junior data analyst in the Microsoft stack.


---

## 📏 Phase 1: Foundations (Weeks 1–4)

### 1. Excel Essentials

**Skills to Learn:**
- Common functions: `VLOOKUP`, `INDEX/MATCH`, `IF`, `SUMIFS`, `COUNTIFS`
- Creating Pivot Tables and Pivot Charts
- Cleaning and transforming data with Power Query

**Example Projects:**
- Analyze a sales dataset (monthly revenue by region)
- Build a dashboard showing total sales, top 5 products, and monthly trends
- Use Power Query to clean raw customer data (remove duplicates, fill blanks)

### 2. SQL for Data Analysis

**Skills to Learn:**
- Basic queries with `SELECT`, `WHERE`, `ORDER BY`
- Joins (`INNER`, `LEFT`, `RIGHT`, `FULL`)
- Aggregations with `GROUP BY`, filtering with `HAVING`
- Common Table Expressions (CTEs), Window Functions

**Example Projects:**
- Query a customer orders database to show average order value per region
- Use a CTE to find the top 3 selling products each month
- Calculate moving averages and running totals using window functions

---

## 🚧 Phase 2: Microsoft Stack Deep Dive (Weeks 5–10)

### 3. SQL Server & T-SQL

**Skills to Learn:**
- Writing stored procedures and user-defined functions
- Creating views and indexing strategies
- Understanding execution plans and optimizing queries
- Scheduling tasks with SQL Server Agent

**Example Projects:**
- Build a stored procedure to generate monthly KPIs from sales data
- Create a view that combines customer, product, and sales info for reporting
- Tune a slow query by analyzing the execution plan and applying indexes

### 4. Power BI for Data Visualization

**Skills to Learn:**
- Connecting to data sources: Excel, SQL Server, web APIs
- Building reports with visuals, slicers, and filters
- Using DAX functions: `CALCULATE`, `FILTER`, `SUMX`, `ALL`

**Example Projects:**
- Build an interactive sales dashboard with filters by region and product
- Use DAX to create YoY growth measures and profit margin KPIs
- Visualize customer churn by month and segment using a line chart

### 5. Microsoft Access (Optional)

**Skills to Learn:**
- Designing tables and relationships
- Writing Access queries and forms
- Creating simple reports

**Example Projects:**
- Build a mini CRM system for tracking client interactions
- Create a form-based data entry system for product inventory

---

## ☁️ Phase 3: Intro to Azure for Analysts (Weeks 11–14)

### 6. Azure Data Fundamentals (DP-900)

**Skills to Learn:**
- Understanding Azure SQL, Azure Synapse Analytics
- Basics of Azure Data Lake, Azure Blob Storage
- Intro to data security, compliance, and data governance

**Example Projects:**
- Load CSV data into Azure SQL Database and run simple queries
- Use Synapse Studio to explore and analyze a sample dataset
- Store and retrieve files from Azure Blob Storage using the portal

---

## 🤖 Phase 4: Python for Analysts (Weeks 15–17)

### 7. Python for Data Analysis

**Skills to Learn:**
- `pandas` for dataframes, `numpy` for calculations
- `matplotlib`/`seaborn` for visualizations
- Connecting to SQL Server via `pyodbc` or `sqlalchemy`

**Example Projects:**
- Analyze a CSV of ecommerce transactions: average basket size, repeat rate
- Visualize distribution of order amounts with histograms and boxplots
- Write a script to automate daily data pull from SQL Server and save to Excel

---

## 🛠️ Phase 5: Portfolio & Job Readiness (Weeks 18–20)

### 8. Build a Portfolio

**Projects to Include:**
- Power BI dashboard: Sales performance or Customer Segmentation
- Python notebook: Data exploration and insights from a public dataset
- SQL Server report: Stored procedures generating KPIs and summaries

### 9. Interview Preparation

**Skills to Practice:**
- Explaining projects clearly (STAR format)
- Writing SQL JOINs and aggregations under time pressure
- Creating DAX measures on the fly

**Example Activities:**
- Mock interview: Explain how you cleaned and visualized messy data
- SQL challenge: Find the second highest salary in a table
- DAX challenge: Create a measure for average daily revenue excluding weekends

---

## 🌟 Final Outcome

After completing this learning path, the learner will be able to:
- Clean, manipulate, and visualize data using Excel, Power BI, and Python
- Write efficient queries and procedures in SQL Server
- Work with cloud data tools in Azure
- Apply for junior data analyst roles confidently with a strong portfolio

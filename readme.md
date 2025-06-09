# **Learning Path to Become a Data Analyst in the Microsoft Stack**

Notes on becoming a junior data analyst in the Microsoft stack. It's a work in progress.

I'd originally made this https://gist.github.com/DominicFinn/41ffee1876d742638415d60a0b37850f for a friend. It was a bit of an incomplete idea dump which was inspired by my previous dump for javascript https://gist.github.com/DominicFinn/3ecb07c7bac2d6fa49a3d931c8ccc0ba

At the end, you should have some experiences or using the tools in data analysis. You will have opinions on which tools are best for which tasks. 

Expand on each section as needed by moidifiying my scripts to create different types of data and projects. This will help you to create a bigger portfolio of work. 

---

## 📏 Phase 1: Foundations (Weeks 1–4)

### 1. Excel Essentials

**Skills to Learn:**
- Common functions: `VLOOKUP`, `IF`, `SUMIFS`, `COUNTIFS`
- Creating Pivot Tables and Pivot Charts
- Transforming data
- Choosing the best chart for the data
- Data Storytelling

**Example Projects:**
- Analyze a sales dataset (monthly revenue by region)
- Build a dashboard showing total sales, top 5 products, and monthly trends
- Reports on customer orders


### 2. SQL for Data Analysis

**Skills to Learn:**
- Basic queries with `SELECT`, `WHERE`, `ORDER BY`
- Joins (`INNER`, `LEFT`, `RIGHT`, `FULL`)
- Aggregations with `GROUP BY`, filtering with `HAVING`
- Common Table Expressions (CTEs), Window Functions
- Indexing
- Dealing with tricky data
- Dealing with missing data
- Dealing with outliers and data quality issues
- Dealing with time-based data

Will think about this more. 

**Example Projects:**
- Query a customer orders database to show average order value per region 

- Calculate moving averages and running totals using window functions

Can keep this simple for now.


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
- Understanding measures

**Example Projects:**
- Build an interactive sales dashboard with filters by region and product
- Create YoY growth measures and profit margin KPIs
- Visualize customer churn by month and segment using a line chart

### 5. .Net Fun (Optional)

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


### 8. Machine learning and data mining techniques with Python 

**Skills to Learn:**
- apriori algorithm
- k-means clustering / cluster analysis
- categorical data, classification
- regression analysis
- decision trees
- random forests
- neural networks / deep learning
- support vector machines
- gradient boosting

**Example Projects:**
- Use the apriori algorithm to find associations between products (e.g. products that are often bought together)
- Use k-means clustering to group customers (e.g. customers with similar purchase history)
- Use decision trees to predict customer churn (e.g. predict which customers are likely to churn)
- Use rule based classification to look at IoT data and predict which devices are likely to fail

Add more fun here when the time comes. This will be the best bit.

Brucey bonus will be: learning to deploy something so it can be used by a business. 

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
- Taking a brief and turning it into a project
- Writing SQL JOINs and aggregations under time pressure
- Creating measures on the fly in Power BI
- Talking coherently about data

**Example Activities:**
- Mock interview: Explain how you cleaned and visualized messy data
- SQL challenge: Find the second highest salary in a table
- Power BI challenge: Create a measure for average daily revenue excluding weekends

---

## 🌟 Final Outcome

After completing this learning path, the learner will be able to:
- Clean, manipulate, and visualize data using Excel, Power BI, and Python
- Write efficient queries and procedures in SQL Server
- Work with cloud data tools in Azure
- Apply for junior data analyst roles confidently with a strong portfolio

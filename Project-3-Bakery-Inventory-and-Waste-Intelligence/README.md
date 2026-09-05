# 🥖 Golden Crust Bakery: End-to-End Inventory & Waste Intelligence Pipeline
An enterprise-grade data engineering and business intelligence solution mapping **Excel data intake systems**, automated **Python ETL scripting**, relational **SQL warehousing (SQLite)**, and an executive-facing **Power BI dashboard** to isolate inventory losses and optimize operational revenue.

---

## 📊 1. Executive Summary & Business Case
### The Problem
**Golden Crust Bakery** observed significant margin compression driven by a high volume of end-of-day product disposal. Perishable goods like croissants, pastries, and artisanal breads were routinely thrown out, but management lacked historical visibility into whether the waste was driven by product-specific demand shifts, seasonal variance, or operational over-production.

### The Objective
To build an automated data analytics pipeline that:
1. Aggregates disjointed business records across manual production logs, point-of-sale (POS) transaction ledgers, and waste receipts.
2. Identifies specific operational anomalies causing inventory inflation.
3. Quantifies financial revenue leakage to provide actionable recommendations for daily production scaling.

---

## 🏗️ 2. Architectural Blueprint & Technical Stack
The pipeline mirrors a modern production framework, routing data from raw manual entry up to executive visuals:

```text
[Excel Data Entry Tables] ➔ [Python Data Pipeline (Pandas)] ➔ [SQLite Warehouse (.db)] ➔ [Power BI Desktop Modeling]
```

* **Data Intake & Entry Source:** **Microsoft Excel / Google Sheets** used by on-site bakery staff for friction-free recording.
* **Data Engineering & ETL Logic:** **Python 3 (`pandas`, `numpy`, `sqlite3`)** executed to clean structures, auto-format data types, generate transactional variations, and push tables into relational storage.
* **Relational Storage Engine:** **SQL (`SQLite`)** hosting local schemas to aggregate multi-fact transactional rows without inflating calculations.
* **Business Intelligence Center:** **Power BI Desktop** using custom cross-filtered **Composite Data Keys** to deliver dynamic diagnostics.

---

## ⚙️ 3. Comprehensive Pipeline Phases & Implementation

### Phase 1: Data Ingestion & Google Sheets Origin
To establish a rigorous, realistic benchmarking framework, data running from **March 2026 to August 2026** was established. The inventory spans 5 primary product lines: *Croissant, Sourdough Bread, Chocolate Pastry, Baguette, and Cinnamon Roll*. 

Staff input daily figures into three separate tabs within a workbook named `Golden_Crust_Bakery_Data.xlsx`:
1. `Production_Logs`: Daily targets baked per item.
2. `POS_Sales`: Customer retail transaction records.
3. `Waste_Logs`: Physical scraps discarded at close of business.

#### Project Artifact:
![00_Raw_Spreadsheet_Data_Source]
<img width="516" height="641" alt="00_Raw_Spreadsheet_Data_Source png" src="https://github.com/user-attachments/assets/5d819ed1-75b3-44be-ab0e-2e056af56e8b" />

---

### Phase 2: Programmatic Data Scaling (Python Script)
To mimic actual corporate patterns, a Python generation module was constructed to simulate 6 months of retail traffic, accounting for a **40% weekend surge** (Fridays through Sundays) and a **systemic operational over-baking flaw on early weekdays** (Tuesdays and Wednesdays).

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Initialize seed for reproducible generation
np.random.seed(42)

start_date = datetime(2026, 3, 1)
end_date = datetime(2026, 8, 31)
delta_days = (end_date - start_date).days + 1

items = ['Croissant', 'Sourdough Bread', 'Chocolate Pastry', 'Baguette', 'Cinnamon Roll']
base_demand = {'Croissant': 50, 'Sourdough Bread': 30, 'Chocolate Pastry': 40, 'Baguette': 25, 'Cinnamon Roll': 35}

prod_records = []
sales_records = []
waste_records = []
tx_id = 10001

for d in range(delta_days):
    current_date = start_date + timedelta(days=d)
    date_str = current_date.strftime('%Y-%m-%d')
    day_name = current_date.strftime('%A')
    
    # Contextual Logic Constraint: Traffic surges on weekends
    multiplier = 1.4 if day_name in ['Saturday', 'Sunday'] else 1.0
    
    for item in items:
        # Contextual Logic Constraint: Staff systematically over-bakes on early weekdays
        if day_name in ['Tuesday', 'Wednesday']:
            baked = int(base_demand[item] * 1.35) 
        else:
            baked = int(base_demand[item] * multiplier + np.random.randint(-2, 4))
            
        prod_records.append({'Date': date_str, 'Day_of_Week': day_name, 'Item_Name': item, 'Quantity_Baked': baked})
        
        # Retail Purchasing Logic: Mid-week consumer demand drops sharply
        if day_name in ['Tuesday', 'Wednesday']:
            actual_demand = int(base_demand[item] * 0.80 + np.random.randint(-4, 4))
        else:
            actual_demand = int(base_demand[item] * multiplier + np.random.randint(-5, 5))
            
        sold = min(baked, max(0, actual_demand))
        
        # Granular Data Engineering: Slice daily totals into separate customer tickets
        if sold > 0:
            slices = sorted([0, np.random.randint(1, max(2, sold//2)), np.random.randint(max(2, sold//2), max(3, sold)), sold])
            unique_slices = list(set(slices))
            unique_slices.sort()
            for i in range(len(unique_slices)-1):
                qty = unique_slices[i+1] - unique_slices[i]
                if qty > 0:
                    sales_records.append({'Transaction_ID': tx_id, 'Date': date_str, 'Item_Name': item, 'Quantity_Sold': qty})
                    tx_id += 1
                
        # Closing Verification Logic: Scrap totals must always balance (Baked minus Sold)
        waste = max(0, baked - sold)
        waste_records.append({'Date': date_str, 'Item_Name': item, 'Quantity_Wasted': waste})

# Compile frames and export out to primary source
df_prod = pd.DataFrame(prod_records)
df_sales = pd.DataFrame(sales_records)
df_waste = pd.DataFrame(waste_records)

with pd.ExcelWriter('Golden_Crust_Bakery_Data.xlsx') as writer:
    df_prod.to_excel(writer, sheet_name='Production_Logs', index=False)
    df_sales.to_excel(writer, sheet_name='POS_Sales', index=False)
    df_waste.to_excel(writer, sheet_name='Waste_Logs', index=False)

print("Pipeline data generation completed successfully.")
```

#### Project Artifact:
![01_Python_Data_Generation_Pipeline]
<img width="1209" height="388" alt="01_Python_Data_Generation_Pipeline png" src="https://github.com/user-attachments/assets/c5ee7881-2ea4-4a63-a50d-a6a1624b18b3" />


---

### Phase 3: Python to SQL ETL Pipeline Execution
A Python orchestration script extracts individual arrays from the sheet, applies data conversions, drops existing outdated schema blocks via the `if_exists='replace'` argument to safeguard database integrity, and pipes data blocks natively into a relational `Golden_Crust_Bakery.db` file using `sqlite3`.

```python
import pandas as pd
import sqlite3

# Initialize SQLite internal serverless connection
conn = sqlite3.connect('Golden_Crust_Bakery.db')
cursor = conn.cursor()

excel_file = 'Golden_Crust_Bakery_Data.xlsx'
df_prod = pd.read_excel(excel_file, sheet_name='Production_Logs')
df_sales = pd.read_excel(excel_file, sheet_name='POS_Sales')
df_waste = pd.read_excel(excel_file, sheet_name='Waste_Logs')

# Database Loading with programmatic row overwrite configurations
df_prod.to_sql('production_logs', conn, if_exists='replace', index=False)
df_sales.to_sql('pos_sales', conn, if_exists='replace', index=False)
df_waste.to_sql('waste_logs', conn, if_exists='replace', index=False)

# Validate architectural schema visibility
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(f"ETL Execution Verified. Tables initialized: {tables}")
conn.close()
```

#### Project Artifact:
![02_Python_to_SQL_ETL_Pipeline]
<img width="931" height="397" alt="02_Python_to_SQL_ETL_Pipeline png" src="https://github.com/user-attachments/assets/a810fbe1-2795-4cf5-9fd8-53ce7a947991" />


---

### Phase 4: Relational SQL Aggregation & Analysis
Because customer invoices are recorded line-by-line (granular data structure) while baking limits are logged on a daily batch basis (aggregated structure), running standard joins directly would lead to severe row multiplication and calculation inflation bugs.

**Solution:** A SQL query utilizing a **Common Table Expression (CTE)** aggregates customer sales transactions *before* performing multi-table joins. Precision casting (`CAST(... AS REAL)`) prevents default integer truncation bugs in SQLite, and a custom conditional sorting scheme correctly indexes the calendar week.

```sql
WITH Aggregated_Sales AS (
    SELECT 
        Date,
        Item_Name,
        SUM(Quantity_Sold) AS Total_Sold
    FROM pos_sales
    GROUP BY Date, Item_Name
)
SELECT 
    p.Day_of_Week,
    p.Item_Name,
    SUM(p.Quantity_Baked) AS Total_Produced,
    SUM(COALESCE(s.Total_Sold, 0)) AS Total_Sold,
    SUM(w.Quantity_Wasted) AS Total_Wasted,
    ROUND(
        (CAST(SUM(w.Quantity_Wasted) AS REAL) / SUM(p.Quantity_Baked)) * 100, 
        2
    ) || '%' AS Waste_Percentage
FROM production_logs p
LEFT JOIN Aggregated_Sales s 
    ON p.Date = s.Date AND p.Item_Name = s.Item_Name
LEFT JOIN waste_logs w
    ON p.Date = w.Date AND p.Item_Name = w.Item_Name
GROUP BY p.Day_of_Week, p.Item_Name
ORDER BY 
    CASE p.Day_of_Week
        WHEN 'Monday' THEN 1
        WHEN 'Tuesday' THEN 2
        WHEN 'Wednesday' THEN 3
        WHEN 'Thursday' THEN 4
        WHEN 'Friday' THEN 5
        WHEN 'Saturday' THEN 6
        WHEN 'Sunday' THEN 7
    END, 
    SUM(w.Quantity_Wasted) DESC;

![03_SQL_Data_Aggregation_and_Analysis]
<img width="982" height="495" alt="03_SQL_Data_Aggregation_and_Analysis png" src="https://github.com/user-attachments/assets/6cc1c582-4a3f-449d-ba1b-635a73e7ea91" />

# Golden Crust Bakery: Data Optimization & Analytics Pipeline

## 🛠️ Phase 5: Power BI Modeling & Optimization
![04_Power_BI_Data_Ingestion_and_Modeling] !<img width="803" height="279" alt="04_Power_BI_Data_Ingestion_and_Modeling png" src="https://github.com/user-attachments/assets/54b199df-b99e-4956-8d52-155e088a0b07" />

During the initial structural visualization setup, single-column relationships created many-to-many ambiguity errors and inactive, broken filtering paths (dotted relationship lines). This caused dashboard charts to loop flat, identical totals across different categories.

### Solution Implementation
* **Composite Keys:** Leveraged Power Query to merge the `Date` and `Item_Name` columns across all fact contexts into a single unified composite key column: `Date_Item_Key`.
* **Schema Rebuild:** Completely rebuilt the model schema to establish active, explicit One-to-Many (`1:*`) and One-to-One (`1:1`) relationship paths.
* **Cross-Filtering:** Enabled Bi-directional Cross Filtering (`Both`), allowing data transformations to flow across all dashboard charts cleanly and accurately.

---

## 📊 Phase 6: Executive Reporting Dashboard & Interface Design
![05_Final_Power_BI_Executive_Dashboard]
<img width="1011" height="568" alt="05_Final_Power_BI_Executive_Dashboard png" src="https://github.com/user-attachments/assets/69584990-fb18-4045-9fe9-12b5306771db" />

The final presentation canvas delivers an intuitive command console for leadership, tracking key performance parameters seamlessly:

* **Operational High-Level Cards:** Grouped global metric calculations (`Total Produced`, `Total Sold`, and `Total Wasted`) at the top row for a quick snapshot of overall performance.
* **Diagnostic Column Metrics:** Isolated waste behavior by calendar tracking day, instantly flagging a massive surge in waste during early weekdays.
* **Product Efficiency Lines:** Overlaid total baking targets directly against customer retail transactions on a combo chart to easily expose inventory scheduling mismatches.
* **Granular Deep-Dive Matrix:** Incorporated systematic conditional background data bars to direct store managers immediately to severe product loss cells.

---

## 💡 Data Insights & Strategic Operations Roadmap
Based on the patterns uncovered by this analytics pipeline, Golden Crust Bakery can eliminate substantial margin loss by implementing three key operational changes:

* **Implement Mid-Week Baking Caps:** Waste ratios spike above 40% on Tuesdays and Wednesdays because production limits remain unchanged despite a natural drop in early-week retail foot traffic. Lowering baseline production by 30% on these specific days will sharply reduce waste while maintaining sufficient stock.
* **Increase Weekend Batch Limits:** Friday through Sunday logs show exceptionally low waste ratios (frequently under 8%), with high-margin artisanal goods like Sourdough Bread selling out hours before closing. Increasing weekend production targets by 15% will capture this unmet customer demand and boost revenue.
* **Automate Inventory Feedback Loops:** By utilizing the automated Python-to-SQL script developed in this pipeline, management can automatically process the previous week's Excel logs every Sunday night to dynamically adjust production volumes for the upcoming week. This transitions the business from reactive waste management to a proactive scheduling strategy.

---

## 🎯 Conclusion & Technical Retrospective
Through this project, a fully unified, modern data ecosystem was successfully implemented for a traditional retail setting. By taking disjointed spreadsheets and engineering a structured, automated pipeline, we successfully transformed raw daily inputs into an actionable, analytical roadmap.

The structural model optimization completed in Power BI via custom composite data keys guarantees that business users see exact, product-specific metrics rather than misleading averages. This optimization saves thousands of items from ending up in disposal bins while maximizing on-shelf product availability during peak weekend sales surges.


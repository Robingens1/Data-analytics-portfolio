# Supply Chain & Sales Intelligence System

An automated data engineering pipeline and interactive business intelligence workspace designed to unify fragmented sales inventory logs, run algorithmic asset optimization models, and mitigate downstream fulfillment risks.

![The Complete Supply Chain & Sales Intelligence Workspace]
<img width="1363" height="634" alt="The Complete Supply Chain   Sales Intelligence Workspace" src="https://github.com/user-attachments/assets/8fb75d48-5af3-4036-a47b-612296058462" />

---

## 💼 1. Business Case & Problem Statement
Modern enterprise supply chains generate massive volumes of transactional and logistical data daily. However, operational leadership frequently suffers from systemic information asymmetry due to data fragmentation. When transaction logs, warehouse configurations, and supplier schedules are managed across disconnected files, critical operational blind spots emerge. 

Without a centralized analytics system, these data silos hide downstream fulfillment threats. High-velocity items deplete without triggering purchase orders, resulting in revenue leakage from stockouts. Conversely, slow-moving inventory accumulates unmonitored, trapping essential working capital in stagnant assets. This project bridges those gaps by replacing reactive manual auditing with a proactive, automated data engine and executive reporting workspace.

### 🔎 Pre-Transformation Vulnerability Analysis
An exploratory structural diagnostics phase conducted on the unrefined datasets exposed multiple systemic entry defects across the operational logs:
* **Dimensional Categorical Variance:** The transaction logs recorded geographic market zones with fragmented string formatting (e.g., a mix of `North`, `WEST`, `south`, and `NORTH`), splitting regional metrics.
* **Temporal Discrepancies:** Chronological data fields suffered from mixed formatting delimiters (alternating between `YYYY-MM-DD` and `MM/DD/YYYY`), which breaks native database sorting routines.
* **Data Corruption and Null Gaps:** Omissions in manual price logs and product counts left critical value gaps, risking inaccurate revenue calculations.

![Exploratory Structural Diagnostic Audit & Source Data Profiling]
<img width="568" height="640" alt="Exploratory Structural Diagnostic Audit   Source Data Profiling" src="https://github.com/user-attachments/assets/94379f4b-9363-4dd8-a8c4-7ed568ec4026" />

![Siloed Operational Master Logistics Profile & Supplier Schedule Dataset]
<img width="556" height="553" alt="Siloed Operational Master Logistics Profile   Supplier Schedule Dataset" src="https://github.com/user-attachments/assets/c9bb2f7c-9949-471c-a9b1-0adf598d55e5" />

![Warehouse Meta-Data Configuration File & Inventory Threshold Targets]
<img width="563" height="590" alt="Warehouse Meta-Data Configuration File   Inventory Threshold Targets" src="https://github.com/user-attachments/assets/f38f68be-f30b-4cc0-8a0f-571f26508da9" />

---

## ⚙️ 2. Solution Architecture & Technical Stack

* **Data Engineering Stack:** Python 3 (Pandas, NumPy, OpenPyXL) via Google Colab and Anaconda Jupyter notebook environments.
* **Analytics Layer:** Algorithmic metric evaluation using automated mathematical transformations and grouping mechanics.
* **Presentation Layer:** Google Sheets / WPS Office interactive multi-tier cross-filtered intelligence interface.

### 🛠️ Ingestion & Mock Data Simulation
To test the pipeline's error-handling stability under realistic conditions, a dedicated mock data script was engineered to programmatically generate data and inject structural defects across the flat files and nested worksheets.

![Programmatic Data Simulation Pipeline & Operational Control Script]
<img width="823" height="472" alt="Programmatic Data Simulation Pipeline   Operational Control Script" src="https://github.com/user-attachments/assets/71b5d88a-7912-4745-8706-8816338b20ae" />

![Algorithmic Corruption Ingestion & Data Flaw Injection Module]
<img width="923" height="428" alt="Algorithmic Corruption Ingestion   Data Flaw Injection Module" src="https://github.com/user-attachments/assets/dfb4b97b-bb15-42bf-a6f7-b89b36c08742" />

---

## 🧮 3. Algorithmic Data Engineering Pipeline
The backend data engine automates extraction, fixes formatting defects, handles missing values, and merges information using the `Product_ID` key.

![Automated Ingestion, Dimensional Normalization & Data Imputation Pipeline](images/image3.png)

### Key Transformation Steps:
1. **String Normalization:** Cleans and converts all unique alpha-numeric item tokens and regional fields to a standardized uppercase format (`.astype(str).str.upper().str.strip()`), eliminating join fragmentation.
2. **Temporal Stabilization:** Uses a multi-format parsing algorithm (`format='mixed'`) to convert inconsistent date rows into uniform datetime objects.
3. **Robust Data Imputation:** Resolves empty financial cells by calculating the specific mean price for each individual product ID. This preserves row counts and data integrity without deleting valuable rows.

![Advanced Logistical Calculations & Programmatic Pareto ABC Categorization Model]
<img width="657" height="491" alt="Automated Ingestion, Dimensional Normalization   Data Imputation Pipeline" src="https://github.com/user-attachments/assets/a266bf03-8676-4d54-add7-531761b98fc5" />

### Core Supply Chain Metrics Calculated:

#### A. Inventory Turnover Rate (ITR)
Evaluates asset capital velocity by analyzing how efficiently inventory is sold and replaced relative to current warehouse capacity:
$$\text{Inventory Turnover Rate} = \frac{\sum \text{Annual Units Sold}}{\text{Current Stock Level}}$$

#### B. Stockout Risk Alert Flag
A programmable binary metric that highlights immediate supply chain gaps by flagging rows where active warehouse balances drop below safety reorder points:
$$\text{Stockout Risk} = \begin{cases} 1 & \text{if Current Stock} < \text{Reorder Point} \\ 0 & \text{otherwise} \end{cases}$$

#### C. Programmatic Pareto Distribution (ABC Analysis)
Applies the Pareto Principle to segment items by economic impact based on their rolling cumulative revenue velocity. This helps procurement teams prioritize high-value stock:
* **Class A (Top 80%):** Core financial engines requiring strict protection.
* **Class B (Next 15%):** Stable operational items requiring standard review.
* **Class C (Bottom 5%):** Long-tail low-priority items suitable for liquidation.

---

## 📉 4. Dashboard Architecture & Layout Blueprint
The master data engine exports a single, clean file (`Clean_Sales_Inventory.csv`) that serves as the verified data source for the executive reporting workspace.

![The Unified Analytical Master Data Layer & Engineered Target Metrics Schema]
<img width="1365" height="644" alt="The Unified Analytical Master Data Layer   Engineered Target Metrics Schema" src="https://github.com/user-attachments/assets/d5048e2c-67f7-4853-a6a1-b1829e64f806" />

### Row 1: Multi-Tier Strategic KPI Banner
Displays top-line revenue (\$1.27M) and distribution volumes (5,013 units). It includes a conditional exception rule that flashes soft red to alert managers to the **104 high-priority Class A items** facing an immediate stockout threat.

![Multi-Tier Strategic KPI Banner & Exception Handling Scorecards]
<img width="933" height="116" alt="Multi-Tier Strategic KPI Banner   Exception Handling Scorecards" src="https://github.com/user-attachments/assets/d9defbd8-f0d8-4402-be8c-386f595fae0d" />

### Row 2: Tactical Supply vs. Demand Velocity Trends
Cross-references commercial velocity against warehouse space across a continuous timeline. Total financial volume (`Line_Revenue`) is plotted as blue vertical columns against the left axis, while average stock balances (`Current_Stock_Level`) run as a red trend line against a secondary right axis, helping users spot seasonal demand patterns.

![Dual-Axis Combo Charting for Supply vs. Demand Velocity Correlation]
<img width="807" height="306" alt="Dual-Axis Combo Charting for Supply vs  Demand Velocity Correlation" src="https://github.com/user-attachments/assets/b9655ce0-fab4-4fdc-879c-19108afa14cf" />

### Row 3: Actionable Operational Intelligence Tables
An automated pivot layout that isolates logistical constraints at the vendor level. It filters out safe transactions to display **only** suppliers tied to active stock shortfalls, sorted by longest lead times. This immediately highlights that **Gamma Corp** poses the highest risk, with an average turnaround lag of **8.38 days** across 516 endangered product units.

![Fulfillment Exception Pivot Matrix & High-Risk Vendor Lead Time Rankings]
<img width="529" height="103" alt="Fulfillment Exception Pivot Matrix   High-Risk Vendor Lead Time Rankings" src="https://github.com/user-attachments/assets/b1558871-1dfc-4142-a800-2432f9264cd9" />

### Data Modeling & Interactive Filtering Strategy
To maximize usability, an interactive `Store_Region` control slicer is pinned to the dashboard interface. This module allows stakeholders to filter all metrics, charts, and pivot grids concurrently without reloading data.

![Interactive Multi-Dimensional Cross-Filtering Component & Regional Slicer]
<img width="496" height="108" alt="Interactive Multi-Dimensional Cross-Filtering Component   Regional Slicer" src="https://github.com/user-attachments/assets/e7583894-8f07-4c66-aecd-372bbe8640f0" />

---

## 🏁 5. Conclusion
The implementation of the **Supply Chain & Sales Intelligence System** demonstrates the business value of transforming siloed, unrefined datasets into an integrated analytics system. By establishing a robust data pipeline, this project successfully eliminated manual data entry anomalies, standardized regional metrics, and unified fragmented operational logs into a single master data layer.

## 💡 6. Strategic Recommendations

Based on the operational insights surfaced by the dashboard workspace, leadership should implement the following strategic supply chain adjustments:

**Vendor Service Level Agreement (SLA) Renegotiation:** Procurement teams must prioritize re-negotiating turnaround timelines and contract terms with **Gamma Corp**. Their documented average delivery delay of **8.38 days** accounts for **516 high-priority stockout risks**, making them the primary source of supply chain friction.
**Capital Reallocation via ABC Segmentation:** Operations should immediately reduce safety stock holding thresholds for **Class C** long-tail items. Liquidating or reducing orders on slow-moving inventory optimizes working capital, freeing up cash flow to fully back your high-velocity, high-margin **Class A** revenue lines.
**Safety Stock Buffer Adjustments:** For Class A items with high seasonal demand variations (as clearly mapped on the trend chart), reorder point boundaries should be dynamically scaled up by **15%** during peak sales months to build a buffer and prevent costly revenue leakage from stockouts.


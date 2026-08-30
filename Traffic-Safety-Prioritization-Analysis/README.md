# Systemic Traffic Crash Analysis & Infrastructure Investment Prioritization Tool

An end-to-end data analytics and predictive machine learning pipeline built to identify roadway risk patterns and optimize municipal safety funding allocations. This project directly addresses proactive safety resource management and infrastructure modeling.

---

## 🚀 Project Architecture & Phases
1. **Phase 1: Ingestion & Diagnostics:** Streamed and audited 100k+ real-world UK DfT vehicle collision records.
2. **Phase 2: Modeling & Risk Factors:** Built an interpretable machine learning model to extract statistical risk weights.
3. **Phase 3: Prioritization Engine:** Developed an optimization scoring framework for data-driven safety budgeting.

---

## 📥 Phase 1: Data Ingestion & Structural Validation
The initial pipeline stage handles raw data extraction and parses the features into a functional workspace. We programmatically validate the data layout to confirm spatial geometries and injury indexes before performing down-stream classification.

![Dataset Profile and Ingestion]<img width="1024" height="394" alt="dataset_profile_and_ingestion png" src="https://github.com/user-attachments/assets/aff021af-0942-495f-aa36-3e81949ebde5" />

### 🔍 Feature Auditing & Dimensional Extraction
To establish our modeling variables, we extract and inventory the raw feature space. This audit isolates critical engineering parameters—such as geometric crash vectors, atmospheric parameters, and injury outcome indices—from extraneous metadata.

![Feature Space Exploration]
<img width="1282" height="103" alt="feature_space_exploration png" src="https://github.com/user-attachments/assets/06d9138d-7c98-4e3f-9b50-45b312ca6bc4" />


### 🎯 Programmatic Feature Isolation
Using a targeted keyword filter script, we map specific metadata tokens down to an optimized subset of engineering parameters. This eliminates column clutter and leaves us with clean target arrays (`collision_severity`), spatial components (`latitude`/`longitude`), and structural factors (`road_type`, `speed_limit`).

![Targeted Feature Filtering]<img width="584" height="465" alt="targeted_feature_filtering png" src="https://github.com/user-attachments/assets/440d7a8e-d93a-4f72-89cf-5df007631572" />


### 🧮 Null-Value Audit & Target Distribution Mapping
Before transforming features, we evaluate structural missing values and profile our target class balance. The data displays 0 structural null cells, but reveals a highly skewed target layout containing 74,881 slight incidents versus 26,644 combined serious and fatal outcomes. This directly informs our down-stream machine learning class-weight balancing strategies.

![Null Value and Target Distribution]<img width="526" height="497" alt="null_value_and_target_distribution png" src="https://github.com/user-attachments/assets/e42badaf-c26d-441d-8ae4-3303286b6f3a" />


### 🕵️ Metadata Diagnostics & Hidden Placeholder Auditing
To ensure data integrity, we programmatically audit the unique arrays of our categorical features. This step evaluates whether missing entries are masked as standard numbers. The diagnostics successfully uncover hidden missing value placeholders (`-1`) within `light_conditions` and `road_surface_conditions`, allowing us to clean them before performing core analytics.

![Categorical Placeholder Audit]<img width="677" height="425" alt="categorical_placeholder_audit png" src="https://github.com/user-attachments/assets/2460f29b-c2f2-427c-9811-306be677a87f" />


---

## 📉 Phase 2: Exploratory Data Analysis & Statistical Modeling

### 🔗 Placeholder Filtration & Base-Rate Analytics
We systematically purge the hidden missing metadata placeholders (`-1`) across all critical analytical columns to ensure pure baseline evaluations. Post-filtration, the pipeline branches into cross-tabulation arrays (`pd.crosstab`) to establish foundational, non-skewed risk proportions across varied light profiles and infrastructure shapes.

![Placeholder Filtration and Crosstab]<img width="633" height="510" alt="placeholder_filtration_and_crosstab png1" src="https://github.com/user-attachments/assets/c55f603c-65d0-4bde-b6d6-072031d8e6a2" />

### 🔢 Quantitative Base-Rate Risk Profiles
After scrubbing missing placeholders, the clean workspace holds 100,877 highly structured records. Executing percentage-normalized cross-tabulations maps structural base-rates for injuries. The resulting distribution mathematically proves that darkness without illumination (Index 6: 4.70% Fatal, 31.55% Serious) and standard single-lane links (Index 6: 1.52% Fatal, 26.52% Serious) hold heavily concentrated crash injury severity rates.

![Crosstab Percentage Outputs]<img width="457" height="470" alt="crosstab_percentage_outputs png2" src="https://github.com/user-attachments/assets/343e6e66-78be-4106-9948-389ebbb43690" />


### ⚙️ Binary Target Engineering & Dummy Encoding
To transition into classification modeling, the framework converts the multi-class severity ranks into an optimized binary target vector where 1 represents high-severity (fatal/serious) and 0 represents low-severity outcomes. We subsequently apply dummy-variable mapping to expand categorical fields, rendering them computationally clean for linear mathematical optimization.

![Feature Engineering and Dummy Encoding]<img width="831" height="506" alt="feature_engineering_and_dummy_encoding png" src="https://github.com/user-attachments/assets/f72efdb8-efb8-4091-8f18-85b872d7a37d" />


### 🧠 Model Ingestion, Training & Performance Report
The pipeline uses a stratified train/test split configuration to partition 20% of the dataset as a complete out-of-sample evaluation pool. To account for heavy class imbalances between slight and severe crash outcomes, we introduce balanced class weighting into our Logistic Regression algorithm. This ensures our model correctly penalizes misclassifications on life-threatening severe injuries.

![Model Training and Evaluation]<img width="618" height="381" alt="1-model_training_and_evaluation png" src="https://github.com/user-attachments/assets/3e098cb6-97c1-4201-8f56-4addb63f08c8" />


### 📊 Out-of-Sample Performance Metrics
To gauge the robustness of our predictive framework, we evaluate the classification output against our hidden test set. While standard baseline predictors struggle with massive imbalance gaps, our class-weighted logistic engine secures a 0.77 precision on minor incidents and successfully flags nearly half of all critical life-threatening injuries (Recall: 0.48), producing a comprehensive, verifiable evaluation log.

![Classification Report Metrics]<img width="579" height="343" alt="2-classification_report_metrics png" src="https://github.com/user-attachments/assets/936dfa15-7b78-4c9d-97ea-bc423613a0e6" />


### 🧮 Mathematical Odds Ratio Extraction
To transform the classification engine weights into interpretable parameters, we isolate the raw directional coefficients and calculate their exponential function values. This step establishes precise systemic risk multipliers, demonstrating strong statistical transparency and enabling us to measure exactly how individual design variables change the likelihood of severe outcomes.

![Odds Ratio Calculation Logic]<img width="775" height="404" alt="1odds_ratio_calculation_logic png" src="https://github.com/user-attachments/assets/0a635461-19bc-4041-a86c-6a07bab79471" />


### 🔢 Empirical Risk Factors & Multipliers
The resulting parameter log establishes our empirical risk multipliers. With standard conditions serving as our control baseline, the data reveals that single carriageways increase severe injury odds by 58% (OR: 1.58), while roads completely lacking lighting infrastructure increase severe crash odds by 34% (OR: 1.34). These figures provide the mathematical bedrock for our resource allocation logic.

![Odds Ratio Output Table]<img width="831" height="302" alt="2odds_ratio_output_table png" src="https://github.com/user-attachments/assets/ae9d3450-e320-471a-ac22-2f10567ad3bb" />


### 🛠️ Graphic Visualization Architecture
To bridge the gap between analytics and visual storytelling, we construct an automated visualization script. The pipeline intercepts the raw odds ratio dataframes, maps engineering categories into polished, publication-ready textual descriptors, and overlays a static reference baseline at an Odds Ratio of 1.0 to isolate statistical growth vectors.

![Visualization Script Logic]<img width="683" height="547" alt="visualization_script_logic png01" src="https://github.com/user-attachments/assets/ee61ffd2-d12e-4d8d-aa18-34a1a84df1dd" />


### 📊 Core Empirical Research Plot
This feature importance plot displays our machine learning model's derived risk multipliers. Variables extending to the right of the red dashed line (Odds Ratio > 1.0) compound severe crash likelihoods. This visual serves as clear empirical backing, pinpointing single carriageways and unlit night segments as our primary infrastructure targets.

![Infrastructure Risk Factors Coefficients]<img width="892" height="474" alt="infrastructure_risk_coefficients png02" src="https://github.com/user-attachments/assets/fe197f37-214e-47f1-a9ac-b3f8c3222524" />


---

## 🛠️ Phase 3: Infrastructure Investment Prioritization Tool

### 🗺️ Spatial Aggregation & Grid Engineering
To convert our predictive insights into an operational tool, the script implements custom spatial grouping blocks. By rounding geospatial coordinates to 3 decimal locations (~110m grid boundaries), we map disparate incident scatter plots down into discrete infrastructure cluster nodes. The pipeline dynamically tallies regional hazard frequencies—such as high-speed layouts and unlit corridor counts—to build out a comprehensive localized safety framework.

![Spatial Clustering and Aggregation]<img width="847" height="481" alt="spatial_clustering_and_aggregation png001" src="https://github.com/user-attachments/assets/b8d31623-592b-4ed4-b7f0-a3ba124a799f" />


### 🧮 Systemic Optimization & Budget Allocation Logic
Instead of relying on reactive crash counts, the framework builds a proactive prioritization engine. The optimization script applies an algorithmic risk equation to our spatial grid nodes, scaling local volumes against design deficits using our model's exact empirical odds ratios. The algorithm automatically sorts regional coordinates to ensure agencies can maximize public safety returns on fixed infrastructure budgets.

![Systemic Risk Scoring Logic]<img width="703" height="500" alt="systemic_risk_scoring_logic png002" src="https://github.com/user-attachments/assets/0fd73c3d-f439-455c-995b-99307ea9ad20" />


### 🎯 Proactive Investment Priority Outputs
The prioritization tool outputs our high-value target cells. Crucially, the optimization architecture successfully implements a proactive safety strategy. Locations containing fewer raw crashes (such as Index 0: 7 total incidents) are successfully ranked above higher volume nodes (such as Index 3: 15 incidents) due to compounding risk factors from undivided single-carriageway layouts.

![Prioritized Investment Output]<img width="998" height="223" alt="prioritized_investment_output png003" src="https://github.com/user-attachments/assets/1e54b82b-05e0-4099-b402-2241b4901162" />


---

## 💻 Tech Stack & Methodologies Summary
* **Languages & Core Libraries:** Python, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn.
* **Mathematical Approaches:** Balanced Binary Logistic Regression, Multi-categorical One-Hot Encoding, Geospatial Coordinate Grid Aggregation, Matrix-Weighted Systemic Index Ranking ($e^\beta$).

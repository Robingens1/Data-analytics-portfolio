#!/usr/bin/env python3
"""
Supply Chain & Sales Intelligence System — Unified Data Engine & Pipeline
Author: Senior Data Analytics Mentor
Description: A single, comprehensive script that handles mock data generation 
             with intentional flaws, extracts the disparate data silos, 
             standardizes attributes, and computes advanced supply chain KPIs.
"""

import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def run_complete_supply_chain_system():
    print("="*60)
    print("🚀 INITIALIZING COMPLETE SUPPLY CHAIN & SALES INTELLIGENCE SYSTEM")
    print("="*60)
    
    # -------------------------------------------------------------------------
    # PHASE 1: INDUSTRIAL DATA SIMULATION ENGINE (Generating Mock Data)
    # -------------------------------------------------------------------------
    print("\n🏗️ Phase 1: Programmatically simulating raw corporate data silos...")
    
    np.random.seed(42)
    records_count = 1000
    products = [f"PROD-{i:03d}" for i in range(1, 31)]
    categories = ['Electronics', 'Home Appliances', 'Office Supplies', 'Apparel']
    
    # 1. Generate Product Catalog Data
    catalog_data = {
        'Product_ID': products,
        'Product_Category': np.random.choice(categories, size=30),
        'Current_Stock_Level': np.random.randint(5, 300, size=30),
        'Reorder_Point': np.random.randint(15, 80, size=30)
    }
    pd.DataFrame(catalog_data).to_excel('Product_Catalog.xlsx', index=False)
    
    # 2. Generate Supplier Performance Data
    supplier_data = {
        'Product_ID': products,
        'Supplier_Name': np.random.choice(['Alpha Logistics', 'Beta Manufacturing', 'Gamma Corp'], size=30),
        'Lead_Time_Days': np.random.randint(2, 20, size=30)
    }
    pd.DataFrame(supplier_data).to_excel('Supplier_Lead_Times.xlsx', index=False)
    
    # 3. Generate Messy Point-of-Sale Log Data
    order_dates = [datetime(2026, 1, 1) + timedelta(days=int(np.random.randint(0, 180))) for _ in range(records_count)]
    formatted_dates = [d.strftime('%Y-%m-%d') if i % 10 != 0 else d.strftime('%m/%d/%Y') for i, d in enumerate(order_dates)]
    
    sales_data = {
        'Order_ID': [f"ORD-{i:05d}" for i in range(1001, 1001 + records_count)],
        'Order_Date': formatted_dates,
        'Product_ID': np.random.choice(products, size=records_count),
        'Quantity_Sold': np.random.randint(1, 10, size=records_count),
        'Store_Region': np.random.choice(['NORTH', 'south', 'East', 'WEST', 'North', 'South'], size=records_count),
        'Unit_Price': np.random.uniform(10.0, 500.0, size=records_count)
    }
    df_sales_raw = pd.DataFrame(sales_data)
    
    # Intentionally inject null entries to test downstream imputation routines
    df_sales_raw.loc[df_sales_raw.sample(frac=0.02).index, 'Unit_Price'] = np.nan
    df_sales_raw.loc[df_sales_raw.sample(frac=0.01).index, 'Quantity_Sold'] = np.nan
    df_sales_raw.to_csv('Sales_Log.csv', index=False)
    
    print("✔️ Raw files successfully written to environment disk space.")
    
    # -------------------------------------------------------------------------
    # PHASE 2: ETL INGESTION LAYER (Extracting files back into system)
    # -------------------------------------------------------------------------
    print("\n📥 Phase 2: Ingesting source worksheets into data engine memory...")
    
    sales_path, catalog_path, supplier_path = 'Sales_Log.csv', 'Product_Catalog.xlsx', 'Supplier_Lead_Times.xlsx'
    
    df_sales = pd.read_csv(sales_path)
    df_catalog = pd.read_excel(catalog_path)
    df_supplier = pd.read_excel(supplier_path)
    
    print(f"✔️ Extraction Complete. Processing {len(df_sales)} relational lines.")
    
    # -------------------------------------------------------------------------
    # PHASE 3: TRANSFORMATION ENGINE (Data Cleaning & Normalization)
    # -------------------------------------------------------------------------
    print("\n⚙️ Phase 3: Initiating cleaning & multi-format standardization layers...")
    
    # 1. Structural Casing Standardization to fix relational text fragmentation
    df_sales['Store_Region'] = df_sales['Store_Region'].astype(str).str.upper().str.strip()
    df_sales['Product_ID'] = df_sales['Product_ID'].astype(str).str.upper().str.strip()
    df_catalog['Product_ID'] = df_catalog['Product_ID'].astype(str).str.upper().str.strip()
    df_supplier['Product_ID'] = df_supplier['Product_ID'].astype(str).str.upper().str.strip()
    
    # 2. Temporal Normalization to resolve multi-delimited date strings smoothly
    df_sales['Order_Date'] = pd.to_datetime(df_sales['Order_Date'], errors='coerce', format='mixed')
    
    # 3. Robust Missing Value Imputation (Data Imputation)
    qty_median = df_sales['Quantity_Sold'].median()
    df_sales['Quantity_Sold'] = df_sales['Quantity_Sold'].fillna(qty_median)
    
    product_mean_prices = df_sales.groupby('Product_ID')['Unit_Price'].transform('mean')
    df_sales['Unit_Price'] = df_sales['Unit_Price'].fillna(product_mean_prices)
    
    global_price_median = df_sales['Unit_Price'].median()
    df_sales['Unit_Price'] = df_sales['Unit_Price'].fillna(global_price_median)
    
    # Calculate operational line totals
    df_sales['Line_Revenue'] = df_sales['Quantity_Sold'] * df_sales['Unit_Price']
    
    print("✔️ Relational formatting errors and missing lines corrected.")
    
    # -------------------------------------------------------------------------
    # PHASE 4: RELATIONAL MASTER CONSOLIDATION (Inner Table Merges)
    # -------------------------------------------------------------------------
    print("\n🔗 Phase 4: Consolidating loose data silos via database joins...")
    
    df_master = pd.merge(df_sales, df_catalog, on='Product_ID', how='inner')
    df_master = pd.merge(df_master, df_supplier, on='Product_ID', how='inner')
    
    print(f"✔️ Single master table created successfully. Size: {df_master.shape}.")
    
    # -------------------------------------------------------------------------
    # PHASE 5: ADVANCED SUPPLY CHAIN LOGIC ALGORITHMS
    # -------------------------------------------------------------------------
    print("\n🧠 Phase 5: Computing advanced logistical KPIs and indicators...")
    
    # 1. Compute Inventory Turnover Rate (ITR)
    total_annual_units_sold = df_master.groupby('Product_ID')['Quantity_Sold'].transform('sum')
    df_master['Inventory_Turnover_Rate'] = round(total_annual_units_sold / df_master['Current_Stock_Level'], 2)
    
    # 2. Generate Stock-out Risk Alert Flags
    df_master['Stockout_Risk_Flag'] = np.where(df_master['Current_Stock_Level'] < df_master['Reorder_Point'], 1, 0)
    
    # 3. Implement Dynamic Pareto Principle ABC Categorization Model
    product_revenue_pool = df_master.groupby('Product_ID')['Line_Revenue'].sum().reset_index()
    product_revenue_pool = product_revenue_pool.sort_values(by='Line_Revenue', ascending=False)
    product_revenue_pool['Cumulative_Revenue'] = product_revenue_pool['Line_Revenue'].cumsum()
    grand_total_revenue = product_revenue_pool['Line_Revenue'].sum()
    product_revenue_pool['Revenue_Percentage'] = product_revenue_pool['Cumulative_Revenue'] / grand_total_revenue
    
    def calculate_pareto_abc(percentage):
        if percentage <= 0.80: return 'A'   # Top 80% Core Revenue Drivers
        elif percentage <= 0.95: return 'B' # Mid-Tier 15% Revenue Buffers
        else: return 'C'                    # Tail End 5% Low Margin Items
        
    product_revenue_pool['ABC_Classification'] = product_revenue_pool['Revenue_Percentage'].apply(calculate_pareto_abc)
    abc_lookup_dictionary = product_revenue_pool.set_index('Product_ID')['ABC_Classification'].to_dict()
    df_master['ABC_Classification'] = df_master['Product_ID'].map(abc_lookup_dictionary)
    
    print("✔️ Analytics calculated. Algorithmic segmentation complete.")
    
    # -------------------------------------------------------------------------
    # PHASE 6: SYSTEM EXPORT LAYER
    # -------------------------------------------------------------------------
    print("\n💾 Phase 6: Exporting optimized tracking layer...")
    
    output_filename = 'Clean_Sales_Inventory.csv'
    df_master.to_csv(output_filename, index=False)
    
    print("="*60)
    print(f"🎯 SUCCESS: SYSTEM CALIBRATED & '{output_filename}' COMPILED")
    print("="*60)
    print("File is fully optimized and ready to load directly into your dashboard tab!")

if __name__ == '__main__':
    run_complete_supply_chain_system()

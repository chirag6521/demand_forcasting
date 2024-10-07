import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define file paths for the datasets
customer_demo_file = "data/CustomerDemographics.csv"
product_info_file = "data/ProductInfo.csv"
transaction_file_1 = "data/Transactional_data_retail01.csv"
transaction_file_2 = "data/Transactional_data_retail02.csv"

try:
    # Load Customer Demographics
    logging.info("Loading Customer Demographics data...")
    demographics_df = pd.read_csv(customer_demo_file)
    logging.info(f"Customer Demographics columns: {demographics_df.columns.tolist()}")
    
    # Load Product Information
    logging.info("Loading Product Information data...")
    product_info_df = pd.read_csv(product_info_file)
    logging.info(f"Product Information columns: {product_info_df.columns.tolist()}")
    
    # Load Transaction Data
    logging.info("Loading Transaction data...")
    transactions_df_1 = pd.read_csv(transaction_file_1)
    transactions_df_2 = pd.read_csv(transaction_file_2)
    transactions_df = pd.concat([transactions_df_1, transactions_df_2], ignore_index=True)
    logging.info(f"Transaction Data columns: {transactions_df.columns.tolist()}")

except Exception as e:
    logging.error(f"Error loading data: {str(e)}")

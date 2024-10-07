import numpy as np

try:
    # Convert InvoiceDate to datetime format
    logging.info("Converting InvoiceDate to datetime format...")
    transactions_df['InvoiceDate'] = pd.to_datetime(transactions_df['InvoiceDate'], errors='coerce', dayfirst=True)
    logging.info(f"Sample InvoiceDate after conversion: {transactions_df['InvoiceDate'].head()}")

    # Drop any rows with missing dates
    transactions_df = transactions_df.dropna(subset=['InvoiceDate'])

    # Filter out any transactions with negative or zero quantities
    transactions_df = transactions_df[transactions_df['Quantity'] > 0]

    # Merge transaction data with Product Info based on 'StockCode'
    logging.info("Merging transaction data with product information...")
    merged_df = pd.merge(transactions_df, product_info_df, on='StockCode', how='left')

    # Group data by StockCode and InvoiceDate to aggregate quantities
    logging.info("Grouping data by StockCode and InvoiceDate...")
    grouped_df = merged_df.groupby(['StockCode', 'InvoiceDate']).agg({
        'Quantity': 'sum',      # Summing up quantities for each product per day
        'Price': 'mean'         # Taking average price for each product per day
    }).reset_index()

    logging.info(f"Sample of grouped data: {grouped_df.head()}")

except Exception as e:
    logging.error(f"Error in preprocessing: {str(e)}")

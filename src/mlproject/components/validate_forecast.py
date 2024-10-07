import pandas as pd
from sklearn.metrics import mean_absolute_error

def validate_forecast(predicted_file, actual_file):
    # Load predicted and actual data
    predicted_df = pd.read_csv(predicted_file)
    actual_df = pd.read_csv(actual_file)

    # Merge on StockCode and Date to align predicted and actual values
    merged_df = predicted_df.merge(actual_df, on=['StockCode', 'ds'], suffixes=('_pred', '_actual'))

    # Calculate MAE
    mae = mean_absolute_error(merged_df['yhat'], merged_df['y_actual'])
    
    return mae

if __name__ == "__main__":
    predicted_file = 'data/forecast_results.csv'  # Path to your predicted data
    actual_file = 'data/actual_sales_data.csv'    # Path to your actual sales data
    mae = validate_forecast(predicted_file, actual_file)
    print(f'Mean Absolute Error: {mae}')

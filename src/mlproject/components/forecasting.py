import pandas as pd
import os
import logging
from prophet import Prophet

class Forecasting:
    def __init__(self, processed_data):
        self.data = processed_data

    def forecast_demand(self, stock_code):
        # Filter data for the specific stock code
        stock_data = self.data[self.data['StockCode'] == stock_code]

        # Log the columns to check if 'OrderDate' and 'Quantity' are present
        logging.info(f"Columns in stock data for {stock_code}: {stock_data.columns.tolist()}")

        # Prepare data for Prophet
        try:
            stock_data = stock_data[['OrderDate', 'Quantity']].rename(columns={'OrderDate': 'ds', 'Quantity': 'y'})
        except KeyError as e:
            logging.error(f"KeyError: {str(e)} - Check if 'OrderDate' and 'Quantity' columns exist.")
            return pd.DataFrame()  # Return empty DataFrame

        # Ensure there is enough data for forecasting
        if len(stock_data) < 2:
            logging.warning(f"Not enough data to forecast for Stock Code: {stock_code}")
            return pd.DataFrame()  # Return empty DataFrame

        # Initialize and fit the Prophet model
        model = Prophet()
        model.fit(stock_data)

        # Create a DataFrame for future predictions
        future = model.make_future_dataframe(periods=15)  # Forecast for the next 15 days
        forecast = model.predict(future)

        # Select relevant columns for output
        forecast_output = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        forecast_output['StockCode'] = stock_code  # Add the stock code

        return forecast_output

    def save_forecast_results(self, forecast_output):
        forecast_output_path = os.path.join('data', 'processed', 'forecast_results.csv')

        # Check if the forecast results file already exists
        if os.path.exists(forecast_output_path):
            # Load old forecast results
            old_forecast_df = pd.read_csv(forecast_output_path)
            logging.info(f"Old forecast results loaded: {forecast_output_path}")

            # Merge old and new forecast results
            combined_forecast_df = pd.concat([old_forecast_df, forecast_output], ignore_index=True)
        else:
            combined_forecast_df = forecast_output

        # Save combined forecast results
        try:
            combined_forecast_df.to_csv(forecast_output_path, index=False)
            logging.info(f"Forecast results saved to: {forecast_output_path}")
        except Exception as e:
            logging.error(f"Error saving forecast results: {str(e)}")

# In your main.py, integrate the forecasting functionality like this:

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        # Load the configuration
        config = Configuration().get_config()  # Get the config dictionary

        # Load and preprocess data
        data_ingestion = DataProcessing(config)
        transactions_df, demographics_df, product_info_df = data_ingestion.load_data()
        preprocessed_data = data_ingestion.preprocess_data(transactions_df, product_info_df)

        logging.info("Data ready for forecasting models.")

        # Step 1: Identify the top 10 best-selling stock codes
        top_10_stock_codes = (preprocessed_data.groupby('StockCode')
                              .agg({'Quantity': 'sum'})
                              .sort_values(by='Quantity', ascending=False)
                              .head(10).index.tolist())

        logging.info(f"Top 10 stock codes based on quantity sold: {top_10_stock_codes}")

        # Step 2: Loop through the top 10 stock codes and forecast demand
        forecasting = Forecasting(preprocessed_data)
        forecast_results = pd.DataFrame()

        for stock_code in top_10_stock_codes:
            logging.info(f"Forecasting for Stock Code: {stock_code}")
            result = forecasting.forecast_demand(stock_code)
            forecast_results = pd.concat([forecast_results, result], ignore_index=True)

        # Step 3: Save the forecast results
        forecasting.save_forecast_results(forecast_results)

    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")

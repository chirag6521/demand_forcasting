import pandas as pd
import matplotlib.pyplot as plt

def visualize_forecast(forecast_file):
    # Load the forecast data
    forecast_df = pd.read_csv(forecast_file)

    # Unique stock codes
    stock_codes = forecast_df['StockCode'].unique()

    for stock_code in stock_codes:
        stock_data = forecast_df[forecast_df['StockCode'] == stock_code]
        
        plt.figure(figsize=(10, 5))
        plt.plot(stock_data['ds'], stock_data['yhat'], label='Predicted Demand', color='blue')
        plt.fill_between(stock_data['ds'], stock_data['yhat_lower'], stock_data['yhat_upper'], color='lightblue', alpha=0.5)
        
        plt.title(f'Demand Forecast for Stock Code: {stock_code}')
        plt.xlabel('Date')
        plt.ylabel('Demand')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        
        # Save the plot
        plt.savefig(f'data/forecast_visualization_{stock_code}.png')
        plt.close()

if __name__ == "__main__":
    forecast_file = 'data/forecast_results.csv'  # Path to your forecast results
    visualize_forecast(forecast_file)

import pandas as pd
import requests
import json
 
def convert_sarif_to_dataframe(sarif_file):
    # This function assumes SARIF files are JSON and focuses on specific parts
    df = pd.read_json(sarif_file)
    # Add your specific parsing logic here based on SARIF format
    return df
 
def send_data_to_power_bi(dataframe, power_bi_url):
    records = dataframe.to_dict('records')
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(records)
response = requests.post(power_bi_url, headers=headers, data=data)
    return response
 
# Example usage
sarif_file = 'path/to/result.sarif'
df = convert_sarif_to_dataframe(sarif_file)
power_bi_url = 'your_power_bi_streaming_dataset_url'
response = send_data_to_power_bi(df, power_bi_url)
print('Data uploaded to Power BI:', response.status_code)

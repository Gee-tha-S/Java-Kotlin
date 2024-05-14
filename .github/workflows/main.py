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
power_bi_url = 'https://api.powerbi.com/beta/b945c813-dce6-41f8-8457-5a12c2fe15bf/datasets/49e96d32-1d52-459a-8e8b-09b82ac161d3/rows?referrer=desktop&key=dwVY70XrRwwCZWJWjJcliwhLGgdqErLna6GVAvaWB4E%2BFL5j4NZ58I4mQD3RwG4fJefm8iDXnM1we72OovnswQ%3D%3D'
response = send_data_to_power_bi(df, power_bi_url)
print('Data uploaded to Power BI:', response.status_code)

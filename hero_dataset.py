import pandas as pd
import requests

url = "https://api.opendota.com/api/heroStats"
print("Fetching data from OpenDota servers...")
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)


columns_to_keep = [
    'localized_name',
    'primary_attr',  
    'base_health',   
    'base_armor',    
    'base_str',      
    'base_agi',      
    'base_int',      
    'str_gain',      
    'agi_gain',      
    'int_gain',       
    'move_speed'      
]

df = df[columns_to_keep]

df.to_csv('dota_heroes.csv', index=False)
print("Done! File dota_heroes.csv created successfully.")

import pandas as pd

krotkiNormal = []

def load_data():
    global krotkiNormal
    # 1. Load raw data fetched from API
    df = pd.read_csv('dota_heroes.csv')
    
    # 2. First, drop heroes with missing data (e.g., Kez, Largo)
    df = df.dropna()
    
    # 3. Separate text columns from numerical ones
    text_columns = df[['localized_name', 'primary_attr']]
    numerical_columns = df.drop(columns=['localized_name', 'primary_attr'])
    
    # 4. Safe normalization (preventing division by zero!)
    spread = numerical_columns.max() - numerical_columns.min()
    # If max-min is 0, replace it with 1 to avoid errors
    spread = spread.replace(0, 1)
    
    df_normalized = (numerical_columns - numerical_columns.min()) / spread
    
    # 5. Concatenate text and numerical columns back together
    df_ready = pd.concat([text_columns, df_normalized], axis=1)
    
    # 6. Pack into a list for the K-means algorithm
    krotkiNormal.clear()
    for _, row in df_ready.iterrows():
        tuple_item = list(row)
        tuple_item.append(0)  # Add space for the cluster number at the end (index 11)
        krotkiNormal.append(tuple_item)
        
    print(f"Data loaded! Number of ready heroes: {len(krotkiNormal)}")

def normalize_data():
    # Left empty, because normalization happens automatically in load_data
    pass

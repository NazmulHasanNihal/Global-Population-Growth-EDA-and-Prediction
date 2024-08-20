import pandas as pd

def clean_data(df):
    df['Continent'] = df['Continent'].fillna('Unknown')
    df = df.dropna(subset=['Continent'])
    
    Q1 = df['Growth Rate'].quantile(0.25)
    Q3 = df['Growth Rate'].quantile(0.75)
    IQR = Q3 - Q1

    df[(df['Growth Rate'] < (Q1 - 1.5 * IQR)) | (df['Growth Rate'] > (Q3 + 1.5 * IQR))]
    return df

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_regression

def engineer_features(df):
 
    df['Population Change'] = df['Population (2024)'] - df['Population (2023)']

    categorical_columns = ['City', 'Country', 'Continent']

    encoder = OneHotEncoder(sparse_output=False, drop='first')

    df_encoded = pd.DataFrame(encoder.fit_transform(df[categorical_columns]), 
                              columns=encoder.get_feature_names_out(categorical_columns))

    df_numeric = df.drop(columns=categorical_columns)
    df_combined = pd.concat([df_numeric.reset_index(drop=True), df_encoded.reset_index(drop=True)], axis=1)

    scaler = MinMaxScaler()
    df[['Population (2024)', 'Population (2023)', 'Growth Rate', 'Population Change']] = scaler.fit_transform(
        df[['Population (2024)', 'Population (2023)', 'Growth Rate', 'Population Change']])

    X = df_combined.drop(columns=['Population (2024)'])
    y = df_combined['Population (2024)']

    selector = SelectKBest(score_func=f_regression, k=5)
    X_new = selector.fit_transform(X, y)

    selected_indices = selector.get_support(indices=True)
    selected_features = X.columns[selected_indices]
    
    print("Encoded Features:")
    print(df_combined.head())
    
    print("Selected Features:", selected_features)
    
    return X_new, y


import pandas as pd
from scripts.data_cleaning import clean_data
from scripts.feature_engineering import engineer_features
from scripts.train_model import train_and_save_model
from scripts.evaluate_model import evaluate_model

def main():
    # Loading raw data
    print("Loading raw data...")
    raw_data = pd.read_csv('/workspaces/Global-Population-Growth-EDA-and-Prediction/data/raw/world_population_growth.csv')

    # Cleaning the data
    print("Cleaning data...")
    cleaned_data = clean_data(raw_data)
    
    # Feature engineering
    print("Engineering features...")
    features, target = engineer_features(cleaned_data)
    
    # Training the model
    print("Training model...")
    model = train_and_save_model(features, target)
    
    # Evaluating the model
    print("Evaluating model...")
    evaluation_results = evaluate_model(model, features, target)
    
    print("Pipeline completed successfully.")
    print("Evaluation Results:")
    print(evaluation_results)

if __name__ == "__main__":
    main()

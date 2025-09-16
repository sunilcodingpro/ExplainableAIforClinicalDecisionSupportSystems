# data_preprocessor.py
import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    # Example preprocessing
    df.fillna(0, inplace=True)
    df = pd.get_dummies(df, columns=['gender', 'symptom_1', 'symptom_2'])
    return df

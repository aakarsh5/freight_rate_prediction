from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT/ "data"

def load_train_data() -> pd.DataFrame:
    # Load the labelled training dataset
    return pd.read_csv(DATA_DIR/"train-test.csv")

def load_validation_data() -> pd.DataFrame:
    # Load unlabelled dataset
    return pd.read_csv(DATA_DIR/"validation.csv")

def load_december_data() -> pd.DataFrame:
    # Load the december charts input dataset
    return pd.read_csv(DATA_DIR/"december-chart-inputs.csv")

def load_prediction_template() -> pd.DataFrame:
    # Load the validation prediction template
    return pd.read_csv(DATA_DIR/"validation-predictions-template.csv")

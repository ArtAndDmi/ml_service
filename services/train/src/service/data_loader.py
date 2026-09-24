import pandas as pd

from src.repositories.training_data import get_training_data


def load_training_data() -> pd.DataFrame:
    df = get_training_data()

    if df.empty:
        raise ValueError('Training dataset is empty')

    return df
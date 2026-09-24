import numpy as np
import pandas as pd


def add_geometry_features(
    x: pd.DataFrame,
) -> pd.DataFrame:
    x = x.copy()

    x['volume'] = x['x'] * x['y'] * x['z']
    x['base_area'] = x['x'] * x['y']
    x['xy_ratio'] = x['x'] / x['y'].replace(0, np.nan)

    return x


def drop_xyz(
    x: pd.DataFrame,
) -> pd.DataFrame:
    x = x.copy()

    return x.drop(
        columns=[
            'x',
            'y',
            'z',
        ],
    )
import numpy as np
import pandas as pd


def replace_zero_dimensions_with_nan(
    x: pd.DataFrame,
) -> pd.DataFrame:
    x = x.copy()

    zero_dimensions_mask = (
        x[['x', 'y', 'z']] == 0
    ).all(axis=1)

    x.loc[
        zero_dimensions_mask,
        ['x', 'y', 'z'],
    ] = np.nan

    return x
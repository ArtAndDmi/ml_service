from collections.abc import Callable, Iterable

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    FunctionTransformer,
    OneHotEncoder,
    OrdinalEncoder,
)

from ml_common.constants import (
    CATEGORICAL_FEATURES,
    CLARITY_ORDER,
)
from ml_common.preprocessing.cleaning import (
    replace_zero_dimensions_with_nan,
)
from ml_common.preprocessing.features import (
    add_geometry_features,
    drop_xyz,
)

def make_one_hot_encoder() -> OneHotEncoder:
    return OneHotEncoder(
        handle_unknown='ignore',
        sparse_output=False,
    )


def apply_final_feature_engineering(
    x: pd.DataFrame,
) -> pd.DataFrame:
    x = replace_zero_dimensions_with_nan(x)
    x = add_geometry_features(x)
    x = drop_xyz(x)

    return x


def make_preprocessor(
    categorical_features: Iterable[str] = CATEGORICAL_FEATURES,
    ordinal_clarity: bool = False,
) -> ColumnTransformer:
    categorical_features = list(categorical_features)

    if ordinal_clarity:
        one_hot_features = [
            feature
            for feature in categorical_features
            if feature != 'clarity'
        ]

        return ColumnTransformer(
            transformers=[
                (
                    'onehot',
                    make_one_hot_encoder(),
                    one_hot_features,
                ),
                (
                    'clarity_ordinal',
                    OrdinalEncoder(
                        categories=[CLARITY_ORDER],
                        handle_unknown='use_encoded_value',
                        unknown_value=-1,
                    ),
                    ['clarity'],
                ),
            ],
            remainder='passthrough',
            verbose_feature_names_out=False,
        )

    return ColumnTransformer(
        transformers=[
            (
                'onehot',
                make_one_hot_encoder(),
                categorical_features,
            ),
        ],
        remainder='passthrough',
        verbose_feature_names_out=False,
    )


def make_transformer(
    function: Callable[[pd.DataFrame], pd.DataFrame],
) -> FunctionTransformer:
    return FunctionTransformer(
        func=function,
        validate=False,
    )
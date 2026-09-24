from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.pipeline import Pipeline

from ml_common.constants import RANDOM_STATE
from ml_common.preprocessing.transformer import (
    apply_final_feature_engineering,
    make_preprocessor,
    make_transformer,
)


def create_model() -> Pipeline:
    return Pipeline(
        steps=[
            (
                'feature_engineering',
                make_transformer(
                    apply_final_feature_engineering,
                ),
            ),
            (
                'preprocessing',
                make_preprocessor(
                    ordinal_clarity=True,
                ),
            ),
            (
                'model',
                HistGradientBoostingRegressor(
                    random_state=RANDOM_STATE,
                    learning_rate=0.04,
                    max_iter=250,
                    max_leaf_nodes=63,
                    min_samples_leaf=20,
                ),
            ),
        ],
    )
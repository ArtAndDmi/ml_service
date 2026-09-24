from pathlib import Path
from tempfile import NamedTemporaryFile

import joblib
from sklearn.pipeline import Pipeline


def save_model(
        model: Pipeline,
) -> Path:
    with NamedTemporaryFile(
            suffix='.joblib',
            delete=False,
    ) as temp_file:
        artifact_path = Path(temp_file.name)

    joblib.dump(
        model,
        artifact_path,
    )

    return artifact_path

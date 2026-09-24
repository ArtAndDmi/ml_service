from io import BytesIO

import pandas as pd
from fastapi import HTTPException


def read_csv(content: bytes) -> pd.DataFrame:
    try:
        return pd.read_csv(
            BytesIO(content),
            sep=None,
            engine='python'
        )

    except Exception as error:
        raise HTTPException(
            status_code=422,
            detail='Unable to parse CSV file'
        ) from error
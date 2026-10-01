import pandas as pd
from sqlalchemy.orm import Session

from src.db.models import TrainingData


def append_training_data(
        session: Session,
        df: pd.DataFrame
) -> int:
    records = df.rename(
        columns={'table': 'table_value'}
    ).to_dict(orient='records')

    objects = [
        TrainingData(**record)
        for record in records
    ]

    session.add_all(objects)
    session.commit()

    return len(objects)


def replace_training_data(
        session: Session,
        df: pd.DataFrame
) -> int:
    records = df.rename(
        columns={'table': 'table_value'}
    ).to_dict(orient='records')

    objects = [
        TrainingData(**record)
        for record in records
    ]

    session.query(TrainingData).delete()
    session.add_all(objects)
    session.commit()

    return len(objects)

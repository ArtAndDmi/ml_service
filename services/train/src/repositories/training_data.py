import pandas as pd
from sqlalchemy import text

from src.db.session import engine


def get_training_data() -> pd.DataFrame:
    query = text(
        '''
        SELECT carat,
               depth,
               table_value,
               x,
               y,
               z,
               cut,
               color,
               clarity,
               price
        FROM training_data
        '''
    )

    with engine.connect() as connection:
        df = pd.read_sql(
            query,
            connection,
        ).rename(
            columns={
                'table_value': 'table',
            }
        )

    return df

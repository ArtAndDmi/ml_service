from io import BytesIO

import pandas as pd


REQUIRED_COLUMNS = {
    'carat',
    'depth',
    'table',
    'x',
    'y',
    'z',
    'cut',
    'color',
    'clarity',
    'price',
}

NUMERIC_COLUMNS = {
    'carat',
    'depth',
    'table',
    'x',
    'y',
    'z',
    'price',
}

REQUIRED_NUMERIC_COLUMNS = {
    'carat',
    'price',
}

CATEGORICAL_VALUES = {
    'cut': {
        'Fair',
        'Good',
        'Very Good',
        'Premium',
        'Ideal',
    },
    'color': {
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
    },
    'clarity': {
        'I1',
        'SI2',
        'SI1',
        'VS2',
        'VS1',
        'VVS2',
        'VVS1',
        'IF',
    },
}


def read_csv(content: bytes) -> pd.DataFrame:
    try:
        return pd.read_csv(
            BytesIO(content),
            sep=None,
            engine='python',
        )
    except Exception as error:
        raise ValueError(
            'Unable to parse CSV file'
        ) from error


def parse_and_validate_csv(content: bytes) -> pd.DataFrame:
    df = read_csv(content)

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            {
                'message': 'CSV has invalid structure',
                'missing_columns': sorted(missing_columns),
            }
        )

    for column in NUMERIC_COLUMNS:
        original_values = df[column]

        converted_values = pd.to_numeric(
            original_values,
            errors='coerce',
        )

        invalid_values = (
            converted_values.isna()
            & original_values.notna()
        )

        if invalid_values.any():
            raise ValueError(
                {
                    'message': 'CSV contains invalid numeric values',
                    'column': column,
                }
            )

        df[column] = converted_values

    for column in REQUIRED_NUMERIC_COLUMNS:
        if df[column].isna().any():
            raise ValueError(
                {
                    'message': 'CSV contains null values',
                    'column': column,
                }
            )

    if (df['carat'] <= 0).any():
        raise ValueError(
            {
                'message': 'CSV contains invalid values',
                'column': 'carat',
                'constraint': 'must be greater than 0',
            }
        )

    if (df['price'] <= 0).any():
        raise ValueError(
            {
                'message': 'CSV contains invalid values',
                'column': 'price',
                'constraint': 'must be greater than 0',
            }
        )

    for column in ('depth', 'table'):
        invalid_values = (
            df[column].notna()
            & (
                (df[column] <= 0)
                | (df[column] >= 100)
            )
        )

        if invalid_values.any():
            raise ValueError(
                {
                    'message': 'CSV contains invalid values',
                    'column': column,
                    'constraint': 'must be between 0 and 100',
                }
            )

    for column in ('x', 'y', 'z'):
        invalid_values = (
            df[column].notna()
            & (df[column] < 0)
        )

        if invalid_values.any():
            raise ValueError(
                {
                    'message': 'CSV contains invalid values',
                    'column': column,
                    'constraint': 'must be greater than or equal to 0',
                }
            )

    for column in ('cut', 'color', 'clarity'):
        if df[column].isna().any():
            raise ValueError(
                {
                    'message': 'CSV contains null values',
                    'column': column,
                }
            )

        invalid_values = ~df[column].isin(
            CATEGORICAL_VALUES[column]
        )

        if invalid_values.any():
            raise ValueError(
                {
                    'message': 'CSV contains invalid categorical values',
                    'column': column,
                    'allowed_values': sorted(
                        CATEGORICAL_VALUES[column]
                    ),
                }
            )

    return df
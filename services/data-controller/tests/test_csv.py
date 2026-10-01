import pytest

from src.service.csv import parse_and_validate_csv


VALID_CSV = """carat,depth,table,x,y,z,cut,color,clarity,price
0.5,61.5,55.0,5.1,5.15,3.16,Ideal,E,SI1,1000
"""


def test_parse_and_validate_csv_success():
    df = parse_and_validate_csv(
        VALID_CSV.encode()
    )

    assert len(df) == 1
    assert df.iloc[0]['carat'] == 0.5
    assert df.iloc[0]['cut'] == 'Ideal'


def test_parse_and_validate_csv_rejects_missing_column():
    csv = """carat,depth,table,x,y,z,cut,color,price
0.5,61.5,55.0,5.1,5.15,3.16,Ideal,E,1000
"""

    with pytest.raises(ValueError) as error:
        parse_and_validate_csv(
            csv.encode()
        )

    detail = error.value.args[0]

    assert detail['message'] == 'CSV has invalid structure'
    assert detail['missing_columns'] == ['clarity']


def test_parse_and_validate_csv_rejects_negative_carat():
    csv = """carat,depth,table,x,y,z,cut,color,clarity,price
-0.5,61.5,55.0,5.1,5.15,3.16,Ideal,E,SI1,1000
"""

    with pytest.raises(ValueError) as error:
        parse_and_validate_csv(
            csv.encode()
        )

    detail = error.value.args[0]

    assert detail['column'] == 'carat'
    assert detail['constraint'] == 'must be greater than 0'


def test_parse_and_validate_csv_rejects_invalid_numeric_value():
    csv = """carat,depth,table,x,y,z,cut,color,clarity,price
0.5,invalid,55.0,5.1,5.15,3.16,Ideal,E,SI1,1000
"""

    with pytest.raises(ValueError) as error:
        parse_and_validate_csv(
            csv.encode()
        )

    detail = error.value.args[0]

    assert detail['message'] == 'CSV contains invalid numeric values'
    assert detail['column'] == 'depth'


def test_parse_and_validate_csv_rejects_invalid_category():
    csv = """carat,depth,table,x,y,z,cut,color,clarity,price
0.5,61.5,55.0,5.1,5.15,3.16,Something,E,SI1,1000
"""

    with pytest.raises(ValueError) as error:
        parse_and_validate_csv(
            csv.encode()
        )

    detail = error.value.args[0]

    assert detail['message'] == 'CSV contains invalid categorical values'
    assert detail['column'] == 'cut'


def test_parse_and_validate_csv_rejects_null_carat():
    csv = """carat,depth,table,x,y,z,cut,color,clarity,price
,61.5,55.0,5.1,5.15,3.16,Ideal,E,SI1,1000
"""

    with pytest.raises(ValueError) as error:
        parse_and_validate_csv(
            csv.encode()
        )

    detail = error.value.args[0]

    assert detail['message'] == 'CSV contains null values'
    assert detail['column'] == 'carat'


def test_parse_and_validate_csv_rejects_invalid_depth():
    csv = """carat,depth,table,x,y,z,cut,color,clarity,price
0.5,101,55.0,5.1,5.15,3.16,Ideal,E,SI1,1000
"""

    with pytest.raises(ValueError) as error:
        parse_and_validate_csv(
            csv.encode()
        )

    detail = error.value.args[0]

    assert detail['message'] == 'CSV contains invalid values'
    assert detail['column'] == 'depth'


def test_parse_and_validate_csv_allows_nullable_dimensions():
    csv = """carat,depth,table,x,y,z,cut,color,clarity,price
0.5,,,,,,Ideal,E,SI1,1000
"""

    df = parse_and_validate_csv(
        csv.encode()
    )

    assert len(df) == 1
    assert df.iloc[0]['carat'] == 0.5
    assert df.iloc[0]['depth'] != df.iloc[0]['depth']
    assert df.iloc[0]['table'] != df.iloc[0]['table']
    assert df.iloc[0]['x'] != df.iloc[0]['x']
    assert df.iloc[0]['y'] != df.iloc[0]['y']
    assert df.iloc[0]['z'] != df.iloc[0]['z']
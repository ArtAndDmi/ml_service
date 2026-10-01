from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from src.db.session import get_session
from src.repositories.training_data import (
    append_training_data,
    replace_training_data,
)
from src.schemas import LoadDataResponse
from src.service import parse_and_validate_csv

router = APIRouter(prefix='/data')


def parse_csv(content: bytes):
    try:
        return parse_and_validate_csv(content)
    except ValueError as error:
        detail = error.args[0] if error.args else 'Invalid CSV file'

        raise HTTPException(
            status_code=422,
            detail=detail,
        ) from error


@router.post('/replace', response_model=LoadDataResponse)
async def replace_data(
        file: UploadFile = File(...),
        session: Session = Depends(get_session)
):
    content = await file.read()

    df = parse_csv(content)

    rows_loaded = replace_training_data(
        session=session,
        df=df,
    )

    return {
        'filename': file.filename,
        'rows_received': rows_loaded,
        'status': 'received'
    }


@router.post('/append', response_model=LoadDataResponse)
async def append_data(
        file: UploadFile = File(...),
        session: Session = Depends(get_session)
):
    content = await file.read()

    df = parse_csv(content)

    rows_loaded = append_training_data(
        session=session,
        df=df,
    )

    return {
        'filename': file.filename,
        'rows_received': rows_loaded,
        'status': 'received'
    }
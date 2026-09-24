from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session

from src.service import read_csv
from src.db.session import get_session
from src.repositories.training_data import insert_training_data
from src.schemas import LoadDataResponse

router = APIRouter(prefix='/data')

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
    'price'
}


@router.post('/upload', response_model=LoadDataResponse)
async def upload_data(
        file: UploadFile = File(...),
        session: Session = Depends(get_session)
):
    content = await file.read()
    df = read_csv(content)

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise HTTPException(
            status_code=422,
            detail={
                'message': 'CSV has invalid structure',
                'missing_columns': sorted(missing_columns)
            }
        )

    rows_loaded = insert_training_data(
        session=session,
        df=df
    )

    return {
        'filename': file.filename,
        'rows_received': rows_loaded,
        'status': 'received'
    }

from fastapi import APIRouter
from src.db.session import check_connection

router = APIRouter(prefix='/health')


@router.get('')
async def health():
    return {
        'status': 'ok',
        'db_status': check_connection(),
        'service': 'data-controller'
    }

from fastapi import APIRouter

router = APIRouter(prefix='/data')

@router.post('/submit')
def post_submit():
    pass

@router.get('/stats')
def get_stats():
    pass

@router.get('/predict')
def get_predict():
    pass

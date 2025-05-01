from fastapi import APIRouter

router = APIRouter(prefix='/auth')

@router.post('/signup')
def post_signup():
    pass

@router.post("/signin")
def post_signin():
    pass

@router.post('/signout')
def post_signout():
    pass

@router.patch('/me')
def patch_me():
    pass
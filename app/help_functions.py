from fastapi import Depends, HTTPException,status
import jwt
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidTokenError
from app.models.schema import bracelets_pools, managers_pools
from app.models.models import TokenData
from app.database import get_db
from sqlalchemy import delete
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

#this for the password encryption
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

#for token ceration and  handling
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')


#f you’re calling delete_rows_by_pool_id inside a FastAPI route, FastAPI will inject the session argument automatically
# from the dependency injection (via Depends(get_db))
def delete_rows_by_pool_id(pool_id_to_delete: int, session: Session = Depends(get_db)):
    """"

    """
    try:
        stmt = delete(bracelets_pools).where(bracelets_pools.c.pool_id == pool_id_to_delete)
        result = session.execute(stmt)
        session.commit()
        affected_rows = result.rowcount

        print(f"Deleted {affected_rows} row(s) with pool_id = {pool_id_to_delete}")

    except Exception as e:
        # Roll back the changes if an error occurs
        session.rollback()
        print(f"Error deleting rows: {e}")

def delete_bracelets_by_code(brac_code_delete: int , session: Session= Depends(get_db)):
    try:
        query = delete(bracelets_pools).where(bracelets_pools.c.bracelet_code == brac_code_delete)
        result = session.execute(query)
        session.commit()
        affected_rows = result.rowcount
        print(f"Deleted {affected_rows} row(s) with bracelets cpde = {brac_code_delete}")
    except Exception as e:
        # Roll back the changes if an error occurs
        session.rollback()
        print(f"Error deleting rows: {e}")


def delete_manager_by_id_from_manager_pool(manager_id_to_delete: int, session: Session = Depends(get_db)):
    try:
        stmt = delete(managers_pools).where(managers_pools.c.manager_id == manager_id_to_delete)
        result = session.execute(stmt)
        session.commit()
        affected_rows = result.rowcount

        print(f"Deleted {affected_rows} row(s) with manager_id = {manager_id_to_delete}")

    except Exception as e:
        # Roll back the changes if an error occurs
        session.rollback()
        print(f"Error deleting rows: {e}")


def delete_pool_from_pool_manager_table(pool_id_to_delete: int, session: Session = Depends(get_db)):
    try:
        stmt = delete(managers_pools).where(managers_pools.c.pool_id == pool_id_to_delete)
        result = session.execute(stmt)
        session.commit()
        affected_rows = result.rowcount

        print(f"Deleted {affected_rows} row(s) with pool_id = {pool_id_to_delete}")

    except Exception as e:
        # Roll back the changes if an error occurs
        session.rollback()
        print(f"Error deleting rows: {e}")


def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")

        if email is None:
            raise credentials_exception
        token_data = TokenData(email = email)
    except InvalidTokenError:
        raise credentials_exception

    return token_data

def get_current_user(token: str = Depends(oauth2_schema)):
    credentials_exception = HTTPException( status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_access_token(token, credentials_exception)





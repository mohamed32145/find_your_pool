from fastapi import Depends

from app.models.schema import bracelets_pools, managers_pools
from app.database import get_db
from sqlalchemy import delete
from sqlalchemy.orm import Session


#f you’re calling delete_rows_by_pool_id inside a FastAPI route, FastAPI will inject the session argument automatically
# from the dependency injection (via Depends(get_db))
def delete_rows_by_pool_id(pool_id_to_delete: int, session: Session = Depends(get_db)):
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




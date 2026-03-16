from fastapi import HTTPException, Body, APIRouter, Depends
from src.models import SessionDep, Task
from src.auth import validate_login
from typing import Annotated


task_route = APIRouter(tags=["task_management"])


@task_route.post("/create_task")
def create_task( db: SessionDep, login_info: Annotated[str, Depends(validate_login)], data= Body(...) ):
      
    task_title = data.get("title")
    description = data.get("description")
    status = data.get("status") if data.get("status") else False
    data_to_add_in_db = Task(user_username=login_info, title=task_title, description=description, status=status)
    db.add(data_to_add_in_db)
    db.commit()
    return {"message": "Task created successfully."}


@task_route.patch("/update_task/{task_id}")
def update_task(task_id, db: SessionDep, login_info: Annotated[str, Depends(validate_login)], data= Body(...) ):

    db_data = db.query(Task).filter( Task.user_username == login_info ).filter(Task.id == task_id).first()
    if not db_data:
        return HTTPException(409, "Given Task ID is not available or not attached to this user.")

    if data.get("title"):
        db_data.title = data.get("title")

    if data.get("description"):
        db_data.description = data.get("description")

    if data.get("status"):
        db_data.status = data.get("status")
    
    db.add(db_data)
    db.commit()
    
    return {"message": "Task Updated successfully."}

@task_route.get("/read_tasks")
def read_task(db: SessionDep, login_info: Annotated[str, Depends(validate_login)]):
      
    db_data = db.query(Task).filter( Task.user_username == login_info ).all()

    return {"message": db_data}

@task_route.delete("/delete_task/{task_id}")
def delete_task(task_id, db: SessionDep, login_info: Annotated[str, Depends(validate_login)]):
      
    db_data = db.query(Task).filter( Task.user_username == login_info ).filter(Task.id == task_id).first()
    if not db_data:
        return HTTPException(409, "Given Task ID is not available or not attached to this user.")

    db.delete(db_data)
    db.commit()
    
    return {"message": "Task Deleted successfully."}


# {
# "title": "Wake at 6AM",
# "description": "I will wake at 6 am and had my breakfast."
# }

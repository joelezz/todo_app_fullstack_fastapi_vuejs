from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, text

app = FastAPI()

#Security middleware, authorisation of web traffic from client to api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #This is for testing and for a local setup. If you will put this to production, change it to allow just the right connections
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Establish the database engine
engine = create_engine("sqlite+pysqlite:///mydb.db", echo=True)

#Database schema
class TaskModel(BaseModel):
    description: str

#Tasks endpoint of the api, for the get calls
@app.get("/tasks")
def get_tasks():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM tasks"))
        tasks = [
            {"id": row[0], "description": row[1], "is_done": bool(row[2])}
            for row in result.fetchall()
        ]
    return tasks

#Tasks endpoint of the api, for the post calls
@app.post("/tasks")
def add_task(task: TaskModel):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO tasks (description, is_done) VALUES (:description, :is_done)"),
            {"description": task.description, "is_done": 0}
        )
    return {"message": f"✅ Your task '{task.description}' has been added!"}

#This endpoint upodates the task status to "done"
@app.put("/tasks/{task_id}/done")
def mark_done(task_id: int):
    with engine.begin() as conn:
        result = conn.execute(
            text("UPDATE tasks SET is_done = 1 WHERE id = :task_id"),
            {"task_id": task_id}
        )
    if result.rowcount == 0:
        return {"error": "❌ Task ID not found."}
    return {"message": f"✅ Task {task_id} marked as done!"}

from typing import Union
import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    student_df = pd.read_csv('../part6/students1.csv')
    return {"count":len(student_df)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/students/{student_id}")
def read_student(student_id: int):
    student_df = pd.read_csv('../part6/students1.csv')
    return student_df.loc[student_df['Id']==student_id ].to_dict()
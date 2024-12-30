import pandas as pd

students = pd.read_json("./part5/students.json")
students['major'].replace({'DSS':'DS'," SE":"SE"},inplace=True)

students.to_json("./part5/students_cleaned.json",orient="records")
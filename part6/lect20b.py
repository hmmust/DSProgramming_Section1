import pandas as pd

def read_students(filename):
    student_df = pd.DataFrame()
    df = pd.read_csv(filename,chunksize=1)
    for d in df:
        student_df = pd.concat([student_df, d])
    return student_df
print(read_students('./part6/students1.csv'))
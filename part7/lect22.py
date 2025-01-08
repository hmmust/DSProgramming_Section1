import pandas as pd
import multiprocessing
import requests

def read_students(filename):
    get_result = requests.get(url=filename)
    if get_result:
        student_df = pd.DataFrame(get_result.json())
        return student_df
    else:
        pd.DataFrame()
if __name__== "__main__":
    pool = multiprocessing.Pool(processes=2)
    df1 = pool.apply_async(read_students,args=("https://rawq.githubusercontent.com/hmmust/DSProgramming_Section1/refs/heads/main/part6/students1.json",))
    df2 = pool.apply_async(read_students,args=("https://raw.githubusercontent.com/hmmust/DSProgramming_Section1/refs/heads/main/part6/students2.json",))
    pool.close()
    pool.join()
    students_df = pd.concat([df1.get(),df2.get()],axis=0,ignore_index=True)
    print(students_df)


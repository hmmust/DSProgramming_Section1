import pandas as pd
import multiprocessing

def read_students(filename):
    student_df = pd.DataFrame()
    df = pd.read_csv(filename,chunksize=1)
    for d in df:
        student_df = pd.concat([student_df, d])
    return student_df
if __name__== "__main__":
    pool = multiprocessing.Pool(processes=2)
    df1 = pool.apply_async(read_students,args=('./part6/students1.csv',))
    df2 = pool.apply_async(read_students,args=('./part6/students2.csv',))
    pool.close()
    pool.join()
    students_df = pd.concat([df1.get(),df2.get()],axis=0,ignore_index=True)
    print(students_df)


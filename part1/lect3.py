def square(n):
    return n**2

def squares(n):
    for i in range(1,n+1):
        yield i**2

students = ('Khalid','Fuad','Raghad','Dana')
for i in squares(9):
    print(i)

    
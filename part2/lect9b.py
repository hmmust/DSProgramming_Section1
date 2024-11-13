import numpy as np
import numpy.random as rd
import string

print(list(string.ascii_letters))
print(list(string.ascii_lowercase))
print(list(string.digits))
print(list(string.punctuation))

print("".join(rd.choice(list(string.ascii_letters),size=5)))

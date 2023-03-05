from Operations import *
import operator as op

expression = input().split()
print(f"{calc(*expression):.2f}")
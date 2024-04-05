#gross salary calculation
n=float(input("enter basic salary: "))

def gross(n):
  g=n+0.1*n+0.12*n
  return g

gross(n)
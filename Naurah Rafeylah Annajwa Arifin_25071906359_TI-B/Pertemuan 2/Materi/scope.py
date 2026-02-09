#local scope
def myfunc():
  x = 300
  print(x)

myfunc()

#lambda
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#recursion
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)
#pemanggilan terhadap diri sendiri

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1 #mengembalikan nilai 1 kedalam fungsi (tipe data)
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))
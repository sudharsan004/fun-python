#Enter a number to find if the number is fizz,buzz or normal number
n=int(input("Enter a number-I"))
def fizzbuzz(n):
    if (n%3==0 and n%5==0):
        print(str(n)+"=Fizz Buzz")
    elif (n%3==0):
        print(str(n)+"=Fizz")
    elif (n%5==0):
        print(str(n)+"=Buzz")
    else:
        print(str(n)+"=Not Fizz or Buzz")
fizzbuzz(n)
#define a function


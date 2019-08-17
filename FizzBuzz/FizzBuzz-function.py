n=int(input("Enter a number"))
#function definition
def fizzbuzz(n):   
    for i in range(1,n+1):
        if (i%3==0 and i%5==0):
            print(str(i)+"=Fizz Buzz")
        elif (i%3==0):
            print(str(i)+"=Fizz")
        elif (i%5==0):
            print(str(i)+"=Buzz")
        else:
            print(str(i))
#function call
fizzbuzz(n)




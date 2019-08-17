n=int(input("Enter limit upto which you want the game to go on:")
for i in range(1,n+1):
    if(i%3==0):
        print("Fizz")
    else:
        if(i%5==0):
            print("buzz")
    if(i%3==0 and i%5==0):
        print("Fizz Buzz")
    else:
        print(i)

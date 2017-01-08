import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def F(n):
    #Calculate up to the nth number in the Fibonacci sequence
    #Print text according to value

    if n is None or n <= 0:
        return

    n_1 = 1
    n_2 = 0
    for i in range (0,n):
        if i ==0:
            answer = 0
        elif i ==1:
            answer = 1
        else:
            answer = n_1 + n_2
            n_2 = n_1
            n_1 = answer
        logging.debug('Answer = '+ str(answer))

        div3 = False
        div5 = False
        #Print custom text
        #If answer satisfies multiple conditions, print all of them
        if (answer >= 3) and (answer%3 == 0):
            print ("Buzz")
            div3 = True
        if (answer >= 5) and (answer%5 == 0):
            print ("Fizz")
            div5 = True
        if div3 and div5:
            print ("FizzBuzz")
        if isprime(answer):
            print ('BuzzFizz')
        else:
            print (answer)

def isprime (n):
    #Return True if n is a prime number
    if n <=1:
        return False
    if n == 2:
        return True
    for i in range (2,int(n**0.5) +1):
        if n%i == 0:
            return False
    return True

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))


def sum(n):
    if n == 0:
        return 0 
    else:
        return n+sum(n-1)

print(sum(2))




new_list = [1 , 2, 3 ,4 ,5]




def num_checker(num , index ):
    if index == len(new_list):
        return "not found"
    elif num == new_list[index]:
        return "found at index : " + str(index)
    else:
        return num_checker(num , index+1)

print(num_checker(4 , 0))

def fibonacci_checker(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_checker(n-1)+fibonacci_checker(n-2)

print(fibonacci_checker(6))




   
        


    






  

    
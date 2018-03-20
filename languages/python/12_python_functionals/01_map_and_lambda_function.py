cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    fib_list = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:    
        while len(fib_list) < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list
    # return a list of fibonacci numbers
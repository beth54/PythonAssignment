
import functools
import time
import matplotlib.pyplot as plt


@functools.lru_cache

def fib(n: int) -> int:
    sequence = [1,1] #initialize fibonacci sequence, 
    x = [] #in which fibonacci numbers will be stored
    y = [] #in which times to compute will be stored

    #plots the map
    def plotting(xcoord, ycoord):
         plt.plot(xcoord, ycoord)
         plt.show()

    #timer function, times how long it takes to compute number
    def timer(function): 
        def wrapper(*args, **kwargs): #wrapper for the timer function
            t1 = time.process_time()
            result = function(*args, **kwargs)
            t2 = time.process_time()
            y.append(t2) #append time expended to list of coordinates
            print(f', executed in {(t2-t1):0.8f}s')
            return {result}
        return wrapper
    
    @timer 
    #computes next number in fibonacci sequence, called recursively
    def numbers(n):
            sum = sequence[number+1] + sequence[number] #determine current number
            sequence.append(sum) #append this number to list of fibonacci numbers
            print(f'({number + 1}) -> {sequence[number]}', end= "")
            x.append(number) #append original number to list of x coordinates
            return sequence[number + 1]
            
    for number in range(n): #for numbers in range of the given number, execute fibonacci calculation
        numbers(n)    
    
    plotting(x,y)

         
    
if __name__ == "__main__":
    fib(100)
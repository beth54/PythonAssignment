# PythonAssignment

In the code folder, there are two Python files.
echo.py produces an "echo" that returns the last 3 letters of an input string, then the last two, then the last one.

![echo.py output](img/echo_py_output.png)

The second file, fib.py, calculates every number in the fibonacci sequence up to the 100th number, printing each one. It also uses a timer decorator function to determine the amount of time it takes to calculate each number.

![fib.py output](img/fib_py_terminal_output.png)

Additionally, the code outputs a graph that shows the cumulative amount of time taken to calculate all numbers in the sequence.
![Fibonacci graph](img/Graph_Output.png)

The code works by having a main function call upon another function that has timer, calculation, and graphing functions inside it. First, the code calculates the number, while timing how long it takes. Then, the index of the fibonacci number and the total time are stored in a list, which is then used to create a graph.

![Fibonacci code](img/fib_py_main_function.png)

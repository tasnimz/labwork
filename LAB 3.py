##LAB 3
##TASK 1
##TASK 2
##TASK 3
st = []; 
  
# Function to push digits into stack 
def push_digits(number): 
  
    while (number != 0):  
        st.append(number % 10); 
        number = int(number / 10); 
  
# Function to reverse the number 
def reverse_number(number): 
      
    # Function call to push number's  
    # digits to stack 
    push_digits(number); 
      
    reverse = 0; 
    i = 1; 
      
    # Popping the digits and forming  
    # the reversed number 
    while (len(st) > 0):  
        reverse = reverse + (st[len(st) - 1] * i); 
        st.pop(); 
        i = i * 10; 
      
    # Return the reversed number formed 
    return reverse; 
  
# Driver Code 
number = 39997; 
  
# Function call to reverse number 
print(reverse_number(number)); 
  
# This code is contributed by mits 
    
##TASK 4
def check(my_string): 
    brackets = ['()', '{}', '[]'] 
    while any(x in my_string for x in brackets): 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    return not my_string 
   
# Driver code 
string = "{[]{()}}"
print(string, "-", "Balanced" 
      if check(string) else "Unbalanced") 

##TASK 5
##TASK 6
from queue import Queue  
  
# Utility function to print the queue  
def Print(queue): 
    while (not queue.empty()): 
        print(queue.queue[0], end = ", ")  
        queue.get() 
  
# Function to reverse the queue  
def reversequeue(queue): 
    Stack = []  
    while (not queue.empty()):  
        Stack.append(queue.queue[0])  
        queue.get() 
    while (len(Stack) != 0):  
        queue.put(Stack[-1])  
        Stack.pop() 
  
# Driver code  
if __name__ == '__main__': 
    queue = Queue() 
    queue.put(10)  
    queue.put(20)  
    queue.put(30)  
    queue.put(40)  
    queue.put(50)  
    queue.put(60)  
    queue.put(70)  
    queue.put(80)  
    queue.put(90)  
    queue.put(100)  
  
    reversequeue(queue)  
    Print(queue) 
  

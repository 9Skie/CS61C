On the contrary, there are global variables, you can define variables outside of functions, and call them into the functions when needed.

```c
// Global variable  
int x = 5;  
  
void myFunction() {  
  printf("%d\n", ++x); // Increment the value of x by 1 and print it  
}  
  
int main() {  
  myFunction();  
  
  printf("%d\n", x); // Print the global variable x  
  return 0;  
}  
  
// The value of x is now 6 (no longer 5)
```

However... it is usually a good idea to not use global variables, unless there's a really good reason to do so.

> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=252&selection=17,0,35,47&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.223]]
> > Many C programmers rely far too much on external variables. One common abuse: using the same external variable for different purposes in different functions. Suppose that several functions need a variable named i to control a for statement. Instead of declaring i in each function that uses it, some programmers declare it at the top of the program, thereby making the variable visible to all functions. This practice is poor not only for the reasons listed earlier, but also because it’s misleading; someone reading the program later may think that the uses of the variable are related, when in fact they’re not.



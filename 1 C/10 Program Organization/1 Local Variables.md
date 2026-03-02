A variable created inside a function belong to the *local scope* of the function, and can only be used inside that function.

```c
void myFunction() {  
  // Local variable that belongs to myFunction  
  int x = 5;  
  
  // Print the variable x  
  printf("%d", x);  
}  
  
int main() {  
  myFunction();  
  return 0;  
}
```

If you do try to access it outside of the function it belongs to, an error occurs.

```c
void myFunction() {  
  // Local variable that belongs to myFunction  
  int x = 5;  
}  
  
int main() {  
  myFunction();  
  
  // Print the variable x in the main function  
  printf("%d", x);  
  // This will raise an error
  return 0;  
}
```

A local variable has a `block scope`, scope being the portion of the program which the variable can be referenced, it is only visible from it's point of declaration the end of the enclosing function body.


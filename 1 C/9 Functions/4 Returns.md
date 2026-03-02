## Return Values

Just like how the `main` function returns a value of `0` by default, functions can also return a value, which needs a data type specified.

```c
int myFunction(int x) {  
  return 5 + x;  
}  
  
int main() {  
  printf("Result is: %d", myFunction(3));  
  return 0;  
}  
  
// Outputs 8 (5 + 3)
```

Of course, you can store the returned results in a variable.

```c
int myFunction(int x, int y) {  
  return x + y;  
}  
  
int main() {  
  int result = myFunction(5, 3);  
  printf("Result is = %d", result);  
  return 0;  
}  
// Outputs 8 (5 + 3)
```
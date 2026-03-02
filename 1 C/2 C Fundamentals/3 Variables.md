In python, variables have been massively simplified, users could type something like this and call it a day.

```python
x = 5
```

But as we know, every data has a type, and in C, when you want to assign data to variables, you must specify a type for the variable.

```c
int x;
x = 5;
```

As you see, there were 2 steps in that process, this is because C's compiler treats the creation of a variable separate that of a variable's assignment of data.

---
### Declaration

Variables must be declared before they can be used, and to declare a variable requires it's type, and it's name

```c
int x; // (type) (name)
```

There's a lot of data types, and their respective syntax for declaring the, here's a mini program containing some of some main ones.

```c
#include <stdio.h>

int main()
{
    // integer
    int age = 20;

    // floating-point
    float height = 5.7;

    // double-precision floating-point
    double pi = 3.14159;

    // character
    char grade = 'A';

    return 0;
}
```

You can also declare multiple variables in 1 line.

```c
int x, y, z;
```

---
### Assignment

```c
x = 5;
```

Assignment must come after declaration, and the data type of the assigned data must match with the variable's declared data type.

Sadly, you can't assign multiple variables in 1 line.

---
## Printing the Value of a Variable

we can use `printf` to print out the current value of a variable.

But different data types require different formatting in `printf` to print them out, this is called data specifiers.

```c
// Defining the variable
int height;
height = 5;

printf("Height: %d", height)
```

> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=48&selection=135,0,177,58&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.19]]
> > %d is a placeholder indicating where the value of height is to be filled in during printing. Note the placement of \n just after %d, so that printf will advance to the next line after printing the value of height. %d works only for int variables; to print a float variable, we’d use %f instead. By default, %f displays a number with six digits after the decimal point.
> 
> 

```c
// Defining the variables
int height;
height = 5;

float weight;
weight = 76;

printf("Height: %d, Weight: %f\n", height, weight)
```

Different data types use different format specifiers, like `%d` or `%i` for `int`.

```c
// Create variables  
int myNum;
myNum = 15;            // Integer (whole number)  

float myFloatNum 
myFloatNum = 5.99;   // Floating point number  

char myLetter;
myLetter = 'D';       // Character  

  
// Print variables  
printf("%d\n", myNum);  
printf("%f\n", myFloatNum);  
printf("%c\n", myLetter);
```

---
### Initialization

Writing 2 lines just to:
- define a variable
- define it's it's data type
- then assign a value to it 

Is a rather cumbersome process, instead, you can just initialize a variable's type and value directly in 1 line.

```c
int height = 8;
```

In C, the value 8 is an 'initializer', you can initialize variables from the value of other variables, like here, we calculated area by initializing it's value from length and width

```c
#include <stdio.h>

int main() {
  int length = 8;
  int width = 10;
  int area = length * width;
  printf("Area is: %i", area);

  return 0;
}
```

---

### Reading Input

But, what if we wanted the user to input the dimensions of width instead of having to manually change it in the code before it compiles? We can do that with another function called `scanf`.



---
### Identifiers

As we can give names to variables, we can also give names to functions, files... etc, this is just a little reminder of things you can and can't do while naming things.

1. C treats upper-case and lower-case differently

```c
// These are all different variables!
int job = 1;
int Job = 2;
int JOB = 3;
```

2. You cannot have your names (identifiers) be these things called 'keywords'

![[Pasted image 20260126201846.png|500]]


All of them have special meanings in C! And the C compiler will treat these keywords by their special meaning! So don't name anything this way.
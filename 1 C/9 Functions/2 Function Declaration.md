While we have learnt about declaring a function this way:

```c
// Create a function  
void myFunction() {  
  printf("I just got executed!");  
}  
  
int main() {  
  myFunction(); // call the function  
  return 0;  
}
```

A function actually consists of 2 parts:
- **Declaration:** the function's name, return type, and parameters (if any)
- **Definition:** the body of the function (code to be executed)

```c
void myFunction() { // declaration 
  // the body of the function (definition)  
}
```

And just like we have type conversions between data types, there's also:
- implicit declaration of functions
- explicit declaration of functions

---
## Implicit Declaration

Suppose we look at this code:

```c
#include <stdio.h> 
int main(void){ 
	double x = 2.1, y=3.4, z=5.5; 
	
	printf("Average of %g and %g: %g\n", x, y, average(x, y));
	printf("Average of %g and %g: %g\n", y, z, average(y, z)); 
	return 0; 
} 
	
double average(double a, double b){
	return (a + b) / 2;
}
```

> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=220&selection=93,0,120,5&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.191]]
> > When the compiler encounters the first call of average in main, it has no information about average: it doesn’t know how many parameters average has, what the types of these parameters are, or what kind of value average returns. Instead of producing an error message, though, the compiler assumes that average returns an int value

This, is an implicit declaration.

---
## Explicit Function Declarations

So... obviously, we would like to declare our functions first so C knows what it's calling.

It basically looks like the line of a function's definition.

```c
return_type name(parameters);
```

And we can include that declaration in front in our C example file.

```c
#include <stdio.h> 

double average(double a, double b); /* DECLARATION */

int main(void){ 
	double x = 2.1, y=3.4, z=5.5; 
	
	printf("Average of %g and %g: %g\n", x, y, average(x, y));
	printf("Average of %g and %g: %g\n", y, z, average(y, z)); 
	return 0; 
} 
	
double average(double a, double b){ /* DEFINITION */
	return (a + b) / 2;
}
```


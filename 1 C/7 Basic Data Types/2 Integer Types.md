We've known about them when looking at how data types are represented in binary, so I'm not going to retell the story again of unsigned, signed integers.

> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=155&selection=38,0,58,8&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.126]]
> > C’s integer types come in different sizes. The int type is usually 32 bits, but may be 16 bits on older CPUs. Since some programs require numbers that are too large to store in int form, C also provides long integers. At times, we may need to conserve memory by instructing the compiler to store a number in less space than normal; such a number is called a short integer.

Here is a table denoting for the range of different integer types 

![[Pasted image 20260207200938.png|500]]

To construct those specific integer types, we can combine certain specifiers together.

```c
short int 
unsigned short int 

int 
unsigned int 

long int 
unsigned long int
```

int:

```c
int num = 100;
printf("%d", num);
```

float:

```c
float floatie = 1.234;
printf("%f", floatie)
```

double:

```c
double doubledouble = 19.9999999999999;
printf("%lf", doubledouble) // lf = long float
```

If you print out a floating number and don't like it's output decimals after it, you can *set the decimal precision* with `.(precision degree number)`.

```c
float myFloatNum = 3.5;  
  
printf("%f\n", myFloatNum);   
// Outputs 3.500000
// Default will show 6 digits after the decimal point  

printf("%.1f\n", myFloatNum); // Only show 1 digit  
printf("%.4f\n", myFloatNum);   // Only show 4 digits
```

---
## Extended Types

These are basically extended keywords that we can layer on top of the original ones of int (and float):
- **short** → uses **fewer bytes** than int, so it stores **smaller numbers** and can save memory.
- **long** → uses **more bytes** than int, so it stores **larger numbers**.
- **unsigned** → removes negative numbers and uses all bits to store **larger non-negative values**.

![[Pasted image 20260128211539.png|500]]

(these only work on int, float, double)

```c
int normalInt = 1000;                       // standard int 
double normalDouble = 3.14;                 // standard double

short int small = -100;                     // smaller int
unsigned int count = 25;                    // only positive int
long int big = 1234567890;                  // larger int
long long int veryBig = 9223372036854775807; // very large int
unsigned long long int huge = 18446744073709551615U; // very large, only positive
long double precise = 3.141592653589793238L; // extended precision

printf("Normal int: %d\n", normalInt);
printf("Normal double: %lf\n", normalDouble);
printf("Small: %hd\n", small);
printf("Count: %u\n", count);
printf("Big: %ld\n", big);
printf("Very Big: %lld\n", veryBig);
printf("Huge: %llu\n", huge);
printf("Precise: %Lf\n", precise);
```

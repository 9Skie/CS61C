## Inside the Memory of a Computer

In most modern computers, main memory is divided into bytes, with each byte capable of storing eight bits of information.

Each byte has a unique address to distinguish it from the other bytes in memory, and as we recall, values of different data types are stored in different sizes of bytes.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 2.jpg|150]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=271&rect=293,508,404,673|C Programming A Modern Approach (K. N. King) (Z-Library), p.242]]

---
## Memory Addresses

Simply, for any variable (and for any programming language too), when a variable is created, it has 2 things:
- a value which it holds
- a place which it's stored

![[Pasted image 20260129175202.png|500]]

For example, this variable `a`, that is it's name:
- it has a value of 5
- it's stored at address 2686732

Normally, we can directly reference a variable's value by referring to it's name.

```c
int a = 5;  
printf("%d", a); // Outputs 5
```

We can access where it is located with the `&` reference operator, notice how printing it out requires the `%p` format specifier, as it's a 'pointer'.

```c
int a = 5;  
printf("%p", &a); // Outputs a long fat hexadecimal, like 0x7ffe5367e044
```

---
## Pointers

So, as you saw we can get the memory address of a variable, we can store it in another variable, with a special type called 'pointers'.

A pointer is a variable that stores the memory address of another variable as its value.

### Address Operator

To get the address of a variable as shown above, you need the `&` operator.

### The Indirection Operator

A pointer variable points to a data type*(like `int`) of the same type, and is created with the `*` operator.

```c
int age = 43;     // An int variable  
int *ptr_age = &age; // A pointer variable for the int datatype, stores the address of age
```

![[C Programming A Modern Approach (K. N. King) (Z-Library) 3.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=272&rect=315,119,422,154|C Programming A Modern Approach (K. N. King) (Z-Library), p.243]]

Effectively, printing both out is the same thing, `ptr_age` and `&age`

```c
// Output the value of myAge (43)  
printf("%d\n", age);  
  
// Output the memory address of myAge (0x7ffe5367e044)  
printf("%p\n", &age);  
  
// Output the memory address of myAge with the pointer (0x7ffe5367e044)  
printf("%p\n", ptr_age);
```

---

## Referencing and Dereferencing

```c
int age = 43;     // An int variable  
int *ptr_age = &age; // A pointer variable for the int datatype, stores the address of age
```

The above we call is 'referencing', basically, giving a value a pointer.

Then there comes 'de-referencing', which allows us to access the stored value at the pointer.
> “Go to the memory address the pointer is holding, and read (or write) the value there.”

In C, dereferencing is done using the * operator as well, but used on the pointer outside of declaration.

```c
int age = 43;
int *ptr_age = &age;

// Dereference the pointer to get the value
printf("%d\n", *ptr_age);  // Outputs 43

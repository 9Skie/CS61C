> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=190&selection=9,0,21,73&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.161]]
> > So far, the only variables we’ve seen are scalar: capable of holding a single data item. C also supports aggregate variables, which can store collections of values. There are two kinds of aggregates in C: arrays and structures. This chapter shows how to declare and use arrays, both one-dimensional (Section 8.1) and multidimensional (Section 8.2). Section 8.3 covers C99’s variable-length arrays.

Well, the infamous... oh we aren't working with memory yet, we'll get there later.

For this example, this array only stores 4 values, and only integer data types.

```c
int myNumbers[] = {25, 50, 75, 100};
```

To access a value inside an array, you simple use an index.

```c
int myNumbers[] = {25, 50, 75, 100};  
printf("%d", myNumbers[0]);  
  
// Outputs 25

myNumbers[0] = 33;
printf("%d", myNumbers[0]);  
  
// Now outputs 33 instead of 25
```

Now, you can also initialize an array and put no values into it at first, and add eventually.

```c
// Declare an array of four integers:  
int myNumbers[4];  
  
// Add elements  
myNumbers[0] = 25;  
myNumbers[1] = 50;  
myNumbers[2] = 75;  
myNumbers[3] = 100;
```
---
## Array Sizes

And as expected, you can use `sizeof` on an array, which just returns it's length.

```c
int myNumbers[] = {10, 25, 50, 75, 100};

printf("%zu", sizeof(myNumbers));  // Prints 20
```

Oh, not in terms of elements, but in bytes, recall that from when we did `sizeof` to the initial data types.

And that's why, if you really wanted the number of elements in the array, you can find the size of bytes the list has, and the size of bytes an element has, and do some division!

```c
int myNumbers[] = {10, 25, 50, 75, 100};
int length = sizeof(myNumbers) / sizeof(myNumbers[0]);

printf("%d", length);  // Prints 5
```

(Don't worry, this works regardless the data type)

---
## Looping Arrays

You can't just directly run a for loop on a array unlike in python! You have to explicitly state the array indexes you want to loop through, making the initial index start at 0, increase it 1 at a time, and stop it when we reach the length of the array...

(It's pretty dumb)

```c
int myNumbers[] = {25, 50, 75, 100};

int length = sizeof(myNumbers) / sizeof(myNumbers[0]);
int i;

for (i = 0; i < length; i++) {
  printf("%d\n", myNumbers[i]);
}
```

The problem with storing an array of strings, is that all strings are variable sized, but C likes fixed sized arrays, whether that be columns, rows, or any other higher dimensions.

Say if we were to try to store this array of strings in a 2D array:

```c
char planets[][8] = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", 
					"Saturn", "Uranus", "Neptune", "Pluto"};
```

Not all our strings were long enough to fill an entire row of the array, so C padded them with null characters. 

There’s a bit of wasted space in this array, since only three planets have names long enough to require eight characters.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 10.jpg|300]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=330&rect=298,515,431,667|C Programming A Modern Approach (K. N. King) (Z-Library), p.301]]

So, instead of creating a native 2D array this way, we can create a list of pointers, which point to these strings.

```c
char *planets[] = {"Mercury", "Venus", "Earth", "Mars", "Jupiter",  
					"Saturn", "Uranus", "Neptune", "Pluto"};
```

Each elements of `planets` is a pointer to a null-terminated string. There are no longer any wasted characters in the strings.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 11.jpg|300]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=330&rect=294,203,439,353|C Programming A Modern Approach (K. N. King) (Z-Library), p.301]]
> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=164&selection=40,0,45,52&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.135]]
> > Working with characters in C is simple, because of one fact: C treats characters as small integers. After all, characters are encoded in binary, and it doesn’t take much imagination to view these binary codes as integers. 

When a character appears in computation, C simply treats it as if it was an integer. 

```c
char ch; 
int i; 

i = 'a'; /* i is now 97 */
ch = 65; /* ch is now 'A' */ 
ch = ch + 1; /* ch is now 'B' */ 
ch++; /* ch is now 'C' */
```

The `char` is used to store a single character, and the character being stored must be surrounded in single quotes.

```c
char Grade = 'A';
printf("%c", Grade);
```

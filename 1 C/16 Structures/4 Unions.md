The syntax for a union is identical to a struct, however, the compiler allocates only enough space for the largest of the members, which overlay each other within this space. 

To see what this means in memory, lets create a union and a struct.

```c
union myUnion {
	int i;
	double d;
}

struct myStruct {
	int i;
	double d;
}

union myUnion u = {1, 1.3}
struct myStruct s = {1, 1.3}
```

Structures and unions differ in just one way: the members of a structure are stored at different addresses in memory, while the members of a union are stored at the same address.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 14.jpg|200]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=425&rect=269,122,450,376|C Programming A Modern Approach (K. N. King) (Z-Library), p.396]]

Members of a union are accessed in the same way as members of a structure. However, since all members share the same memory, changing one will affect the others. Only the **last assigned member** holds a valid value.

```c
union myUnion {  
  int myNum;  
  char myLetter;  
  char myString[30];  
};  
  
int main() {  
  union myUnion u1;  
  
  u1.myNum = 1000;  
  
  // Since this is the last value written to the union, myNum no longer holds 1000 - its value is now invalid  
  u1.myLetter = 'A';  
  
  printf("myNum: %d\n", u1.myNum); // This value is no longer reliable  
  printf("myLetter: %c\n", u1.myLetter); // Prints 'A'  
  
  return 0;  
}
```

--- 
## So Why Use Unions?

Unions save space compared to structs! Remember, this is a time when memory was scarece.
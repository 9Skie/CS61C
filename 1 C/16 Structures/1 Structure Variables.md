This chapter introduces three new types: structures, unions, and enumerations. 
- A structure is a collection of values (members), possibly of different types. 
- A union is similar to a structure, except that its members share the same storage.
- An enumeration is an integer type whose values are named by the programmer.

Structures (also called structs) are a way to group several related variables into one place. Each variable in the structure is known as a **member** of the structure.
> The idea is very similar to kinda like a class... but not as sophisticated

Here  are some properties about structs:
- the elements (member) of it don't have to have the same data type
- each member has it's own name

You can create a structure by using the `struct` keyword and declare each of its members inside curly braces:

```c
struct Part {               // Structure Declaration
    int number;               // Member (int)
    char name[NAME_LEN + 1];  // Member (char list)
    int on_hand;              // Member (int)
};
```

The members of a structure are stored in memory in the order in which they’re declared.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 12.jpg|150]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=407&rect=303,137,431,387|C Programming A Modern Approach (K. N. King) (Z-Library), p.378]]

It's totally fine if members of another structure collide in their naming schemes, but structs cannot have the same name.

---
## Initializing Structure Variables

To access the structure, you must create a variable of it.

Use the `struct` keyword inside the `main()` method, followed by the name of the structure and then the name of the structure variable:

```c
struct Part {
    int number;
    char name[NAME_LEN + 1];
    int on_hand;
};

int main(void)
{
    struct Part part1 = {528, "Disk drive", 10};
    struct Part part2 = {914, "Printer cable", 5};

    return 0;
}
```

The value in the initializer must appear in the same order as the members of the structure.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 13.jpg|200]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=409&rect=286,543,396,615|C Programming A Modern Approach (K. N. King) (Z-Library), p.380]]

---
## Accessing Structure Members

To access members of a structure, use the dot syntax `.`:

```c
// Create a structure called myStructure  
struct myStructure {  
  int myNum;  
  char myLetter;  
};  
  
int main() {  
  // Create a structure variable of myStructure called **s1**  
  struct myStructure s1;  
  
  // Assign values to members of s1  
  s1.myNum = 13;  
  s1.myLetter = 'B';  
  
  // Print values  
  printf("My number: %d\n", s1.myNum);  
  printf("My letter: %c\n", s1.myLetter);  
  
  return 0
}
```

You also use this syntax to modify the value of members.

```c
struct myStructure {  
  int myNum;  
  char myLetter;  
  char myString[30];  
};  
  
int main() {  
  // Create a structure variable and assign values to it  
  struct myStructure s1 = {13, 'B', "Some text"};  
  
  // Modify values  
  s1.myNum = 30;  
  s1.myLetter = 'C';  
  strcpy(s1.myString, "Something else");
  
  return 0;
```
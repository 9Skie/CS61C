An enum is just a special type that represents a group of constants, they don't have much similarity with structs and unions, except their syntax is similar.

```c
enum Level {  
  LOW = 25,  
  MEDIUM = 50,  
  HIGH = 75  
};

int main() {  
  // Create an enum variable and assign a value to it  
  enum Level myVar = MEDIUM;  
  
  // Print the enum variable  
  printf("%d", myVar);  // Prints 50
  
  return 0;  
}
```

You'll notice how it's... well, syntactically different from enum.

Say you declared this enum:

```c
enum Color {
	RED = 0xFF0000, 
	GREEN = 0x00FF00, 
	BLUE = 0x0000FF};
```

You make a variable from the enum like this:

```c
enum Color a_color = RED;
```

That’s it.
- No braces
- No multiple fields
- No enum Color.RED
- Just assign one enumerator

Also, enums CANNOT store any data type outside of integers, so that's a thing.

---
## Default Values

Behind the scenes, C treats enumeration variables and constants as integers. By default, the compiler assigns the integers 0, 1, 2, … to the constants in a particular enumeration.

In this example, by default, the first item (`LOW`) has the value `0`, the second (`MEDIUM`) has the value `1`, and onwards.

```c
enum Level {  
  LOW,  
  MEDIUM,  
  HIGH  
};

int main() {  
  // Create an enum variable and assign a value to it  
  enum Level myVar = MEDIUM;  
  
  // Print the enum variable  
  printf("%d", myVar);  // This will output 1
  
  return 0;  
}
```
While we have seen that we can output with `printf()`, to get user input, we can use the `scanf()` function.

```c
// Create an integer variable that will store the number we get from the user  
int myNum;  
  
// Ask the user to type a number  
printf("Type a number: \n");  
  
// Get and save the number the user types  
scanf("%d", &myNum);  
  
// Output the number the user typed  
printf("Your number is: %d", myNum);
```

As you can see, `scanf()` takes in two arguments, the format of the variable which we want to store the user's input in, and the addresses of variables where the parsed values should be stored.

You can also get a string entered, but again remember that strings are a series of chars, which is a list.

```c
// Create a string  
char firstName[30];  
  
// Ask the user to input some text  
printf("Enter your first name: \n");  
  
// Get and save the text  
scanf("%s", firstName);  
  
// Output the text  
printf("Hello %s", firstName);
```

But! `scanf()` does consider spaces, tabs etc as a terminating character, which means only a single word is displayable.

---
## How scanf Works

Like the printf function, scanf is controlled by the format string. When it is called, scanf begins processing the information in the string, starting at the left. 

For each conversion specification in the format string, scanf tries to locate an item of the appropriate type in the input data, skipping blank space if necessary.

If the item was read successfully, scanf continues processing the rest of the format string. 

If any item is not read successfully, scanf returns immediately without looking at the rest of the format string (or the remaining input data).

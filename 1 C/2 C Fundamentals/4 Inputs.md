Based on the box example we had from the last note:

```c
#include <stdio.h>

int main() {
  int length = 8;
  int width = 10;
  int area = length * width;
  printf("Area is: %i", area);

  return 0;
}

```

What if we wanted the user to input the dimensions of width instead of having to manually change it in the code before it compiles? We can do that with another function called `scanf`.

```c
int x;              // uninitialized variable, x
printf("Enter a value into x: ");
scanf("%d", &x);    // scanf writes an integer into x
```

And now, we'll be able to allow user input for our box program.

```c
#include <stdio.h>

int main() {
  // Write your code here
  int length;
  int width;
  int area = length * width;
  printf("Area is: %i", area);

  return 0;
}
```
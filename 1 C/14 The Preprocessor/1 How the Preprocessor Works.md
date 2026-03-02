In C, the **preprocessor** runs before the actual compilation begins. It handles things like including files and defining **macros**.

Preprocessor commands begin with a `#` symbol and are called **directives**, for example, we've already seen the `#include` directory.

```c
#include <stdio.h>
```

This instructs the preprocessor to open the file named `stdio.h` and bring it's contents into the program.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 19.jpg|200]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=345&rect=302,375,414,535|C Programming A Modern Approach (K. N. King) (Z-Library), p.316]]

You need to use angle brackets `< >` for standard libraries and double quotes `" "` for your own files.

---

Below is an example of a C file before and after the pre-processor.

```c
#include <stdio.h>

#define FREEZING_PT 32.0f
#define SCALE_FACTOR (5.0f / 9.0f)

int main(void)
{
    float fahrenheit, celsius;

    printf("Enter Fahrenheit temperature: ");
    scanf("%f", &fahrenheit);

    celsius = (fahrenheit - FREEZING_PT) * SCALE_FACTOR;

    printf("Celsius equivalent is: %.1f\n", celsius);

    return 0;
}
```

After the preprocessor:

```c

/* --- imported lines from stdio.h go here --- */

int main(void)
{
    float fahrenheit, celsius;

    printf("Enter Fahrenheit temperature: ");
    scanf("%f", &fahrenheit);

    celsius = (fahrenheit - 32.0f) * (5.0f / 9.0f);

    printf("Celsius equivalent is: %.1f\n", celsius);

    return 0;
}
```

So, what changed? Can you tell the difference?

- The preprocessor responded to the #include directive by bringing in the contents of stdio.h.
- The preprocessor also removed the #define directives and replaced FREEZING_PT and SCALE_FACTOR wherever they appeared later in the file. 
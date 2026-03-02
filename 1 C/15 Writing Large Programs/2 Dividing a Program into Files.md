This is just a big example of dividing a single large program into logically separate modules.

The example is the `justify` program. Instead of putting everything into one source file, the program is divided into three .c files and two header files:
- justify.c → contains main (overall control logic)
- word.c → handles reading words from input
- line.c → handles building and formatting lines

Each module has a corresponding header:
- word.h → declares the functions in word.c
- line.h → declares the functions in line.c

Here is a compact, structured view of what Section 15.3 is doing with the justify program. I’ll show only the relevant imports and a small portion of each file so you can see the structure clearly.

Here’s a very minimal preview of what Section 15.3 is doing — just enough to see the structure.

`justify.c`

```c
#include "line.h"
#include "word.h"

int main(void) {
    char word[22];

    clear_line();
    read_word(word, 21);
    add_word(word);
    write_line();
}
```

 `word.h`

```c
#ifndef WORD_H
#define WORD_H

void read_word(char *word, int len);

#endif
```

`word.c`

```c
#include <stdio.h>
#include "word.h"

void read_word(char *word, int len) {
    /* actual input logic here */
}
```

`line.h`

```c
#ifndef LINE_H
#define LINE_H

void clear_line(void);
void add_word(const char *word);
void write_line(void);

#endif
```

`line.c`

```c
#include <stdio.h>
#include "line.h"

void clear_line(void) { /* ... */ }
void add_word(const char *word) { /* ... */ }
void write_line(void) { /* ... */ }
```
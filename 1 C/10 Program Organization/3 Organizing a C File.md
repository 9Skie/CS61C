Now that we've seen many C programs, and many parts that make up a C program, there's a convention for organizing things inside a C program.

```
#include directives 
#define directives 

Type definitions 
Declarations of external variables 
Prototypes for functions other than main 

Definition of main 
Definitions of other functions
```

- **#include** **directives first**
    Bring in headers needed throughout the program.
    
- **#define** **directives next**
    Macros are usually used globally, so define them early.
    
- **Type definitions (****typedef****,** **struct****,** **enum****)**
    Types must be defined before anything that uses them.
    
- **External (global) variable declarations**
    Makes them visible to all following functions.
    
- **Function declarations (prototypes)**
    Prevents errors from calling functions before they’re defined. Allows function definitions to appear in any order.
    
- **main** **function**
    Put it first among function definitions so readers can quickly find the entry point.
    
- **Other function definitions**
    Order them however makes sense (alphabetical or grouped by purpose).
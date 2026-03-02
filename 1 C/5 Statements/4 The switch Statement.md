This is basically the match case in python (I even barely use that one too).

I do understand why they might want to call it "switch"? It feels like you are pulling an n-way level to channel the code into just 1 of them

```c
switch (_expression_) {  
  case x:  
    // code block
    break;  
  case y:  
    _// code block  
    break;  
  default:  
    // this is like the else statmenet, if no cases match then it runs this code
    // code block  
}
```

Basically:
- The `switch` expression is evaluated once
- The value of the expression is compared with the values of each `case`
- If there is a match, the associated block of code is executed
- The `break` statement breaks out of the switch block and stops the execution
- The `default` statement is optional, and specifies some code to run if there is no case match

Why would anyone use a switch...?

```c
int day = 4;
  
switch (day) {  
  case 1:  
    printf("Monday");  
    break;  
  case 2:  
    printf("Tuesday");  
    break;  
  case 3:  
    printf("Wednesday");  
    break;  
  case 4:  
    printf("Thursday");  
    break;  
  case 5:  
    printf("Friday");  
    break;  
  case 6:  
    printf("Saturday");  
    break;  
  case 7:  
    printf("Sunday");  
    break;  
}  
  
// Outputs "Thursday" (day 4)
```
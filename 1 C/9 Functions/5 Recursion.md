As we know, functions can call themselves, this is recursion.

Below is an example of a summation.

```c
int sum(int k);

int main() {
  int result = sum(10);
  printf("%d", result);
  return 0;
}

int sum(int k) {
  if (k > 0) {
    return k + sum(k - 1);
  } 
  else {
    return 0;
  }
}
```

> [!PDF|yellow] [[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=233&selection=78,0,80,28&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.204]]
> > Some programming languages rely heavily on recursion, while others don’t even allow it. C falls somewhere in the middle: it allows recursion, but most C programmers don’t use it that often



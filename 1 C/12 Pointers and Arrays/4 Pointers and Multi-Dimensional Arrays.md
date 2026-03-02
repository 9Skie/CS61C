If we recall how multi-dimensional arrays rare stored in memory, they are all compressed down into an 1-D array, a 2D array with r rows, and c columns would look like this in memory.

![[C Programming A Modern Approach (K. N. King) (Z-Library) 8.jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=296&rect=262,294,465,346|C Programming A Modern Approach (K. N. King) (Z-Library), p.267]]

As it's all just a 1-D array in memory, we can use a for loop to increment the pointer to`a[0][0]` row * col times.

```c
int row = 7, col = 8, sum = 0;
int a[row][col];
int *a_pointer = &a[0][0];

int main(){
	for (i = 0, i < row; i++){
		for (j = 0, j < row; j++){
			sum += *a_pointer
			p++
		}
	}
}
```

---
## Name of N-D Array as Pointer

This is the most confusing par

| **Expression** | **Moves by** |
| -------------- | ------------ |
| a + 1          | one row      |
| a[i] + 1       | one column   |
| a[i][j] + 1    | one element  |

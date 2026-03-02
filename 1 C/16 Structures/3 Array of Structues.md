Structures and arrays can be combined without restriction. Arrays may have structures as their elements, and structures may contain arrays and structures as members.

So... in a way, we are able to make C lists store more than 1 data type, with lists holding structs, and structs holding different things.

First define the struct type:

```c
struct Part {
    int number;
    char name[NAME_LEN + 1];
    int on_hand;
};
```

Then make an array of them:

```c
struct Part inventory[100];
```

That’s it, you now have 100 struct Part values in a row.

You can access elements like any array, just remember each element is a struct, and you know how to access members of structs:

```c
inventory[0].number = 528;
inventory[0].on_hand = 10;
```

 An array of structs is just an array — each element happens to be a struct, it's nothing crazy.
For our example:

```text
Cache lines:  4
Block size:   16 bytes
Address size: 32 bits
```

We directly try to read `0x00000014`.

![[Screenshot 2026-08-06 at 6.06.35 PM.jpg|500]]

That is index 1, so we access it, realize it doesn't have valid data stored in there (due to valid bit)

![[Screenshot 2026-08-06 at 6.07.12 PM.jpg|500]]

Then we load the data into the cache, and set the tag and valid bit

![[Screenshot 2026-08-06 at 6.08.02 PM.jpg|500]]

Then we read from cache at the offset, the offset is 4, which is index 4-7, so we return word `b`.

![[Screenshot 2026-08-06 at 6.08.50 PM.jpg|500]]

Next, say we are reading from `0x0000001C`.

We go check the index at 1, the valid bit has been toggled to 1, so we confirm there is a value sitting here in cache.

![[Screenshot 2026-08-06 at 6.12.14 PM.jpg|500]]

And then we check the cache tag, which is valid

![[Screenshot 2026-08-06 at 6.16.02 PM.jpg|500]]

Lastly, since all of this is valid, we check the offset, which is 12, so we go get the value of `d`.

![[Screenshot 2026-08-06 at 6.16.57 PM.jpg|500]]


In actuallity, this is achieved in hardware simultiouasly, rather than sequentially in a software perpesecitve

![[Screenshot 2026-08-07 at 10.06.19 AM.jpg]]

As we can see, the **index** bits are used to select the specific cache line we want to inspect. The **tag** from the requested address is then compared with the tag stored in that cache line. If the tags match and the line is valid, the cache produces a `1` for a hit.

At the same time, the **block offset** is used as the select input to a multiplexer, which chooses the specific byte or word we want from the data stored in that cache block.
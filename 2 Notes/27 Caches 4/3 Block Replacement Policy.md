A **block replacement policy** determines which cache block should be removed when a new block needs to be loaded into a full cache. This is needed in fully associative and set-associative caches, because a new block can have multiple possible locations, and the cache must choose which existing block to replace.

Common replacement policies include:

- **LRU (Least Recently Used):** Replace the block that has not been accessed for the longest time, based on the idea that recently used data is more likely to be used again.
- **FIFO (First In First Out):** Replace the block that has been in the cache the longest.
- **Random:** Randomly choose a block to replace, which is simple and can work reasonably well in practice.


Let's look at an example of LRU with the following assumptions:
- 2 way set associate cache
- 1 byte blocks

Say we are trying to access address 0,2,0,1,4,0

![[Screenshot 2026-08-09 at 10.34.08 AM.jpg|500]]

As we can see from the image, access memory address 0, it's a miss, we bring into set 0 location 0.

Then we access memory address 2, it's a miss, we bring into set 0 location 1.

Then we access memory address 0, it's a hit, so set 0 location 1 becomes least recently used (LRU).

Then we access memory address 1, it's a miss, we bring it into set 1 location 0.
- Notice how this doesn't change the LRU of set 0

Then we access memory address 4, it's a miss, we bring it into set 0, based on the LRU policy, the current LRU index is 2, so we replace address 2 at set 0 location 1.
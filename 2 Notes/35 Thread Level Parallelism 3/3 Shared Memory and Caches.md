If we recall the general memory of a computer model looks like this:
- We have the main memory, an L3 cache which is global to all processors
- For each processor we have respective L2 and L1 caches

![[Screenshot 2026-08-19 at 10.27.59 AM.jpg|500]]

How do they share data back and fourth? How do they coordinate? How many processors can be supported? These are questions we'll look at in this note.

When we look at this model, however, we find an important problem: because each processor has its own private caches, the same memory location can exist as multiple cached copies at the same time.

For example, suppose Processor 1 and Processor 2 both read `memory[1000]` (it's the value of 20). If neither cache contains it, both processors fetch the value from memory and store their own local copy in cache. So now the same memory location has been duplicated across multiple caches.

![[Screenshot 2026-08-19 at 10.57.12 AM.jpg|500]]

The duplication itself is fine for reads. The real problem appears when one processor updates its cached copy. Processor 0 might now write `memory[1000] = 40`, now both processor 1 and 2 still have the  old cached value `20`. The different cached copies are no longer synchronized, or **coherent**.

![[Screenshot 2026-08-19 at 10.58.34 AM.jpg|500]]

The mechanism used to keep these duplicated cache copies consistent is called **cache coherence**, which we'll look at in the next note.
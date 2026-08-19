The difficulty with pipelining is that several instructions are in progress at the same time.

When the processor encounters a branch, it may not yet know whether the branch will be taken. Meanwhile, it continues fetching and partially executing the following instructions.

![[Screenshot 2026-08-04 at 9.38.57 PM.jpg|500]]

If the branch is taken, those instructions belong to the wrong execution path and must not be allowed to complete.


One simple solution is to stop fetching new instructions for two cycles after encountering a branch. This gives the processor enough time to determine whether the branch is taken and where execution should continue.

However, this is wasteful. Even when the branch is not taken, the processor still loses two cycles.


Instead, the processor can continue fetching the next two sequential instructions under the assumption that the branch will not be taken.
- If the branch is not taken, those instructions are already correct and execution continues normally.
- If the branch is taken,  all incorrectly fetched instructions are discarded (this is called flushing), and instruction fetching resumes from the correct branch target.

 Branch prediction can reduce this cost by guessing the branch outcome before it is fully resolved.
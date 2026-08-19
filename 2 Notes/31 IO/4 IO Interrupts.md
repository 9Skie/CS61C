Polling works well when an event happens frequently and on a predictable schedule. If something needs to be checked at regular intervals anyway, periodically checking its state can be simple and efficient. If the screen refreshes exactly $x$ times per second, and the CPU already knows that it needs to interact with the screen every $1/x$ seconds, periodically checking or updating it is reasonable.

Interrupts work better when events are relatively infrequent and unpredictable. A keyboard is the classic example: the computer has no idea when a human will press a key, and human typing is extremely slow compared with CPU speed. Constantly polling the keyboard would therefore waste work. Instead, the CPU can continue executing other instructions, and when a key event occurs, the keyboard controller generates an interrupt so the CPU knows there is something to handle.

In real systems, there is often a hybrid approach, like in High-speed network interfaces. 

At low traffic rates, interrupts are efficient: a packet arrives, so the NIC interrupts the CPU. But at extremely high packet rates, generating an interrupt for every packet becomes expensive. The OS may temporarily switch to polling the NIC and process many packets together. Linux's NAPI networking mechanism works roughly along these lines.

![[ChatGPT Image Aug 11, 2026, 10_15_52 AM.png|500]]



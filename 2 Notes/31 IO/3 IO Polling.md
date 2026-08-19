Polling is a simple way for the processor to deal with the fact that I/O devices and the CPU operate at very different speeds. The CPU is usually much faster, so instead of trying to perfectly synchronize the two, the device exposes a small status bit or status register that tells the CPU whether it is ready.

For an input device, the device might receive some data, place that data into a device register, and then set a `ready` bit to `1`. The CPU keeps checking that bit. Once it sees `ready = 1`, it knows there is data available and reads it. Afterward, the bit can be cleared again until more data arrives.

```text
while ready == 0:
    check again

read data from device
```

For an output device, the same idea works in reverse. The CPU checks whether the device is ready to accept new data. If the device is still busy, the CPU keeps polling. Once the device reports that it is ready, the CPU writes the next piece of data to it.

```
while ready == 0:
    check again

write byte to device
```

The device maintains status bits describing whether data is available or whether it is ready to accept data, and the CPU periodically polls those bits before performing the actual I/O.


You might go: 'wait, isn't this a bit wasteful? Most of those polling operations won't return the ready status.' And you'd be right, this does create extra overhead, but we don't really have a better solution do we?

If we make the simplifying assumption that each poll costs exactly one CPU cycle, then the overhead is extremely small.

A 1 GHz processor has $10^9$ cycles per second. If we poll the screen 60 times per second, then only 60 cycles are spent polling:

$\text{Polling overhead}=\frac{60}{10^9}\times100\% =0.000006\%$

So under that assumption, essentially none of the processor's time is being spent polling.

The real problem with polling appears when you poll very frequently. This is one of the main motivations for interrupts: rather than having the CPU constantly ask, “Are you ready yet?”, the device tells the CPU when something actually happens.
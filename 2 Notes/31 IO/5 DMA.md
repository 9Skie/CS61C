DMA, or Direct Memory Access, is a hardware mechanism that lets an I/O device transfer data directly to or from RAM without making the CPU copy every byte. The DMA mainly exists to reduce CPU overhead for large or frequent I/O transfers.

![[Screenshot 2026-08-11 at 10.37.55 AM.jpg|500]]

For incoming data, the four steps are:

1. The device first has some data ready, so it interrupts the CPU
2. The CPU handles that interrupt and sets up the DMA transfer.
3. The DMA engine then performs the actual transfer directly between the device and memory, the CPU can do other work.
4. When the DMA transfer is finished, the device or DMA engine interrupts the CPU again.

For outgoing data, the flow is almost the same, except the CPU initiates it. The CPU first decides it wants to send data and confirms that the device is ready.

The overall pattern is:

```text
set up transfer
      ↓
DMA moves the data
      ↓
CPU does other work
      ↓
interrupt when finished
```

The main difference is that incoming DMA often starts because the device says “I have data,” while outgoing DMA starts because the CPU says “I want to send data.”
Uh... this feels like for another class, so this won't be a big note. 

OS is for the purpose of running many applications at once, and it makes the communication between applications and hardware easier.

There was a website trying to compare how many lines of code do different applications have, and the question is 'Is a million lines of code a lot'? How many lines are there in Windows? Facebook? iPhone apps?

This image shows it all.

![[Pasted image 20260809123139.png|700]]

We can see that operating systems... are a lot of code! Windows 2000 is 29 million lines of code, Mao OS X Tiger is 86 million lines of code, and this was statistics gathered way back in 2015.

As the needs of applications (and hardware) grew and grew, operating systems became more and more complicated, this is an image showing how lines of code in the linux kernel grew over the years.

![[Screenshot 2026-08-09 at 12.34.35 PM.jpg|500]]

It gets complicated!

The OS is the first software that runs when the computer stats, it finds and controls all IO devices in the machine in a general way, relying on device drivers, and provides services like the file system, networking, keyboard and mouse, the loading & running of programs, etc.


When a computer is powered on, the CPU starts in a predefined state and begins executing instructions from a fixed address stored in **firmware** (such as Flash ROM).  Its job is to initialize the basic hardware and find a storage device containing the operating system. It then loads the first piece of the operating system startup code, called the **bootloader**, from the disk into memory and transfers control to it.

The **bootloader** is responsible for loading the operating system kernel from storage into main memory. Once the kernel is loaded, the bootloader jumps to the kernel's entry point, and the operating system begins executing.

The operating system kernel then initializes the rest of the computer. Finally, the OS starts user-level programs such as a terminal, desktop environment, or login screen, allowing the user to interact with the computer.

 ![[Screenshot 2026-08-09 at 12.38.45 PM.jpg|500]]
We know there are layers of abstraction in a CPU, as we just finished learning about the high level language of C, we are now moving onto assembly language, RISC V.

What is RISC V? Well, I feel like we need to formally introduce a little background first for assembly language, and RISC V.

---
## What is an Instruction Set

A CPU has a dedicated set of instructions that it can carry out, this we call the instruction set.
- Arithmetic operations
- Logical operations
- Branching 
- Registor load/storage

Well, what's it's purpose? It's the standardized way of communication between the software, and the hardware.

![[Screenshot 2026-02-11 at 4.34.07 PM.png|500]]

Here's an illustrative example: imagine an ensemble, the conductor waves his wand, and the musicians play their instruments, but how do they coordinate with each other? Through the music sheet.

- ![[芯片有自己的革命史！指令集架构的突围与重生【RISC-V进化史｜革故鼎新】PT2M24.42S.jpeg|芯片有自己的革命史！指令集架构的突围与重生【RISC-V进化史｜革故鼎新】 - 02:24|150]] [02:24](https://www.bilibili.com/video/BV1449GYHETw/?t=144.420307#t=02:24.42) 

The conductor, through the music sheet can tell the ensemble to play at what tempo, what tone etc, and the musicians through the music sheet can know what notes to play, when to play.

In such a sense, the conductor is like the software, and the musicians are like the hardware, and what lets them communicate uniformly is through the music sheet, the instruction set.

Here's an image illustrating the logical progression from a program to actual electricity running through a computer, and the ISA (instruction set architecture) sits right in the middle of it.

- ![[芯片有自己的革命史！指令集架构的突围与重生【RISC-V进化史｜革故鼎新】PT2M43.435S.jpeg|芯片有自己的革命史！指令集架构的突围与重生【RISC-V进化史｜革故鼎新】 - 02:43|500]] 

---
## Complicated Instruction Sets

On the hardware side, the ISA must be realistic to implement efficiently in circuits and future microarchitectures; on the software side, it must give compilers, operating systems, and applications enough structure and features to generate fast, clean code.

In the early days of personal computing, instruction sets and the chips that implemented them were already quite complex. 

For example, the 1979 Motorola 68000 contained around 68,000 transistors, and roughly 1/3 of the transistors were devoted to microcode control logic used to implement its complex instruction set.

This CISC (complex instruction set computer) is still common on the market today, why? While there were many competing instruction sets and processor designs at the time, when IBM chose the Intel 8088 for the original IBM PC in 1981, it anchored the market to Intel’s architecture. 

As the IBM PC became the business standard, software developers targeted that platform, and compatibility became economically critical. This network effect pushed the x86 instruction set (by intel) into dominance.

----
## Reduced Instruction Sets

At this time, UCB assistant professor David Patterson was helping out with a company to help debug and improve microcode in personal computers. 

In this process, he found something shocking: roughly 20% of the instructions handled most of the work, while the remaining 80% added complexity but was used rarely, and the instructions were all very slow.

So in 1980, him and his student David Ditzel created the idea of RISC (reduced instruction set computer)

The idea was simple, cut down the complex instructions and remain only the simple ones, and break down any complex instructions as combinations of simple instructions.

- ![[芯片有自己的革命史！指令集架构的突围与重生【RISC-V进化史｜革故鼎新】PT5M28.072S.jpeg|芯片有自己的革命史！指令集架构的突围与重生【RISC-V进化史｜革故鼎新】 - 05:28|150]] [05:28](https://www.bilibili.com/video/BV1449GYHETw/?t=328.071757#t=05:28.07) 

And this is when the design ideology of RISC and CISC is formally introduced.

---
## RISC Chips

David Patterson took this even further, under governmental funding, he built a team and created the first ever RISC microprocessor in 1982. RISC 1, which had about 44000 transistors.

Snd then in 1983, they made RISC 2, 1985 they made RISC 3, 1987 RISC 4... there's a lot of detail I'm glossing over here for what improvements they made on each iteration of the chip, so please, if you are interested, go look at the details yourself.

Afterwards in 2010 in UCB's parallel computing lab, another group of people picked this project back up (Krste Asanovia, Yunsup Lee, Andrew Waterman) developed RISC 5 (RISC-V)

---
## The Future of RISC?

As an open source, modern instruct set, RISC-V quickly gained community and grew an ecosystem.

But it was still no where close to breaking into mainstream computing devices:
- Laptops / Desktops → mostly x86 (Intel / AMD) and ARM (Apple Silicon)
- Phones → almost entirely ARM (Qualcomm, MediaTek, Apple)
- Servers→ mostly x86, with growing ARM (Amazon Graviton)

Still, there are companies that are trying to build on top of RISC-V and make chips using this instruction set.

Like Alibaba, in 2018, they developed XuanTie E902, and in 2019 XuanTIe C910, a high-performance, RISC-V core designed to run modern day operating systems.

When it was announced, Alibaba claimed it was one of the fastest RISC-V cores available at the time. And they kept going, later announcing Wujian 100 in the same year,  an open source RISC-V–based development platform for building custom system-on-chip (SoC) designs.

With the tide of AI, RISC-V received a new wave of attention as well, while training LLMs are still done on GPUs, inferencing using LLMs saw potential for RISC-V processors for their customizability to specifically suit AI inference needs.

However, in mainstream AI, especially large-scale inference in data centers, the ecosystem is still dominated by established platforms like GPUs from Nvidia and specialized ASICs (e.g., TPUs from Google). These platforms have mature software stacks, optimized libraries, and massive industry adoption. RISC-V lacks that deep tooling maturity and deployment scale right now.
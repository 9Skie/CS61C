Conductors are materials through which electricity can easily pass. Insulators are materials through which electricity can barely pass. Semiconductors are materials whose ability to conduct electricity can be controlled.

![[Pasted image 20260305204147.png|500]]

## Transisters

We don't use primary old transistors, the modern transistors follow the convention of MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor)

A transistor is a 3 lead device: source, drain, gate

The simple idea is that the source wants to go to the drain, but the gate controls whether that happens or not, the circuit becomes closed only when voltage of the gate is higher than the voltage of the source.
- this we call an n-channel MOSFET

![[Screenshot 2026-03-05 at 8.54.56 PM.png|400]]

On the inverse, we have a p-channel MOSFET, which is if the gate voltage is higher than the source voltage (above a certain threshold), the transistor **turns on** and current can flow from source to drain.

![[Screenshot 2026-03-05 at 9.01.18 PM.png|400]]

Like from such, we can make our not gate.

![[Screenshot 2026-03-05 at 9.16.17 PM.png|400]]

But as we've read, from a computer scientist's perspective, you REALLY don't need to understand the physical circuit (even though it's really cool), and from this point on, we'll use block diagrams to abstractly describe these circuits.

![[Screenshot 2026-03-05 at 9.21.39 PM.png|400]]
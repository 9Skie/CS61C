This is a video on youtube which I think has explained the details of floating numbers very well.

https://www.youtube.com/watch?v=dQhj5RGtag0

Floating point is why we get stuff like this on a computer:

[00:19](https://www.youtube.com/watch?v=dQhj5RGtag0&t=19#t=19.34) 

![[how floating point worksPT19.341S.jpeg|how floating point works - 00:19|500]] 

---
## Starting From Bits

We know numbers are represented with bits on a computer, and 8 bits make a byte.

- ![[how floating point worksPT1M4.516S.jpeg|how floating point works - 01:04|150]] [01:04](https://www.youtube.com/watch?v=dQhj5RGtag0&t=65#t=01:04.52) 

Every position in a binary number is associated with a power of 2, and you just add them up, but this format has no way to store negative numbers.

But there is a pretty limited representation of numbers in 8 bits, if we change that into 32 bits, we can represent up to 4294967295.

But there are still numbers larger than that! Like the global population, which is like 8 billion.

This gives way to a new question, can we represent super huge numbers (but less precisely), and super small numbers (but super accurately)?

And that's what inspired floating bit.

---
## Floating Bits

Say, instead of having 32 bits going from $2^1, 2^2, 2^3...$ what if we put a decimal right in the middle? And allow negative powers of 2?

[02:46](https://www.youtube.com/watch?v=dQhj5RGtag0&t=167#t=02:46.84) 

![[how floating point worksPT2M46.842S.jpeg|how floating point works - 02:46|500]] 

With this method, we would only be able to represent numbers up to 65535.9999985.

This is called 'fixed point format', as we explicitly expects users of this notation to know where that point resides, as to which portion of bits describe integers and which part describe decimals.

But, what if there's some way to tell the computer 'where' to put that point arbitrarily? What happens when we want to put that dot somewhere else 'floating'?

As our number has 32 bits, this would require 5 bits to describe all 32 possible positions where the dot can be placed.

So we'll have 5 bits that represent the index of the point, and the rest 27 bits representing the values.
- the 5 bits are called: point index
- the 27 bits are called: mantissa

- ![[how floating point worksPT4M23.945S.jpeg|how floating point works - 04:23|150]] [04:23](https://www.youtube.com/watch?v=dQhj5RGtag0&t=264#t=04:23) 

But we can make 32 combinations with 5 bits, and after taking out these 5 bits from our number, we have only 26 possible dot indexes, and there's 6 additional not used values for indexing.

So we can place the binary bit outside of the mantissa with 'imaginary' digits to the left/right of the floating bit number, which allows us to represent a wider range of numbers.

- ![[how floating point worksPT4M39.386S.jpeg|how floating point works - 04:39|150]] [04:39](https://www.youtube.com/watch?v=dQhj5RGtag0&t=279#t=04:39.00) 

In fact, we can extend the range of values we want to represent further by making the entire first byte be for the point index, so then we have 255 places where we can place that point.

 ![[how floating point worksPT4M57.552S.jpeg|how floating point works - 04:57|500]]

And we make 1 bit at the very front to indicate whether this number is positive or negative.

![[how floating point worksPT5M40.128S.jpeg|how floating point works - 05:40|500]]

This, makes our very first and simple model of floating bit numbers, but it still has lot's of problems, which we'll get to how to solve.

---
## The Problems With Redundancy

- ![[how floating point worksPT5M51.601S.jpeg|how floating point works - 05:51|150]] [05:51](https://www.youtube.com/watch?v=dQhj5RGtag0&t=352#t=05:51) 

With the ability to place the floating point anywhere, we can say, for example this to be the representation of 1.5.

 ![[how floating point worksPT6M0.155S.jpeg|how floating point works - 06:00|500]] 

This would also just as well represent 1.5.

 ![[how floating point worksPT6M4.278S.jpeg|how floating point works - 06:04|500]] 

As long as we can write 1 on both sides of the mantissa, we would get duplicate representation of 1.5, and this is wasting possible representations of numbers.

0 Is the most extreme case of this, as regardless of the point index, as long as the mantissa is 0, the entire value is 0.

 ![[how floating point worksPT6M15.69S.jpeg|how floating point works - 06:15|500]] 

![[how floating point worksPT6M17.51S.jpeg|how floating point works - 06:17|500]] 

That's not good! Again, we don't like redundancy, and is happy when these representations are 1 to 1, and don't waste possible representation space.

What can we do? We again, need to look at scientific notation.

---
## How Scientific Notation Solves the Problem

In scientific notation, the position of the decimal index is ALWAYS placed after the first non-zero digit in the coefficient, and then the exponent on the base (10) is adjusted accordingly.

![[how floating point worksPT8M55.587S.jpeg|how floating point works - 08:55|500]]

This idea could be directly used over in the floating number system, and we can fix that decimal place right after the first non-zero bit in the mantissa, which must be 1.

![[how floating point worksPT7M22.365S.jpeg|how floating point works - 07:22|500]]

This way, we have a 'default' position for where the decimal point is, and originally the bits that used to represent the decimal point's index now resemble how much we want to 'shift' that fixed decimal point (by $2^{exponent}$ multiplication).

However, we can't just 'default' assume all floating point numbers must start with $1.xxx...$ why? Because then we wouldn't be able to represent 0, we'll show how to solve this problem below with the exponents.

---
## Negative Exponents

The exponent also faces it's own ambiguity, which right now, being an unsigned 8 bits, can only describe exponent values from 0-255.

 ![[how floating point worksPT7M58.024S.jpeg|how floating point works - 07:58|500]] 

At this point, you might be temped to use 2's complement to allow representations of negative exponent powers, but no, the exponent really doesn't use that, instead, it is stored in bias form.

The idea is we store the exponent as a unsigned integer from 0-255, and then subtract a bias of 128 from the stored value, which makes the range [-128, 127]
- **SUPER IMPORTANT NOTE**: IEEE uses 127 as the bias, the range is [-127, 128]

![[how floating point worksPT8M19.842S.jpeg|how floating point works - 08:19|500]]

And to solve the 'storing 0' problem which we've described above, we can reserve the $2^{-128}$ as a special case to represent 0.

![[how floating point worksPT10M11.84S.jpeg|how floating point works - 10:11|500]]

It's a good idea, but it leaves then no purpose left for the mantissa bits when we have the exponent bits to be 0.

- ![[how floating point worksPT10M15.823S.jpeg|how floating point works - 10:15|150]] [10:15](https://www.youtube.com/watch?v=dQhj5RGtag0&t=616#t=10:15.82) 

So, let's try to put those values to use shall we?

---
## Subnormals

The idea of subnormals came from the inability of our system to represent numbers to any smaller degree than $2^{-128}$, if there's any number smaller than that resulting from calculations, our system's best shot is calling it 0.

- ![[how floating point worksPT10M38.2S.jpeg|how floating point works - 10:38|150]] [10:38](https://www.youtube.com/watch?v=dQhj5RGtag0&t=638#t=10:38.20) 

 ![[how floating point worksPT10M43.537S.jpeg|how floating point works - 10:43|500]]

So, we can use those extra representations of 0 for this purpose! With the original representation of $2^{-128}$, we can do this:
- view it as $2^{-127}$
- make the leading bit of the mantissa (which is implicitly assumed to be 1 in all other cases) to be 0

- ![[how floating point worksPT11M20.169S.jpeg|how floating point works - 11:20|150]] [11:19](https://www.youtube.com/watch?v=dQhj5RGtag0&t=680#t=11:19.70) 

This allows us to represent numbers smaller than the smallest exponent power of $2^{-127}$, but their precision decreases the closer they get to 0.

Now, we got subnormals, are there 'abnormals'? Numbers that are so huge that they are also impossible to describe with our current floating point system?

---
## Infinity & NAN

The answer to that question is, no, we don't have anyway to go above to 'abnormal' large numbers.

This is the largest possible number which we can represent under our current system.

 ![[how floating point worksPT13M39.376S.jpeg|how floating point works - 13:39|500]] 

And any higher than that we'll call it infinity, whenever we hit $2^{128}$.

![[how floating point worksPT14M26.555S.jpeg|how floating point works - 14:26|500]]

So whenever the exponent is 128, and the mantissa is all 0's except the implicitly assumed leading bit, we call this infinity for a 32 bit computer.

 ![[how floating point worksPT14M46.315S.jpeg|how floating point works - 14:46|500]] 

And if we try to go any higher than this, we would call it NAN (not a number).

 ![[how floating point worksPT14M48.393S.jpeg|how floating point works - 14:48|500]] 

As such, when we have $1/0$, our answer would be infinity.

 ![[how floating point worksPT15M22.679S.jpeg|how floating point works - 15:22|500]] 

And when we have $0/0$, we have NAN (not a number), or any operation with numbers too large/small possible on the system.

 ![[how floating point worksPT15M46.298S.jpeg|how floating point works - 15:46|500]] 

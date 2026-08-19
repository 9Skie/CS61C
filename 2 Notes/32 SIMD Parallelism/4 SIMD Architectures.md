The first ever SIMD machine was implemented by MIT Lincoln Labs in 1957, and the idea was further commercialized by intel in the late 1990s.

Why? Since people started looking at media, and media is saved in a vector-ish data format, and operations often involved changing many things at once, like pixels on a screen.

![[Pasted image 20260814221505.png|500]]

Over the years, SIMD became more and more sophisticated as well, evolving it's extensions all the way from MMX to AVX.

|Extension|Main idea|
|---|---|
|**MMX**|Early SIMD; 64-bit packed integer operations|
|**SSE**|Introduced 128-bit `XMM` registers; especially SIMD floating-point|
|**SSE2**|Expanded 128-bit SIMD to more integer operations and double-precision floats|
|**SSE3**|Added some additional SIMD operations|
|**SSSE3**|More specialized integer SIMD instructions|
|**SSE4.1 / SSE4.2**|More vector operations, comparisons, string-related instructions, etc.|
|**AVX**|Extended SIMD registers to 256 bits (`YMM`)|
|**AVX2**|Extended many integer SIMD operations to the full 256 bits|
|**AVX-512**|Introduced 512-bit `ZMM` registers and more advanced SIMD features|
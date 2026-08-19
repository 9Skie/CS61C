We want to look at the registers & instructions related to SIMD processing, in the simple case of array processing, it means we can process multiple indexes of an array simultaneously.

Consider this simple program that adds the x, y, z, w coordinates of a vector:

![[Screenshot 2026-08-14 at 10.33.21 PM.jpg|500]]

```
vec_res.x = v1.x + v2.x;
vec_res.y = v1.y + v2.y;
vec_res.z = v1.z + v2.z;
vec_res.w = v1.w + v2.w;
```

With SSE, an **XMM register is 128 bits wide**, so it can hold four 32-bit single-precision floats at once. The computation can therefore be done with a simple **move → add → move** sequence:

```
movaps address-of-v1, %xmm0
addps  address-of-v2, %xmm0
movaps %xmm0, address-of-vec_res
```

First, `movaps` moves the four values of `v1` from memory into `%xmm0`:

```
%xmm0 = [v1.x, v1.y, v1.z, v1.w]
```

Then, `addps` performs a **packed single-precision addition**. It takes the four values of `v2` and adds all four pairs simultaneously:

```
%xmm0 =
[v1.x + v2.x,
 v1.y + v2.y,
 v1.z + v2.z,
 v1.w + v2.w]
```

Finally, the second `movaps` moves these four results from `%xmm0` back into memory as `vec_res`.

So instead of executing four separate scalar additions, **one `addps` instruction performs all four additions in parallel**.
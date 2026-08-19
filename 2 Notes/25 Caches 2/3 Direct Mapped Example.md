For our example:

```text
Cache lines:  4
Block size:   16 bytes
Address size: 32 bits
```

Because the cache has four lines, two index bits are required:

```text
4 cache lines → 2² = 2 index bits 
```

Because each block contains 16 bytes, four offset bits are required:

```text
16 bytes per block → 2⁴ = 4 offset bits
```

The remaining bits form the tag:

```text
32 total bits - 2 index bits - 4 offset bits = 26 tag bits
```

Therefore, every 32-bit memory address is divided as follows:

```text
+--------------------+----------+-------------+
| 26-bit             | 2-bit    | 4-bit       |
| Tag                | Index    | Offset      |
+--------------------+----------+-------------+
```


Say we are trying to access an address, 105 in main memory using a 32-bit address:

```text
Address 105 = 00000000 00000000 00000000 01101001₂
```

The address is divided into a 26-bit tag, a 2-bit index, and a 4-bit offset from right to left.

```text
+----------------------------+----------+-------------+
| 26-bit                     | 2-bit    | 4-bit       |
| Tag                        | Index    | Offset      |
+----------------------------+----------+-------------+
| 00000000000000000000000001 | 10       | 1001        |
+----------------------------+----------+-------------+
```

The values of the three fields are:

```text
Tag    = 00000000000000000000000001₂ = 1
Index  = 10₂                         = 2
Offset = 1001₂                       = 9
```

The index is `10₂`, so the CPU checks cache line `2`:

```text
Index 10₂ → cache line 2
```

The tag tells the cache which of the many memory blocks that map to line `2` is being requested.

The complete memory block number is formed from the tag and index:

```text
+----------------------------+----------+
| Tag                        | Index    |
+----------------------------+----------+
| 00000000000000000000000001 | 10       |
+----------------------------+----------+


Combined memory block number:

+--------------------------------+
| 0000000000000000000000000110₂  |
+--------------------------------+
| 6                              |
+--------------------------------+
```

Therefore, address `105` belongs to memory block `6`, which contains addresses `96–111`.

Suppose cache line `2` currently contains:

```
          +-------+----------------------------+----------------+
Line 2 →  | Valid | Tag                        | Data           |
          +-------+----------------------------+----------------+
          |   1   | 00000000000000000000000001 | bytes 96–111   |
          +-------+----------------------------+----------------+
```

The requested address has:

```
Requested tag = 00000000000000000000000001
Stored tag    = 00000000000000000000000001
```

Because the valid bit is `1` and the tags match, this is a **cache hit**.

Finally, the offset is `1001₂`, which equals `9`. This selects byte offset `9` inside the cached block:

```text
Cached memory block 6:

Address:  [96][97][98][99][100][101][102][103][104][105][106] ... [111]
Offset:    0   1   2   3    4    5    6    7    8    9   10  ...   15
                                                     ↑
                                                offset 1001₂
```


So in conclusion:

```text
Address 105
    ↓
Tag 1       → confirms the correct memory block
Index 2     → selects cache line 2
Offset 9    → selects address 105 within the block
```

---


For our example, assume that each memory address refers to one **8-bit word**, which is exactly **1 byte**. So when we say that a block contains 16 bytes, that means it contains 16 addressable 8-bit words.

```text
Cache lines:  4
Block size:   16 bytes
Word size:    8 bits
Address size: 32 bits
```

Because the cache has four lines, two index bits are required:

```text
4 cache lines → 2² = 4 possibilities → 2 index bits
```

Because each block contains 16 bytes, and each address selects one byte, four offset bits are required:

```text
16 bytes per block → 2⁴ = 16 possible byte positions → 4 offset bits
```

The remaining bits form the tag:

```text
32 total bits - 2 index bits - 4 offset bits = 26 tag bits
```

Therefore, every 32-bit memory address is divided as follows:

```text
+--------------------+----------+-------------+
| 26-bit             | 2-bit    | 4-bit       |
| Tag                | Index    | Offset      |
+--------------------+----------+-------------+
```

Now suppose we want to access address `105` in main memory.

Because each address refers to one byte, address `105` means we want the **8-bit value stored at byte address 105**.

```text
Address 105 = 00000000 00000000 00000000 01101001₂
```

We divide the 32-bit address from right to left into tag, index, and offset:

```text
+----------------------------+----------+-------------+
| 26-bit                     | 2-bit    | 4-bit       |
| Tag                        | Index    | Offset      |
+----------------------------+----------+-------------+
| 00000000000000000000000001 | 10       | 1001        |
+----------------------------+----------+-------------+
```

So:

```text
Tag    = 00000000000000000000000001₂ = 1
Index  = 10₂                         = 2
Offset = 1001₂                       = 9
```

The index is `10₂`, so the CPU checks cache line `2`:

```text
Index 10₂ → cache line 2
```

The tag tells the cache which memory block should currently be stored in that line. The complete memory block number is formed from the tag and index:

```text
+----------------------------+----------+
| Tag                        | Index    |
+----------------------------+----------+
| 00000000000000000000000001 | 10       |
+----------------------------+----------+

Combined memory block number:

+--------------------------------+
| 0000000000000000000000000110₂  |
+--------------------------------+
| 6                              |
+--------------------------------+
```

So address `105` belongs to memory block `6`.

Since each block contains 16 bytes, block `6` contains:

```text
Addresses 96–111
```

Each of those addresses refers to one 8-bit word:

```text
Block 6:

+----+----+----+----+-----+-----+-----+-----+-----+-----+-----+ ... +-----+
| 96 | 97 | 98 | 99 | 100 | 101 | 102 | 103 | 104 | 105 | 106 |     | 111 |
+----+----+----+----+-----+-----+-----+-----+-----+-----+-----+ ... +-----+
 8b   8b   8b   8b    8b    8b    8b    8b    8b    8b    8b         8b
```

So the entire cache block stores:

```text
16 bytes × 8 bits per byte = 128 bits
```

Suppose cache line `2` currently contains block `6`:

```text
          +-------+----------------------------+----------------+
Line 2 →  | Valid | Tag                        | Data           |
          +-------+----------------------------+----------------+
          |   1   | 00000000000000000000000001 | bytes 96–111   |
          +-------+----------------------------+----------------+
```

The requested tag matches the stored tag, and the valid bit is `1`, so this is a **cache hit**.

Finally, the offset is `1001₂ = 9`. Since we are returning one 8-bit word at a time, the offset selects the ninth byte position within the block:

```text
Cached memory block 6:

Address:  [96][97][98][99][100][101][102][103][104][105][106] ... [111]
Offset:    0   1   2   3    4    5    6    7    8    9   10  ...   15
                                                     ↑
                                                offset 1001₂
```

So the cache returns the **8-bit value stored at address 105**.

In this example:

```text
Address 105
    ↓
Tag 1       → confirms the correct memory block
Index 2     → selects cache line 2
Offset 9    → selects byte 9 within the block
    ↓
Return 8 bits = 1 byte
```

The important distinction is that the **block contains 16 bytes total**, while each individual access in this example returns **one byte = 8 bits**.
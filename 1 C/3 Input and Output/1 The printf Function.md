The `printf` function is designed to display the contents of a string, known as the *format string*, and values can be inserted into the string.

The formal string can contain normal characters, and converted characters with a conversion specification (the ones beginning with the % character).

A conversion specification is a placeholder representing a value to be filled in during printing, telling it how the value should be converted from binary to a printed form.

![[C Programming A Modern Approach (K. N. King) (Z-Library).jpg|500]]

[[C Programming A Modern Approach (K. N. King) (Z-Library).pdf#page=67&rect=185,491,502,630&color=yellow|C Programming A Modern Approach (K. N. King) (Z-Library), p.38]]

The ordinary characters acted normally, while the converted specifications are replaced by the values of the variables.

---
## Conversion Specifications

This is a bit... on the nail polish side of things, so I'll just throw it here, glancing over it.

A conversion specification can have the form `%m.pX` or `%-m.pX`, where m and p are integer constants and X is a letter.

- X (type conversion)
	- There's a huge list of this stuff, we'll just put some of the common ones.
	- - **%d** — signed decimal integer
	- **%u** — unsigned decimal integer
	- **%x** **/** **%X** — unsigned hexadecimal (lowercase / uppercase)
	- **%f** — floating-point number (decimal notation)
	- **%c** — single character
	- **%s** — C string (char *)
	- **%p** — pointer address

- m (field width)
	- Minimum number of characters to print
    
- **.** p (precision), depends on type
    - integers → minimum digits
    - floats → digits after decimal
    - strings → max characters printed

---
## Escape Sequences

The \n code that we often use in format strings is called an escape sequence, there are a couple of them:
- Alert - `\a`
- Backspace - `\b`
- New line - `\n`
- Horizontal tab - `\t`


This isn't a long chapter, it's a transitional chapter between writing a VM translator from VM Byte-code to assembly, and writing a compiler from a high level language (Jack) to VM Byte-code.

We need to first know what the high level language is before we can translate it, right? Jack isn't a huge language, it looks similar alike Java, we'l just throw you some syntax and get this chapter over with.

Take a look at Jack's "Hello world" program.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 61.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=237&rect=132,480,480,627|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.237]]

So, sorry that this note won't look like it's got much substance in it, it's just a big old list of Jack syntax.

## Syntactic Elements

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 62.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=243&rect=106,300,513,730|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.243]]

### Program Structure

Jack uses classes, and for any Jack files under the same folder, you need a file called `Main`, it needs a class called `main`, and needs to contain the `Main.main` function.

The class declaration has the following structure:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 63.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=244&rect=65,576,489,667|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.244]]

And within each class, you can have subroutines declared 1 of 3 types:

- method
- function
- constructor

A subroutine follows this structure:

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 64.jpg|200]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=244&rect=62,311,263,379|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.244]]

## Data Types

Primitively, there are only 3 data types in Jack for the sake of simplicity.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 65.jpg|200]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=245&rect=62,306,258,382|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.245]]

The rest are all made through the OS (in chapter 12)

## Variables

There are 4 kinds of variables in Jack.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 66.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=248&rect=130,134,485,302|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.248]]

### Statements

these are very similar in other programming languages.

![[The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed 67.jpg|500]]

[[The Elements of Computing Systems Building a Modern Computer from First Principles.pdf#page=249&rect=70,159,423,457|The Elements of Computing Systems, Building a Modern Computer from First Principles 2 ed, p.249]]

### Go Programming...?

There is no "big project" for this chapter, the book just wants you to get your hands dirty by practicing programming some Jack programs out, it's not crazy rocket science.

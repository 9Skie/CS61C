As we know, computers can only store numbers (in bits), so how is it able to represent characters, and make up strings (as combinations of characters) with numbers?

There's a good video about this... and I've watched it a long time ago as well.

https://www.bilibili.com/video/BV1ai4y1x7Uz

Historically, as computers were invented in America, the Americans simply thought about creating a mapping between characters and a table of numbers, ASCII.

![[Pasted image 20260208114928.png|500]]

Basically, it mapped most commonly used ENGLISH symbols, characters, punctuation etc to numbers.

But this created a problem, as other countries like china and korea got hands on computers as well, they were also faced with the same problem of converting their text into numbers for the computer to store.

And so... everyone just created their own charts, China made GBK, Korea make KSC... etc, and nobody matched each other's encoding.

Like in China's case, there were about 20K+ characters to encode, compared to the 128 characters in ASCII. So, this created lots of problem between sending data across computers with different text encodings in different countries.

Solution? Unicode, get a huge conversion chart! UTF-8 is the mainstream version nowadays, which allows variable length encoding for different languages, like English just requires 1 byte due to how little characters it has, Chinese uses 4... and on.
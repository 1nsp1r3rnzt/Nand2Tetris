It may be instructive to describe the thought process that led to the design of this particular ALU. First, we made a list of all the primitive operations that we wanted our computer to be able to perform . Next, we used backward reasoning to figure out how x, y, and out can be manipulated in binary




For creating NOT gate from NAND gate, draw truth table of both gates. 

A NAND gate
|a|b|Out|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|

A NOT gate

|in|Out|
|0|1|
|1|0|

Now, think about the difference between the two.
one major difference is that a NOT gate has only single input.

Now, think about how can we run a NAND gate on a single input.
We can plug a same input, both to `a` and `b` of a NAND gate.

Lets draw the TRUTH table for that.

Connect a single input named `in`  to both wires of a NAND gate.
|in|a=in|b=in|Out|
|0 |  0 |0   |1|
|1 |  1 |1   |0|

Now, only these two states will exist as `b` would have same input as `a`.

So, the following two states would never exist in such case.
|a|b=a|Out|
|0|1|1|
|1|0|1|


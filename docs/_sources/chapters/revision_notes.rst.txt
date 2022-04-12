Revision notes
==============

Truth tables
------------

0 is ``False``, 1 is ``True``.

==== ==== =======
A    B    A AND B
==== ==== =======
0    0    0
0    1    0
1    0    0
1    1    1
==== ==== =======

==== ==== =======
A    B    A OR B
==== ==== =======
0    0    0
0    1    1
1    0    1
1    1    1
==== ==== =======

==== ==== =======
A    B    A XOR B
==== ==== =======
0    0    0
0    1    1
1    0    1
1    1    0
==== ==== =======

==== =====
A    NOT A
==== =====
0    1
1    0
==== =====

Data types
--------------
======  =====================        ============
Type    Examples                     Meaning
======  =====================        ============
bool    True, False                  Boolean
int     1, 5, 0, -3                  Integer
float   1.0, 0.56, -17.1             Floating point, real
str     'abc', "hello", "10"         String
char    'a', 'z'                     Character [1]_
list    [1, 2, 3]                    List
dict    {'a': 1}                     Dictionary
======  =====================        ============


.. topic:: noo

   foo
   woo sdf

   sdfs

.. NOTE:: this is a note
   note
   foo

   sdfsdf

.. tip:: this is a tip
   note
   foo

   sdfsdf

.. admonition:: And, by the way...

   You can make up your own admonition too.

.. sidebar:: Optional Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   ==== ==== =======
   A    B    A AND B
   ==== ==== =======
   0    0    0
   0    1    0
   1    0    0
   1    1    1
   ==== ==== =======



.. [1]
   Character is not a type in Python, it is just a string of length 1.

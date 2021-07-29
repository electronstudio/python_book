Drawing graphics
================

To create graphics for our games we will use `the Pygame Zero
library <https://pygame-zero.readthedocs.io>`__\  [1]_. You will find
the documentation on the website useful!

The smallest square that can be displayed on a monitor is called a
*pixel*. This diagram shows a close-up view of a window that is 40
pixels wide and 40 pixels high. At normal size you will not see the grid
lines.

.. figure:: images/figures/pixelgrid.pdf
   :alt: Model View Controller

   Model View Controller

We can refer to any pixel by giving two co-ordinates, *(x,y)* Make sure
you understand co-ordinates before moving on because everything we do in
Pygame Zero will use it. (In maths this called a ‘Cartesian coordinate
system’).

Lines and circles
-----------------

If are using the Mu editor, Pygame Zero is built-in, but **you must
remember to click ‘Mode’ and select ‘Pygame Zero’ before running your
program**!

If you are using a different editor, `instructions are
online <https://pygame-zero.readthedocs.io/en/stable/ide-mode.html>`__\  [2]_

.. literalinclude:: programs/10_lines_circles.py
   :caption: Lines and circles
   :name: code-lines_circles
   :linenos:



.. topic:: Exercise

   Finish drawing this picture


.. topic:: Exercise

   Draw your own picture.

   \newpage

Moving rectangles
-----------------

To make things move we need to add the special ``update()`` function. We
don’t need to write our own loop because *Pygame Zero calls this
function for us in its own loop*, over and over, many times per second.

.. literalinclude:: programs/11_moving_boxes.py
   :caption: Moving rectangles
   :name: code-moving_boxes
   :linenos:



.. topic:: Exercise

   Make the box move faster.


.. topic:: Exercise

   Make the box move in different directions.


.. topic:: Exercise

   Make two boxes with different colours.




Actor sprites
-------------

Actor sprites are very similar to boxes! Click ``Images`` to see the
folder of image files available. ``alien.png`` should already be there,
but for other images you must add the files yourself.

You could use Microsoft Paint which comes with Windows but I recommend
you download and install `Krita <https://krita.org>`__\  [3]_.

.. literalinclude:: programs/12_sprites.py
   :caption: Actor sprites
   :name: code-sprites
   :linenos:



.. topic:: Exercise

   Draw or download your own image to use instead of alien.




Background image
----------------

We are going to add a background image to
:numref:`code-sprites`

Click ``Images`` to see the folder of image files available.

**You must create or download a picture to use a background. Save it as
``background.png`` in the directory ``mu_code/images``. It should be the
same size as the window, 500×500 pixels and it must be in ``.png``
format.**

.. literalinclude:: programs/12b_background.py
   :caption: Background
   :name: code-background
   :linenos:



.. topic:: Exercise

    Create a picture to use a background.  Save it as `background.png`.  Run the program.




Keyboard input
--------------

The alien moves when you press the cursor keys.

.. literalinclude:: programs/13_keyboard_input.py
   :caption: Keyboard input
   :name: code-keyboard_input
   :linenos:



.. raw:: latex

   \begin{aside}
   \label{exercise:updown}
   \heading{}
   \noindent Make the alien move up and down as well as left and right.


.. topic:: Exercise

   Use the more concise += operator to change the `alien.x` value (see :numref:`code-shortcuts`).


.. topic:: Exercise

    Use the `or` operator to allow WASD keys to move the alien in addition to the cursor keys (see :numref:`code-logic`).




.. [1]
   https://pygame-zero.readthedocs.io

.. [2]
   https://pygame-zero.readthedocs.io/en/stable/ide-mode.html

.. [3]
   https://krita.org

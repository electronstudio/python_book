Drawing graphics
================

To create graphics for our games we will use `Raylib <https://www.raylib.com/>`__
along with `my RLZero
library <https://electronstudio.github.io/rlzero/>`__. You will find
the documentation on the websites useful!

Installing the graphics library
-------------------------------

Installing a Python package varies depending on what Python editor or IDE
you are using.
Here is how you do it if you are using the Mu editor.

Run *Mu*. Click **Mode** and select **Python3**.  Then click *the small gadget icon* in the bottom right
hand corner of the
window. Click **third party packages**. Type

::

   rlzero

into the box. Click **OK**. The library will download.

*If you are not using Mu* you can install from the
command line like this:

::

   pip3 install rlzero

RLZero and Raylib
-----------------

Raylib is a graphics library.  RLZero adds some extra functions to Raylib to make
it easier to use.  Once you have installed RLZero you are free to use all the
functions of Raylib - you don't have to stick to the RLZero features.

Specifically, whenever we use a function prefixed by ``screen.`` that is a Raylib
function.  You can use any function from the
`Raylib documentation <https://electronstudio.github.io/raylib-python-cffi/pyray.html>`__
if you prefix it with ``screen``.

The RLZero functions don't need a prefix.

Pixels
------

The smallest square that can be displayed on a monitor is called a
*pixel*. This diagram shows a close-up view of a window that is 40
pixels wide and 40 pixels high. At normal size you will not see the grid
lines.

.. figure:: images/figures/pixelgrid.png
   :width: 70%




We can refer to any pixel by giving two co-ordinates, *(x,y)* Make sure
you understand co-ordinates before moving on because everything we do in
Pygame Zero will use it. (In maths this called a ‘Cartesian coordinate
system’).

.. literalinclude:: programs/pixels.py
   :caption: A pixel
   :name: code-pixels
   :linenos:

.. topic:: Exercise

   Make this pixel blue.

Lines and circles
-----------------

.. literalinclude:: programs/10_lines_circles.py
   :caption: Lines and circles
   :name: code-lines_circles
   :linenos:



.. topic:: Exercise

   Finish drawing this picture


.. topic:: Exercise

   Draw your own picture.



Moving rectangles
-----------------

To make things move we need to add the special ``update()`` function. We
don’t need to write our own loop because *RLZero calls this
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




Sprites
-------------

Sprites are very similar to boxes, but are loaded from a **png** or **jpg** image file.
RLZero has one such image built-in,
``alien.png``.  If you want to use other images you must create them
and place the files in the same directory as your program.

You could use Microsoft Paint which comes with Windows but I recommend
you download and install `Krita <https://krita.org>`__.

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

**You must create or download a picture to use a background.** Save it as
``background.png`` in the folder with your program. It should be the
same size as the window, 500×500 pixels and it must be in ``.png``
format.

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



.. topic:: Exercise

   Make the alien move up and down as well as left and right.


.. topic:: Exercise

   Use the more concise += operator to change the `alien.x` value (see :numref:`code-shortcuts`).


.. topic:: Exercise

    Use the `or` operator to allow WASD keys to move the alien in addition to the cursor keys (see :numref:`code-logic`).





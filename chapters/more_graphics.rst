Improving your games
====================

Here are some tips that will enable you to enhance your games.



Game controllers
----------------

You may call them *joysticks* or *controllers*, but Raylib calls them
*gamepads*.

Some controllers have different inputs and some are not compatible at
all so don’t be surprised if this doesnt work properly! PS4 and Xbox One
controllers connected by USB cable seems to work best.

.. literalinclude:: programs/14_joystick_input.py
   :caption: Joystick input
   :name: code-joystick_input
   :linenos:



.. topic:: Optional, if you have a controller

   Make the alien move up and down as well as left and right using the controller.  Do the same for any other examples that use the keyboard!


Colours
-------

.. Note::
   The word *colour* is incorrectly spelt *color* in American programs such as Raylib.
   We will try to use the correct spelling wherever we can but sometimes you will have to use
   *color*.

Instead of using ready made colours like ``RED``, ``YELLOW``, etc. you can
create your own colour with a *tuple* of three numbers. The numbers must
be between 0 - 255 and represent how much *red*, *green* and *blue* to
mix together.

.. literalinclude:: programs/25_colours.py
   :caption: RGB colours
   :name: code-colours
   :linenos:



.. topic:: Advanced

   Change the green and blue amounts to make different colours.


.. topic:: Exercise

   Make a gray colour.


.. topic:: Advanced

   Make random colours.  (see :numref:`codemaths`).




Using loops
-----------

The loops from :numref:`codeloop` are useful for
graphical games too! Here we draw red circles using a *for loop*.

We draw green circles using a *loop within another loop*.

.. literalinclude:: programs/20_loops.py
   :caption: Loops are useful
   :name: code-loops
   :linenos:



.. topic:: Exercise

   `import random` at the top of the program and then make the positions random, e.g::

      x = random.randint(0, 100)



.. topic:: Advanced

    Learn about `RGB colour <https://en.wikipedia.org/wiki/RGB_color_model>`_ and make random colours (see :numref:`code-colours`).


.. topic:: Advanced

   Create a timer variable and change colours based on time (see :numref:`code-timer`)


Fullscreen mode
---------------

Sometimes it is nice to play your game using the entire screen rather
than in a window. This program show how to enter fullscreen and and how to quit.

.. literalinclude:: programs/26_fullscreen_mode.py
   :caption: Fullscreen mode
   :name: code-full_screen_mode
   :linenos:

.. note::

   RLZero **automatically** uses the *F* key for fullscreen and *Escape* key to quit, so
   you don't actually need this code in your programs unless you want to use a different key.




Displaying the score
--------------------

This game shows how you can keep the score in a variable and print it on
to the game screen. You can display any other messages to the player the
same way.

.. literalinclude:: programs/27_displaying_text.py
   :caption: Keeping score in a variable and displaying it
   :name: code-displaying_text
   :linenos:



.. topic:: Exercise

    Make the score text larger.


.. topic:: Advanced

   Add a second player who presses a different key and show their score too.


.. topic:: Exercise

   Add text to one of your other games.

Animation
----------------

*Animation* is a RLZero class that makes it easy to show a sequence of different
images on the same Sprite.  You need to give it the image file names and the number
of frames-per-second you want.

.. literalinclude:: programs/animation.py
   :caption: Animation
   :name: codeanimation
   :linenos:

.. topic:: Exercise

    Draw three images of a man walking and save them as *man1.png*, *man2.png*, *man3.png*.
    Edit the program so it animates these images.

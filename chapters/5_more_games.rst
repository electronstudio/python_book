More advanced games
===================

These games demonstrate some essential building blocks you will need to
make more advanced games of your own.



Lists
-----

We introduced lists in Program~:raw-latex:`\ref{code:arrays}`. In this
game, we create an empty list ``[]`` and use a loop to fill it with
alien Actors.

We again use loops to draw all the aliens and move all the aliens in the
list. When the mouse is clicked we add a new alien to the list.

.. raw:: latex

   \begin{codelisting}
   \codecaption{Lists are useful in games!}
   \label{code:arrays2}
   <<(programs/21_arrays.py)
   \end{codelisting}

.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent Go back to a previous game (e.g. Program~\ref{code:collisions})
   and add a list of bullets that move up the screen.  When the player presses the spacebar to shoot,
   add a new bullet to the list.


Animation
---------

Animation is another use for functions. (See
Program~:raw-latex:`\ref{code:functions}`) We define our own function
and then ask Pygame to *call it back* every 0.2 seconds. Most of this
code is from Program~:raw-latex:`\ref{code:collisions}`.

.. raw:: latex

   \begin{codelisting}
   \codecaption{Animation}
   \label{code:animation}
   <<(programs/22_animation.py)
   \end{codelisting}

.. topic:: Exercise

   Make the alien animate more quickly.


.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent Add another image to the list of images.


.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent Draw your own animation, e.g. a man walking left which plays when the left key is pressed


.. raw:: latex

   \pagebreak

Simple physics
--------------

Here we draw a ball and move it, like we did in
Program~:raw-latex:`\ref{code:moving_boxes}`. But instead of moving it
by a fixed number of pixels, we store the number of pixels to move in
variables, ``vx`` and ``vy``. These are *velocities*, i.e. speed in a
fixed direction. ``vx`` is the speed in the horizontal direction and
``vy`` is the speed in the vertical direction. This allow us to change
the velocity. Here we reverse the velocity when the ball hits the edge
of the screen.

.. raw:: latex

   \begin{codelisting}
   \codecaption{Simple physics: velocity}
   \label{code:simple_physics}
   <<(programs/23_simple_physics.py)
   \end{codelisting}

.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent Make the ball move faster by increasing its velocity each time it hits the sides.


.. raw:: latex

   \pagebreak

Bat and ball game
-----------------

*Pong* is the classic bat and ball game.

.. raw:: latex

   \begin{codelisting}
   \codecaption{Pong}
   \label{code:pong}
   <<(programs/24_pong.py)
   \end{codelisting}

.. raw:: latex

   \pagebreak

.. topic:: Exercise

   Make the ball move more quickly.


.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent Add another bat at the top of the screen for player 2.


.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent Add bricks (Rects) that disappear when the ball hits them.


.. raw:: latex

   \pagebreak

Timer
-----

The ``update()`` and ``draw()`` functions are called by Pygame many
times every second. Each time ``draw()`` is called we say it draws one
*frame*. The exact number of frames per second is called the *framerate*
and it will vary from one computer to another. Therefore counting frames
is not the most reliable way of keeping time.

Fortunately Pygame can tell us exactly how much many seconds have passed
since the last frame in a parameter to our update function. We use this
*delta time* to keep a timer.

.. raw:: latex

   \begin{codelisting}
   \codecaption{Timer}
   \label{code:timer}
   <<(programs/28_timer.py)
   \end{codelisting}

.. topic:: Exercise

   Make the timer count down, not up.


.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent Add a timer to one of your other games.


.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent Add a timer to Program~\ref{code:arrays} that deletes one of the aliens when the timer runs out, then starts the timer again.


.. raw:: latex

   \pagebreak

Callbacks: another kind of timer
--------------------------------

Pygame has its own clock which we can use by asking it to *callback* one
of our functions at a certain time, or regularly over and over at an
interval.

.. raw:: latex

   \begin{codelisting}
   \codecaption{Timer with callback functions}
   \label{code:timer2}
   <<(programs/29_timer2.py)
   \end{codelisting}

.. topic:: Exercise

    Make the aliens appear more often.


.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent Use ```len(aliens)``` to print how many aliens there are


.. raw:: latex

   \begin{aside}
   \label{}
   \heading{Advanced}
   \noindent When there are too many aliens, stop adding them using this code:
   ```python
          clock.unschedule(add_alien)
   ```


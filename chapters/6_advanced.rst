Advanced topics
===============

Instructor note
---------------

This is the beginning of my attempts to teach object oriented
programming, but I wouldn’t attempt this with young students since it
requires abstract thinking.

Classes
-------

You’ve already been using class types provided by Pygame Zero, e.g. Rect
and Actor. But if we want to store velocity as in
Program~:raw-latex:`\ref{code:simple_physics}` we find these classes do
not include *vx* and *vy* variables inside them by default. We have to
remember to add a *vx* and *vy* every time we create an Actor.

So let’s create our own class, called *Sprite*, that is the same as
Actor but with these variables included.

.. literalinclude:: programs/26_classes.py
   :caption: Classes
   :name: code-classes
   :linenos:





Methods
-------

Classes can contain functions (called *methods*) as well as variables.
Methods are the best place to modify the class’s variables.

.. literalinclude:: programs/27_classes2.py
   :caption: Class methods
   :name: code-classes2
   :linenos:





Joystick tester
---------------

This program demonstrates using joysticks and for loops, but is mainly
included to help you test the input from your controllers.

(I don’t suggest typing this one yourself.)

.. literalinclude:: programs/19_joystick_tester.py
   :caption: Joystick tester
   :name: code-joystick_tester
   :linenos:





Distributing your Pygame Zero games
-----------------------------------

This is often tricky to get working, but you can distribute your games
to people who don’t have Python or Mu installed. You can put them on a
USB stick, or a website for people to download, or even on itch.io for
people to buy.

1. Install the full version of python from
   `www.python.org <https://www.python.org/downloads/>`__.

2. Edit your game source code (using Mu). We will assume your source is
   in a file ``NAME_OF_GAME.py``. At the top of the file add the line:

.. code:: python

   import pgzrun

At the bottom of the file add the line:

.. code:: python

   pgzrun.go()

Any time in the program you use ``draw.text()`` you *must* specify a
font, e.g. add parameter ``fontname="arial"``

Save the file.

3. Copy any fonts you have used into the ``fonts`` folder and rename
   them to lowercase names, e.g. ``arial.ttf``

4. Open a command prompt (Click start menu and type ``cmd.exe``)

5. Enter your mu_code folder. At the prompt type:

   ``cd mu_code``

6. Install pyinstaller and pgzero. At the command prompt type:

   ``pip install pgzero pyinstaller``

7. You should find the *pgzero* folder at:

   :raw-latex:`\verb+C:\Users\YOURNAME\AppData\\Local\\Programs\+`

   :raw-latex:`\verb+Python\Python37\Lib\site-packages\pgzero+`

   This is a hidden folder so you must enable hidden folders in Windows
   Explorer to see it.

   Copy the *pgzero* folder into your *mu_code* folder.

   You should find your *mu_code* folder at:
   :raw-latex:`\verb+C:\Users\YOURNAME\mu_code+`

8. Create the executable. At the command prompt type:

   ``pyinstaller NAME_OF_GAME.py --distpath . --add-data "pgzero;pgzero" --add-data "images;images" --add-data "fonts;fonts" --add-data "sounds;sounds" --add-data "music;music" --onefile --noconfirm --windowed --clean``

   This will generate a program called ``NAME_OF_GAME.exe``. You can
   double click this program to play your game.

9. To distribute your game you need to copy the entire *mu_code* folder.
   You could put it inside a zip file, and then put that on a website

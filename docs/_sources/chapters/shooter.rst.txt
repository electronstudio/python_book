Tutorial: Shooting game
=======================

In this chapter we will build a shooting game together, step by step.
The Python we will use is: conditionals, loops, lists and functions.

Step 1: Decide what Sprites you will need
-----------------------------------------

Our game will need these Sprites, so **we must create images for all of
them and save them** as ``.png`` files in the program folder.

============== =============== ==========
variable name  image file name image size
============== =============== ==========
player         player.png      64x64
background     background.png  600x800
enemies (list) enemy.png       64x64
bullets (list) bullet.png      16x16
bombs (list)   bomb.png        16x16
============== =============== ==========

The ``player`` and ``background`` variables will contain Sprites. The
others are lists which we initialize to the empty list ``[]``. Sprites
will be appended to the lists later.



.. literalinclude:: programs/shoot17a.py
   :caption: Shooter game part 1 of 4
   :name: code-shoot17a
   :linenos:



Step 2: Draw your Sprites
-------------------------

Every RLZero game needs a ``draw()`` function, and it should draw all
the Sprites we created above.

.. literalinclude:: programs/shoot17b.py
   :caption: Shooter game part 2 of 4
   :name: code-shoot17b
   :linenos:





Step 3: Move your Sprites
-------------------------

Every RLZero game needs an ``update()`` function to move the Sprites,
check for collisions, etc.

.. literalinclude:: programs/shoot17c.py
   :caption: Shooter game part 3 of 4
   :name: code-shoot17c
   :linenos:




Step 4: Define your functions
-----------------------------

Python cannot call a function that has not yet been defined. Therefore
we must at least provide empty, dummy versions of our functions that
don’t do anything so we can fill them in later. However Python cannot
define a completely empty function - it must contain at least one line.
Therefore we use the ``pass`` keyword to create a line that doesn’t do
anything.

.. literalinclude:: programs/shoot17d.py
   :caption: Shooter game part 4 of 4
   :name: code-shoot17d
   :linenos:



.. topic:: Exercise

   Create the png image files (``player.png, background.png, bullet.png, bomb.png, enemy.png``).  Type in program :numref:`code-shoot17a`, :numref:`code-shoot17b` and :numref:`code-shoot17c` and :numref:`code-shoot17d` into a single file.  Verify the game now runs and you can see the player at the bottom of the screen.  (He can't move yet.)


Create enemies
--------------

Add this new function to the end of the program, and then call it
immediately. It uses a loop within a loop to create enemy Sprites and put
them in the ``enemies`` list. The reason we put this in a function is we
will need to call it again at the start of each level.

..  code:: python

    def create_enemies():
        for x in range(0, 600, 60):
            for y in range(0, 200, 60):
                enemy = Sprite("enemy.png", (x, y))
                enemy.vx = level * 2
                enemies.append(enemy)


   create_enemies()

Move the player
---------------

Replace the ``move_player()`` dummy function definition with this.
Remember **there can only be one function with a given name**. *There
cannot be two ``move_player()`` function definitions.*

..  code:: python

    def move_player():
        if keyboard.right:
            player.x = player.x + 5
        if keyboard.left:
            player.x = player.x - 5
        if player.x > WIDTH:
            player.x = WIDTH
        if player.x < 0:
            player.x = 0




Move the enemies
----------------

Replace the ``move_enemies()`` dummy function definition with this:

..  code:: python

    def move_enemies():
        global score
        for enemy in enemies:
            enemy.x = enemy.x + enemy.vx
            if enemy.x > WIDTH or enemy.x < 0:
                enemy.vx = -enemy.vx
                enemy.y += 60
            for bullet in bullets:
                if bullet.colliderect(enemy):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score = score + 1
            if enemy.colliderect(player):
                exit()

Draw text on the screen
-----------------------

Replace the ``draw_gui()`` dummy function definition with this:

..  code:: python

    def draw_gui():
        draw_text("Level " + str(level), 0, 0, 20, RED)
        draw_text("Score " + str(score), 100, 0, 20, RED)
        draw_text("Lives " + str(lives), 200, 0, 20, RED)


Player bullets
--------------

Add this new function to the end of the program. Pygame will call it for
us automatically when a key is pressed.

..  code:: python

    def on_key_pressed(key):
        if key == keys.space and len(bullets) < MAX_BULLETS:
            bullet = Sprite("bullet.png", pos=(player.x, player.y))
            bullets.append(bullet))

Replace the ``move_bullets()`` dummy function definition with this:

.. code:: python

   def move_bullets():
       for bullet in bullets:
           bullet.y = bullet.y - 6
           if bullet.y < 0:
               bullets.remove(bullet)

Enemy bombs
-----------

Replace the ``create_bombs()`` dummy function definition with this:

.. code:: python

   def create_bombs():
       if random.randint(0, 100 - level * 6) == 0:
           enemy = random.choice(enemies)
           bomb = Sprint("bomb.png", enemy.pos)
           bombs.append(bomb)

Replace the ``move_bombs()`` dummy function definition with this:

.. code:: python

   def move_bombs():
       global lives
       for bomb in bombs:
           bomb.y = bomb.y + 10
           if bomb.colliderect(player):
               bombs.remove(bomb)
               lives = lives - 1
               if lives == 0:
                   exit()



Check for end of level
----------------------

Replace the ``check_for_end_of_level()`` dummy function definition with
this:

.. code:: python

   def check_for_end_of_level():
       global level
       if len(enemies) == 0:
           level = level + 1
           create_enemies()

Ideas for extension
-------------------

-  Draw an explosion image and create an explosion Sprite every time an
   alien dies.

-  Make the explosion Sprite disappear after a short time.

-  Draw several explosion images, put them in a list and make the Sprite
   animate displaying each of them in order.

-  The player can only fire 3 bullets at a time. Create a powerup that
   allows him to fire additional bullets.

-  Add music and sound effects.

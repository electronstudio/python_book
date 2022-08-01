Tutorial: Network coding
========================

Sockets
-------

A socket connects a program on one computer to a program running on another computer.  One program writes data into its socket.  The data may be raw bytes, or any
of the datatypes we have seen (e.g. integer, string, etc.) The data travels across the network.  The program
on the other computer reads the data from its socket.

Connecting a socket is a bit like making a phone call.  The program that is waiting to receive the call is the *server*.  The program
that makes the call is the *client*.  Once the call is connected they can both speak to each other.

If possible, you should run the server program on one computer and the client program on a different computer,
both connected to the same network.  If you don't have two computers you can run both programs on the same computer.
Using Mu, you will have to load two copies of Mu in order to run two programs at the same time.

First find out the IP address of your server computer and write it down.  The easiest way to open a command terminal
and type a command.  Possible commands:

- ``ipconfig`` (Windows)
- ``ifconfig`` (Mac)
- ``ip address`` (Linux)

The IP address will look similar to this: *192.168.0.105*

Enter and run the server program:

.. literalinclude:: server1.py
   :caption: Socket server
   :name: code-server
   :linenos:

After creating the socket, we *bind()* it to an *internet address*.  **0.0.0.0** is a special address that means "any address belonging
to this computer".  We also give a *port number*, **65439**.  This can be (almost) any number, but it must match on the client
and server.

Then we *listen()*, which pauses the program until a connection arrives.  Then we read a line from the socket connection
and print it out.

Enter and run the client program.  We have put the address of the server in a variable.  If your server is on a different
computer, use the address of that computer.  If it on the same computer, use the special address **127.0.0.1**.

.. literalinclude:: client1.py
   :caption: Socket client
   :name: code-client1
   :linenos:

Note that we send a string, but we prefix it with *b* to convert it into bytes.  We close the socket after
we are finished to end the connection.

You should see the string appear on the server program output.

.. topic:: Exercise

   Send a different message from the client to the server.

.. topic:: Exercise

   Make the client program ask the user to input a message, and then send it to the server.  Make a loop so it keeps
   asking and sending.


Gopher
------

Gopher is a hypertext system, similar to the World Wide Web.  However Gopher is older than the web, and its protocol
is simpler, which makes it easier for us to implement.  A *protocol* is just an agreement between the client and server
on what sort of data they are allowed to send and receive.

We are going to write a Gopher client, connect it to a Gopher server, and see if we can figure out the protocol.

.. literalinclude:: gopher.py
   :caption: Gopher client
   :name: code-gopher
   :linenos:

You can change the server to connect to any gopher server, but we are using *gopher.floodgap.com* because it is popular.

When you run the program, it simply sends **"\\r\\n"** which means a return followed by a newline.  It then prints
the lines it gets back from the server.  You should get some output that looks a bit like this:

::

   iWelcome to Floodgap Systems' official gopher server.		error.host	1

   iFloodgap has served the gopher community since 1999		error.host	1

   i(formerly gopher.ptloma.edu).		error.host	1

This is readable, but we can improve it.  You might notice that every line starts with a special character,
usually an **i** (meaning *info*).  This isn't part of the text, so we will chop it off.

Python lists and strings allow us *slice* them up.  For example, if you have a string

::

   s = "Hello"

Then these some slices you could make:

::

   s[0] == "H"
   s[1] == "e"
   s[0:4] == "Hell"
   s[1:] == "ello"
   s[:2] == "He"


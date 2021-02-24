************
On-board IDE
************

You can interactively run Python and transfer data through CodeBug Connect's on-board IDE. You access through a web browser so you need to be able to access CodeBug Connect over your local network, or connect directly to CodeBug Connect's access point. See :doc:`setup_wifi` for more details.

The IDE consists of a file browser, file editor and terminal.

File Browser
============

Use the file browser to explore what is stored on your CodeBug Connect, or perform file operations such as creating new files or directories. Click on a file to open it in the Text Editor

Text Editor
===========

Use the text editor to update your python programs. For now, due to space constraints you cannot update block programs without using the full www.codebug,.org.uk website.

Terminal
========

The terminal allows you to run Python interactively and also see the results of programs. Why not try typing the following in it:

.. code-block:: python

    import cbc
    cbc.display.scroll_test("hello me!")

or

.. code-block:: python

    print("hello world")


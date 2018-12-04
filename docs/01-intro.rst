=====================================
Option complémentaire en informatique
=====================================

Ce site GitHub contient le matériel pour le cours d'option complémentaire 
en informatique du gymnase du Bugnon.

Les sujets sonts: 

* Raspberry Pi
* GitHub
* Linux
* LaTeX
* Python
* Jupyter Lab
* Jupyter Notebook
* Widgets
* Bokeh
* Matplotlib
* NumPy
* SciPy
* OpenCV
* MarkDown
* reStructuredText
* Sphinx
* HTML
* CSS
* Pygame
* Minecraft

Once Sphinx is :doc:`installed <glossary>`, you can proceed with
setting up your first Sphinx project. To ease the process of getting started,
Sphinx provides a tool, :program:`sphinx-quickstart`, which will generate a
documentation source directory and populate it with some defaults. We're going
to use the :program:`sphinx-quickstart` tool here, though it's use by no means
necessary.


Préparation de l'infrastructure
------------------------------------

The root directory of a Sphinx collection of :term:`reStructuredText` document
sources is called the :term:`source directory`.  This directory also contains
the Sphinx configuration file :file:`conf.py`, where you can configure all
aspects of how Sphinx reads your sources and builds your documentation. 

.. code-block:: shell

   $ pip install jupyter
   $ jupyter labextension list

Sphinx comes with a script called :program:`sphinx-quickstart` that sets up a
source directory and creates a default :file:`conf.py` with the most useful
configuration values from a few questions it asks you. To use this, run:

.. code-block:: shell

   $ sphinx-quickstart


.. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)

 
 The :py:func:`enumerate` function can be used for ...

 Lists
 -----

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.


* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues


Definition list
---------------

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

 Line blocks
 -----------

| These lines are
| broken exactly like in
| the source file.


Literal blocks
--------------

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

Doctest blocks
--------------

>>> 1 + 1
2

Tables
------

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

This is another form.

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

Hyperlinks
----------

Use `EPFL <https://www.epfl.ch/>`_ for inline web links.

If link text and link are the same use : https://www.epfl.ch without any special formatting.


This is a heading
=================

This is a heading
-----------------

.. this is a comment

.. code-block:: shell

   $ sphinx-quickstart



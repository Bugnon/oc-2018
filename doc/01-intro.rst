=====================================
Option complémentaire en informatique
=====================================

Once Sphinx is :doc:`installed </usage/installation>`, you can proceed with
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
aspects of how Sphinx reads your sources and builds your documentation.  [#]_

Sphinx comes with a script called :program:`sphinx-quickstart` that sets up a
source directory and creates a default :file:`conf.py` with the most useful
configuration values from a few questions it asks you. To use this, run:

.. code-block:: shell

   $ sphinx-quickstart

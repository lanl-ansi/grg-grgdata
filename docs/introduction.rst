============
Introduction
============

Overview
------------------------

grg-grgdata is a minimalist python package for working with of GRG_ network data files.

The primary entry point of the library is :class:`grg_grgdata.cmd` module, which contains the methods for GRG data validation.


Installation
------------------------

Simply run::

    pip install grg-grgdata


Testing
------------------------

grg-grgdata is designed to be a library that supports other software.
It is not immediately useful from the terminal.
However, you can test the validation functionality from the command line with:: 

    python -m grg_pssedata.cmd <path to GRG data file>

If this command is successful, you will see a message indicating that the given data is a valid GRG file printed to the terminal.

.. _GRG: https://gdg.engin.umich.edu/


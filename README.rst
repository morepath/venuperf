Venusian Performance Testing
============================

This is simple performance testing tool for Venusian.

Usage
-----

Set up a virtualenv, then in virtualenv::

  $ pip install venusian==1.0a8

(or some other version of Venusian)

Then create a package named fixture that we can then measure::

  $ python create_fixture.py 100

This create a fixture package with 100 python modules in it that use
Venusian-style decorators. Each module has 30 decorators; it's a copy
of ``sample.py``.

Then to run the performance test::

  $ python main.py

This scans that fixture package reports on the time taken. It also
does a an import of all modules without scanning (just Venusian
attach) to time this part.

Run it multiple time to eliminate the effect of the initial compile to
``.pyc``.

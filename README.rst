git-ctm |pypi| |Wheel| |Versions| |License|
===========================================

git-ctm = ``git commit`` Time Machine

Sometimes you need to create a commit with particular timestamp.
**git-ctm** provides a command-line tool ``ctm`` for easy committing with desired timestamp:


.. code:: bash

   $ ctm -d 'Thu Feb 8 03:14:15 2018 +0200' -m 'my commit message'

   # is the same as
   $ GIT_AUTHOR_DATE='Thu Feb 8 03:14:15 2018 +0200'    \
     GIT_COMMITTER_DATE='Thu Feb 8 03:14:15 2018 +0200' \
     git commit -m 'my commit message'

*All commits in this project are done with* ``ctm`` *itself.*


Installation
------------

From `PyPI`_ using ``pip`` package manager:

.. code:: bash

    pip install --upgrade git-ctm


Or install the latest sources from GitHub:

.. code:: bash

    pip install https://github.com/pavdmyt/git-ctm/archive/master.zip


Or just put ``ctm`` `PEX`_ (Python EXecutable) file somewhere in the ``$PATH``:

.. code:: bash

    $ git clone https://github.com/pavdmyt/git-ctm.git
    $ cd git-ctm
    $ sudo cp ctm /usr/local/bin/

Now ``ctm`` command-line tool should be available to use, try:

.. code:: bash

    ctm --version


Usage
-----

.. code:: bash

    $ ctm --help
    Usage:  ctm -d <date> -m <msg>
            ctm -p

      -d <date>      Commit date and time
      -m <msg>       Commit message
      -p             Print date template

      --help         Print usage
      --version      Print version


Development
-----------

Clone the repository:

.. code:: bash

    git clone https://github.com/pavdmyt/git-ctm.git


Install dependencies:

.. code:: bash

    make install-dev


Lint code:

.. code:: bash

    make lint


Contributing
------------

1. Fork it!
2. Create your feature branch: ``git checkout -b my-new-feature``
3. Commit your changes: ``git commit -m 'Add some feature'``
4. Push to the branch: ``git push origin my-new-feature``
5. Submit a pull request
6. Make sure tests are passing


License
-------

MIT - Pavlo Dmytrenko


.. |pypi| image:: https://img.shields.io/pypi/v/git-ctm.svg
   :target: https://pypi.org/project/git-ctm/
.. |Versions| image:: https://img.shields.io/pypi/pyversions/git-ctm.svg
   :target: https://pypi.org/project/git-ctm/
.. |Wheel| image:: https://img.shields.io/pypi/wheel/git-ctm.svg
   :target: https://pypi.org/project/git-ctm/
.. |License| image:: https://img.shields.io/pypi/l/git-ctm.svg
   :target: https://pypi.org/project/git-ctm/


.. _PyPI: https://pypi.org/
.. _PEX: https://github.com/pantsbuild/pex

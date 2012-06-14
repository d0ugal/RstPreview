RstPreview - Sublime Text
=========================

This is a simple plugin for sublime text to convert RST files to HTML for
previewing and testing. The output HTML file will be loaded in your default
browser.


Installation
------------

This package relies on docutils which Sublime must be able to import. This
means that it needs to be in the site-packages of the global python install
or on the PYTHONPATH. Below are common ways to install docutils on your
system.


Mac OS X and Linux
``````````````````

Install docutils for the global python interpreter that Sublime uses::

	sudo easy_install-2.6 docutils


Windows
````````

To install docutils on windows `follow these steps in the docutils
documentation <http://docutils.sourceforge.net/README.html#installation/>`_

Usage
-----

When viewing a reStructuredText document in sublime text use the following
key combinations.

Mac OS X
`````````

`cmd ⌘` + `shift ⇧` + `r`

Linux & Windows
````````````````

`ctrl` + `shift` + `r`


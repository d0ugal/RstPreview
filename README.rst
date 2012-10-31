RstPreview - Sublime Text
=========================

This is a simple plugin for sublime text to convert RST files to HTML for
previewing and testing. The output HTML file will be loaded in your default
browser.

![Preview](http://f.cl.ly/items/26183a2u0b0M3l1u313N/Screen%20Shot%202012-10-03%20at%2014.14.37.png)


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


After the install, you may need to restart sublime text for it to be picked up.


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


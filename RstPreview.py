"""
RstPreview renders reStructuredText files as HTML and shows them in your
default browser.
"""

import sys
import os
import webbrowser
import tempfile
import hashlib

import sublime
from sublime_plugin import TextCommand
from sublime import Region

SETTINGS_FILE = 'RstPreview.sublime-settings'


def rst_to_html(rst_text):
    try:
        from docutils.core import publish_string
        bootstrap_css_path = os.path.join(sublime.packages_path(), 'RstPreview/css/bootstrap.min.css')
        base_css_path = os.path.join(sublime.packages_path(), 'RstPreview/css/base.css')
        args = {
            'stylesheet_path': ','.join([bootstrap_css_path, base_css_path]),
            'syntax_highlight': 'short'
        }
        return publish_string(rst_text, writer_name='html', settings_overrides=args)
    except ImportError:
        error_msg = """RstPreview requires docutils to be installed for the python interpreter that Sublime uses.
    run: `sudo easy_install-2.6 docutils` and restart Sublime (if on Mac OS X or Linux). For Windows check the docs at
    https://github.com/d0ugal/RstPreview"""

        sublime.error_message(error_msg)
        raise


class RstpreviewCommand(TextCommand):

    def run(self, edit):

        settings = sublime.load_settings(SETTINGS_FILE)
        site_packages_path = settings.get('site_packages_path')
        if site_packages_path and site_packages_path not in sys.path:
            sys.path.append(site_packages_path)

        # Select all the text in the current document
        text = self.view.substr(Region(0, self.view.size()))

        # Write that RST text as HTML
        html = rst_to_html(text)
        TEMP_DIR = tempfile.gettempdir()
        if self.view.file_name():
            preview_filename = hashlib.md5(self.view.file_name()).hexdigest() + ".html"
        else:
            preview_filename = 'rst_preview.html'
        file_path = os.path.join(TEMP_DIR, preview_filename)
        with open(file_path, 'w') as f:
            f.write(html)

        # Open the generated file in the default browser
        webbrowser.open('file://%s' % file_path)

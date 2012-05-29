from tempfile import NamedTemporaryFile
from webbrowser import open as show_in_browser

from sublime_plugin import TextCommand
from sublime import Region

from docutils.core import publish_string


class RstpreviewCommand(TextCommand):
    def run(self, edit):

        f = NamedTemporaryFile(delete=False)

        text = self.view.substr(Region(0, self.view.size()))

        f.write(publish_string(text, writer_name='html'))
        f.close()

        show_in_browser("file://%s" % f.name)

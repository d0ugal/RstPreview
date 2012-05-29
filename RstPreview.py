"""
RstPreview renders reStructuredText files as HTML and shows them in your
default browser.
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from webbrowser import open as open_in_browser

from sublime_plugin import TextCommand
from sublime import Region

from docutils.core import publish_string


def render_in_browser(html):
    """
    Starts a simple HTTP server, directs the browser to it and handles that
    request before closing down. This avoids the need to create many temp
    files. However, it does mean the page can't be reloaded after which is
    a little odd.
    """

    class RequestHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            """
            Write the HTML to the request file
            """
            self.wfile.write(html)

    # Start the server on a given random port
    server = HTTPServer(('127.0.0.1', 0), RequestHandler)
    # point the browser to that IP and port.
    open_in_browser('http://127.0.0.1:%s' % server.server_port)
    # handle the single request and then end.
    server.handle_request()


class RstpreviewCommand(TextCommand):

    def run(self, edit):

        # Select all the text in the current document
        text = self.view.substr(Region(0, self.view.size()))

        # Write that RST text as HTML
        html = publish_string(text, writer_name='html')

        render_in_browser(html)

# from __future__ import unicode_literals

import click
import multiprocessing

from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems

from api.cli import pass_context

def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1

class GunicornApp(BaseApplication):
    """ Custom Gunicorn application
    This allows for us to load gunicorn settings from either consul or disk.
    """
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApp, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


@click.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=8000)
@pass_context
def command(ctx, host, port):
    """Run Server"""
    ctx.log('Serving on http://%s:%s' % (host, port))

    from api.src.main import App

    # Api instances are callable WSGI apps
    app = App(ctx=ctx).api
    if host is None:
        host = ctx.config.server.host

    if port is None:
        port = ctx.config.server.port

    options = {
        'bind': '%s:%s' % (host, port),
        'workers': number_of_workers(),
        'reload': True,
    }

    GunicornApp(app, options).run()
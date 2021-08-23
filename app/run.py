# --- core python imports
from ramish_mart import app
import os
import sys
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics
# --- core python imports


VENV_ACTIVE = hasattr(sys, 'real_prefix')


def _activate():
    """ Activates virtual environment. """
    if VENV_ACTIVE:
        return None
    # construct virtual environment path.
    this = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(this, 'venv/Scripts/activate_this.py')

    # check if we can activate the virtual environment at standard location.
    if not os.path.isfile(path):
        app.log.error('[ERROR] Seems like you have not activated your virtual environment.')
        app.log.error('[ERROR] I tried to load from the standard location, but was not able to find it.')
        app.log.error('Please create a virtual environment at: {0}'.format('{0}/venv'.format(this)))
        sys.exit(1)

    # activate the virtual environment.
    exec(compile(open(path).read(), path, 'exec'), dict(__file__=path))


def _run():
    """ Imports the app and runs it. """
    from ramish_mart import app

    # provide app's version and deploy environment/config name to set a gauge metric
    register_metrics(app, app_version="v1.0", app_config="staging")

    # Plug metrics WSGI app to your main app with dispatcher
    dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

    run_simple(hostname="0.0.0.0", port=5000, application=dispatcher)

    # app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == '__main__':
    # _activate() Uncomment this if you want to execute with virtualenv and dont have docker container but before that first create it. 
    _run()

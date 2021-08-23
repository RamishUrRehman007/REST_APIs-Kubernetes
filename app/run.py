# --- core python imports
from ramish_mart import app
import os
import sys
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

    app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == '__main__':
    # _activate() Uncomment this if you want to execute with virtualenv but before that first create it. 
    _run()

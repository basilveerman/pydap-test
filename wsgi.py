import sys

from logging import basicConfig, DEBUG
from argparse import ArgumentParser

from flask import Flask
from pydap.wsgi.app import DapServer

if __name__ == '__main__':

    parser = ArgumentParser(description='Start a Pydap test server')
    parser.add_argument('-c', '--config', required=True,
        help='Pydap config file to use')
    parser.add_argument('-i', '--interface', required=True,
        help='Interface to listen on')
    parser.add_argument('-p', '--port', type=int, required=True,
        help='Indicate the port on which to bind the application')
    parser.add_argument('-t', '--threaded',
        default=False, action='store_true',
        help='Flag to specify use of Flask in threaded mode')
    args = parser.parse_args()

    basicConfig(format='%(levelname)s:%(name)s:%(asctime)s %(message)s', stream=sys.stdout, level=DEBUG)

    app = Flask(__name__)
    app.wsgi_app = DapServer(args.config)

    app.run('0.0.0.0', args.port, use_reloader=True, debug=True, use_debugger=True, threaded=args.threaded, extra_files=[args.config])

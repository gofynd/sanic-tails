#!/usr/bin/env python3.6
from argparse import ArgumentParser
from multiprocessing import cpu_count
from app import create_app

HOSTS = ('0.0.0.0', '127.0.0.1')

parser = ArgumentParser(__doc__)
parser.add_argument('--port', type=int, default=8085)
parser.add_argument('--host', choices=HOSTS, default=HOSTS[0])
parser.add_argument('--debug', type=bool, default=False)
parser.add_argument('--workers', type=int, default=cpu_count())
args = parser.parse_args()


app = create_app()
if args.debug:
    args.workers = 1
app.run(host=args.host, port=args.port, workers=args.workers, debug=args.debug)
#!/usr/bin/env python

"""
CLI Tool for creating and updating RunRules.

Usage:
    runrule.py -h | --help
    runrule.pt -v | --version
    runrule.py [--update] [--template=<PATH>] [--params=<FILE> | <params>...]

Arguments:
    <params>            Specify input parameters to be passed to the cookiecutter
                        template on the CLI.

Options:
    -h --help           Print this page.
    -v --version        Print the version.
    --update            Update mode.
    --template=<PATH>   Specify path to a cookiecutter template. The 
                        cookiecutter template may be a local folder as well 
                        as a GitHub or BitBucket repository.
    --params=<FILE>     Specify input parameters to be passed to the 
                        cookiecutter template in a JSON file.
"""

from docopt import docopt
from cookiecutter.main import cookiecutter
import json

VERSION = '0.1'
DEFAULT_NEW_TEMPLATE = './.templates/RunRule'
DEFAULT_UPDATE_TEMPLATE = './.templates/Settings'

if __name__ == '__main__':

    args = docopt(__doc__, version=VERSION)

    print args

    with open('../.context.json') as f:
        context = json.load(f)

    def_tpl = DEFAULT_NEW_TEMPLATE
    if args['--update']:
        def_tpl = DEFAULT_UPDATE_TEMPLATE

    tpl = args['--template'] or def_tpl

    if args['--params']:
        with open(args['--params']) as f:
            context.update(json.load(f))
            cookiecutter(tpl, no_input=True, extra_context=context)

    elif len(args['<params>']):
        context.update(dict(p.split('=') for p in args['<params>']))
        cookiecutter(tpl, no_input=True, extra_context=context)

    else:
        cookiecutter(tpl)

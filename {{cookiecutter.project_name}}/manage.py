#!/usr/bin/env python


"""
CLI Tool for managing MaxCompiler projects.

Usage:
    manage.py -h | --help
    manage.py -v | --version
    manage.py <runrule> [--template=<PATH>] [--params=<JSON> | <params>...]

Arguments:
    <runrule>           Specify name of the RulRule. If it does not exist, it
                        will be created. If it already exists, it will be 
                        updated.
    <params>            Specify input parameters for creating or updating
                        the RunRule as command-line arguments.

Options:
    -h --help           Print this page.
    -v --version        Print the version.
    --template=<PATH>   Specify cookiecutter template to use for creating or
                        updating the RunRule. The cookiecutter template may 
                        be a local folder or a GitHub repository.
    --params=<JSON>     Specify input parameters for creating or updating
                        the RunRule as a file argument. Currently, only JSON
                        files are accepted.
"""


from docopt import docopt

from os.path import join, abspath, dirname, realpath, isdir
from os import getcwd, chdir

from cookiecutter.main import cookiecutter
from cookiecutter.utils import work_in
from jinja2 import Environment, FileSystemLoader

import xmltodict
import json


VERSION = '0.1'

PROJECT_ROOT = dirname(realpath(__file__))

# Template paths
TEMPLATES = abspath(join(PROJECT_ROOT, '.templates'))
RUNRULE_TEMPLATE_DIR = join(TEMPLATES, 'RunRules')
RUNRULE_TEMPLATE = join(RUNRULE_TEMPLATE_DIR, 'RunRule')
SETTINGS_TEMPLATE = join(RUNRULE_TEMPLATE_DIR, 'Settings')

# Project paths
CONTEXT = join(PROJECT_ROOT, '.context.json')
RUNRULES_DIR = join(PROJECT_ROOT, 'RunRules')


if __name__ == '__main__':

    # Parse CLI
    args = docopt(__doc__, version=VERSION)

    # Load project context to get e.g. stem_name etc.
    with open(CONTEXT) as f:
        context = json.load(f)

    # Load runrule_name in the context
    context['runrule_name'] = args['<runrule>']

    # Load custom context if given
    if args['--params']:
        with open(args['--params']) as f:
            context.update(json.load(f))
    elif len(args['<params>']):
        context.update(dict(p.split('=') for p in args['<params>']))

    # Set up RunRule paths
    RUNRULE_DIR = join(RUNRULES_DIR, args['<runrule>'])

    # If the RunRule does not exist, we are creating a new one
    if not isdir(RUNRULE_DIR):

        # Set given template or default
        tpl = RUNRULE_TEMPLATE
        if args['--template']:
            tpl = abspath(args['template'])

        # Launch cookiecutter
        with work_in(RUNRULES_DIR):
            cookiecutter(tpl, no_input=True, extra_context=context)
    
    # Now that the RunRule has been created, lets bootstrap Makefile.rules
    RUNRULE_SETTINGS = join(RUNRULE_DIR, 'RunRules.settings')

    # Load up the RunRule settings    
    with open(RUNRULE_SETTINGS) as f:
        # We are going to load up the RunRules.settings XML into a dict which
        # we will pass to jinja2 as part of the context
        context.update(xmltodict.parse(f))

    # Load up the template
    loader = FileSystemLoader(searchpath=SETTINGS_TEMPLATE)
    env = Environment(loader=loader)
    tpl = env.get_template('Makefile.rules')
    
    RUNRULE_MAKE = join(RUNRULE_DIR, 'Makefile.rules')
    with open(RUNRULE_MAKE, 'wb') as f:
        f.write(tpl.render(context))


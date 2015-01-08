from subprocess import call
from cookiecutter.main import cookiecutter
from cookiecutter.utils import work_in
from os.path import dirname, realpath, join
from os import pardir
from cd import cd
import unittest


TEST = dirname(realpath(__file__))
TMP = join(TEST, 'tmp')
PROJECT = join(TMP, 'my-project')
ROOT = join(TEST, pardir)


class TestMake(unittest.TestCase):

    def setUp(self):
        """Bootstrap the project"""
        call(['mkdir', TMP])
        with work_in(TMP):
            cookiecutter(ROOT, no_input=True)

    def test_make(self):
        """Fire off make build"""
        with work_in(PROJECT):
            call(['./manage.py', 'Sim'])
            with cd(join('RunRules', 'Sim')):
                assert(call(['make', 'build']) == 0)
                
    def tearDown(self):
        """Kill the temp"""
        call(['rm', '-fr', TMP])

if __name__ == '__main__':
    unittest.main()

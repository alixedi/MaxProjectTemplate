MaxProjectTemplate
==================

This is a draft [cookiecutter](https://github.com/audreyr/cookiecutter) template for Maxeler projects.


Usage
-----

1. Install dependencies:

    $ pip install -r https://raw.githubusercontent.com/alixedi/MaxProjectTemplate/master/requirements.txt

2. Bootstrap a project:

    $ cookiecutter https://github.com/alixedi/MaxProjectTemplate

3. Create a new RunRule:

	$ cd <PROJECT_NAME>
	$ ./manage.py Simulation

4. Try compiling the project:

	$ cd RunRules/Simulation
	$ make build



Tests
-----

1. Clone repository:

	$ git clone https://github.com/alixedi/MaxProjectTemplate

	$ cd MaxProjectTemplate

2. Install dependencies:

    $ pip install -r requirements-test.txt

2. Run tests:

    $ nosetests



How to help
-----------

* If you think this is missing something, please open an issue.

* If you think you can help with some issue, please fork, modify, commit and submit a pull-request.


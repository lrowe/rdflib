#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
This test runner uses Nose for test discovery and running. It uses the argument
spec of Nose, but with some options pre-set.

See <http://code.google.com/p/python-nose/> for details.

If ``coverage.py`` is placed in $PYTHONPATH, it can be used to create coverage
information (using the built-in coverage plugin of Nose) if the default
option "--with-coverage" is supplied (which also enables some additional
coverage options).

See <http://nedbatchelder.com/code/modules/coverage.html> for details.

Note that this runner is just a convenience script. You can use ``nosetests``
directly if it's on $PATH, with the difference that you have to supply the
options pre-set here manually.
"""


NOSE_ARGS = [
        '--where=./',
        '--with-doctest',
        '--doctest-extension=.doctest',
        '--doctest-tests',
    ]

COVERAGE_EXTRA_ARGS = [
        '--cover-package=rdflib',
        '--cover-inclusive',
    ]

DEFAULT_ATTRS = ['!slowtest', '!unstable', '!non_standard_dep']

DEFAULT_DIRS = ['test', 'rdflib']


if __name__ == '__main__':

    from sys import argv, exit, stderr
    try: import nose
    except ImportError:
        print >>stderr, """\
    Requires Nose. Try:

        $ sudo easy_install nose

    Exiting. """; exit(1)


    if '--with-coverage' in argv:
        try: import coverage
        except ImportError:
            print >>stderr, "No coverage module found, skipping code coverage."
            argv.remove('--with-coverage')
        else:
            NOSE_ARGS += COVERAGE_EXTRA_ARGS


    if True not in [a.startswith('-a') or a.startswith('--attr=') for a in argv]:
        argv.append('--attr=' + ','.join(DEFAULT_ATTRS))

    if not [a for a in argv[1:] if not a.startswith('-')]:
        argv += DEFAULT_DIRS # since nose doesn't look here by default..


    finalArgs = argv + NOSE_ARGS
    print "Running nose with:", " ".join(finalArgs[1:])
    nose.run(argv=finalArgs)


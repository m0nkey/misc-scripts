#!/usr/bin/env python
"""
Generic python2.7+ (incl. py3x) command line script skeleton.
This implements most of the common stuff I put in one-off scripts
to make them actually not-so-shitty.

If you have ideas for improvements, or want the latest version, it's at:
<https://github.com/jantman/misc-scripts/blob/master/skeleton.py>

NOTE that I've converted this from using the now-deprecated optparse
module for option parsing, to the new argparse module. This was only
introduced in Python 2.7; if you need to run this on an older python,
you'll likely need to flip back to using optparse. In that case,
see <https://docs.python.org/2/library/optparse.html>.

Copyright 2014 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
Free for any use provided that patches are submitted back to me.

CHANGELOG:
2015-07-06 Jason Antman <jason@jasonantman.com>:
  - switch to module-level logger
2014-12-25 Jason Antman <jason@jasonantman.com>:
  - switch to use argparse instead of optparse
  - use class instead of module functions
  - add some more examples for those new to Python
2014-05-30 Jason Antman <jason@jasonantman.com>:
  - remove superfluous, broken line
2014-05-07 Jason Antman <jason@jasonantman.com>:
  - initial version of script
"""

import sys
import argparse
import logging

FORMAT = "[%(levelname)s %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(level=logging.ERROR, format=FORMAT)
logger = logging.getLogger(__name__)


class SimpleScript:
    """ might as well use a class. It'll make things easier later. """

    def __init__(self, dry_run=False):
        """ init method, run at class creation """
        self.dry_run = dry_run

    def run(self):
        """ do stuff here """
        logger.info("info-level log message")
        logger.debug("debug-level log message")
        logger.error("error-level log message")
        print("run.")


def parse_args(argv):
    """
    parse arguments/options

    this uses the new argparse module instead of optparse
    see: <https://docs.python.org/2/library/argparse.html>
    """
    p = argparse.ArgumentParser(description='Sample python script skeleton.')
    p.add_argument('-d', '--dry-run', dest='dry_run', action='store_true',
                   default=False,
                   help="dry-run - don't actually make any changes")
    p.add_argument('-v', '--verbose', dest='verbose', action='count', default=0,
                   help='verbose output. specify twice for debug-level output.')

    args = p.parse_args(argv)

    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if args.verbose > 1:
        logger.setLevel(logging.DEBUG)
    elif args.verbose > 0:
        logger.setLevel(logging.INFO)
    script = SimpleScript(dry_run=args.dry_run)
    script.run()

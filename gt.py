#!/usr/bin/env python3
# this is a simple python script to automate
# git pull, commit and push to github.

import shutil
import sys
import subprocess


class GitOperation:
    """
    ./gt.py "commit-msg" master/branch-name
    """

    def __init__(self, msg, branch):
        self.msg = msg
        self.branch = branch
        self._add_new_files()

    def _term_size(self):
        col, _ = shutil.get_terminal_size()
        print("-" * col)

    def _add_new_files(self):
        self._term_size()
        retcode = subprocess.call("git add .", shell=True)
        self._commit() if not retcode else sys.exit("could not add files")

    def _commit(self):
        retcode = subprocess.call('git commit -m "%s"' % self.msg, shell=True)
        self._push() if not retcode else sys.exit("could not commit")

    def _push(self):
        retcode = subprocess.call('git push origin "%s"' % self.branch, shell=True)
        if not retcode:
            print(f"Pushed to {self.branch} branch")
            self._term_size()
        else:
            sys.exit("could not push")


def main():
    if len(sys.argv) >= 2:
        msg = sys.argv[1]
        branch = sys.argv[2] if len(sys.argv) == 3 else "master"
        GitOperation(msg, branch)
    else:
        print(GitOperation.__doc__)


if __name__ == "__main__":
    main()

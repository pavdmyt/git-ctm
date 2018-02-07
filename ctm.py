# -*- coding: utf-8 -*-

import os

from docopt import docopt


CLI_SPEC = """\
Usage:  ctm -d <date> -m <msg>
        ctm -p

  -d <date>      Commit date and time
  -m <msg>       Commit message
  -p             Print date template

"""


CMD_TMPL = ("GIT_AUTHOR_DATE='{date}' "
            "GIT_COMMITTER_DATE='{date}' "
            "git commit -m '{msg}'")


DATE_TMPL = 'Wed Feb 7 11:11:11 2018 +0200'


def main():
    args = docopt(CLI_SPEC)
    date = args['-d']
    msg = args['-m']
    print_tmpl = args['-p']

    if print_tmpl:
        print(repr(DATE_TMPL))
        return

    cmd = CMD_TMPL.format(**{'date': date, 'msg': msg})
    print(cmd)
    os.system(cmd)


if __name__ == '__main__':
    main()

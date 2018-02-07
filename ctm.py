# -*- coding: utf-8 -*-

import os

from docopt import docopt


CLI_SPEC = """\
Usage:  ctm -d <date> -m <msg>

  -d <date>      Commit date and time
  -m <msg>       Commit message

"""


CMD_TMPL = ("GIT_AUTHOR_DATE='{date}' "
            "GIT_COMMITTER_DATE='{date}' "
            "git commit -m '{msg}'")


def main():
    args = docopt(CLI_SPEC)
    date = args['-d']
    msg = args['-m']

    cmd = CMD_TMPL.format(**{'date': date, 'msg': msg})
    print(cmd)
    os.system(cmd)


if __name__ == '__main__':
    main()

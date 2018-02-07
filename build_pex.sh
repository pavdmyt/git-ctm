#!/bin/bash

shebang="/usr/bin/env python"

# -r : recreate virtualenv
# -o : output file
# -c : console_script entry point
# -v : verbose
#
# --python-shebang=PYTHON_SHEBANG
#                    The exact shebang (#!...) line to add at the top of
#                    the PEX file minus the #!.  This overrides the default
#                    behavior, which picks an environment python
#                    interpreter compatible with the one used to build the
#                    PEX file.
#
# More about interpreter and shebang options:
#  https://github.com/pantsbuild/pex/issues/4
#  https://github.com/pantsbuild/pex/issues/53
#
PEX_VERBOSE=5                        \
    pex                              \
    -r requirements-pex.txt          \
    -o "ctm.pex"                     \
    -c ctm                           \
    --python-shebang="$shebang"      \
    -v

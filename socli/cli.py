# -*- coding: utf-8 -*-
"""
Systems Overview – CLI Module
=============================
The command line interface

Copyright 2021 MET Norway

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import socli
import sys
import logging
import getopt

# Initiating logging
logger = logging.getLogger(__name__)

def command(sysArgs=None):
    """Entry function for the command line client.
    """
    if sysArgs is None:
        sysArgs = sys.argv[1:]

    shortOpt = "hvi:o:"
    longOpt  = [
        "help",
        "version",
        "input=",
        "output="
    ]

    helpMsg = (
        "This is socli {version} ({date})\n"
        "{copyright}\n"
        "\n"
        "Usage:\n"
        " -h, --help     Print this message.\n"
        " -v, --version  Print program version and exit.\n"
        " -i, --input=   The input file or folder.\n"
        " -o, --output=  The output folder.\n"
    ).format(
        version   = socli.__version__,
        copyright = socli.__copyright__,
        date      = socli.__date__,
    )

    if not sysArgs:
        print(helpMsg)
        sys.exit(1)

    # Internal Variables
    inPath = None
    outPath = None

    # Parse Options
    try:
        inOpts, inRemain = getopt.getopt(sysArgs, shortOpt, longOpt)
    except getopt.GetoptError as E:
        print("ERROR: %s" % str(E))
        sys.exit(1)

    for inOpt, inArg in inOpts:
        if inOpt in ("-h", "--help"):
            print(helpMsg)
            sys.exit(0)
        elif inOpt in ("-v", "--version"):
            print(f"socli version {socli.__version__} ({socli.__date__})")
            sys.exit(0)
        elif inOpt in ("-i", "--input"):
            inPath = inArg
        elif inOpt in ("-o", "--output"):
            outPath = inArg
        else:
            print(f"ERROR: Unrecognised command line option '{inOpt}'")
            print("")
            print(helpMsg)
            sys.exit(1)

    # Validate Options
    if inPath is None:
        print("ERROR: Please specify an input file or folder")
        sys.exit(1)

    if outPath is None:
        print("ERROR: Please specify an output folder")
        sys.exit(1)

    if inPath == outPath:
        print("ERROR: Input and output cannot be the same location")
        sys.exit(1)

    return

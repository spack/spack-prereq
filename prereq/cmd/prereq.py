# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""Check for spack pre-requisites. Default will exit with error code
if any missing
"""

import argparse
import sys

import spack
import spack.cmd
import llnl.util.tty.color as color
import llnl.util.tty as tty
from spack.util.executable import which

description = "check spack pre-requisites"
section = "scripting"
level = "long"


def setup_parser(subparser):
    install_status = subparser.add_mutually_exclusive_group()
    install_status.add_argument(
        '--force-pass', dest='force_pass', default=False, action='store_true',
        help='force pass (success) if something is missing.'
    )


def prereq(parser, args):

    # Start optimistically, a return value 0 means all are installed!
    retval = 0

    # Check for present, X for missing
    missing = color.colorize("@R{[ ]}")
    present = color.colorize("@G{[X]}")

    tty.info("SPACK PRE-REQ INVENTORY")

    # Check that system requirements are included
    for cmd in ["wget", "bzip2", "tar", "python", "patch", "curl", "gzip", "xz", "zstd", "file", "git", "hg", "svn"]:
        executable = which(cmd)
        if not executable:
            print("%-20s %s" %(cmd, missing))
            if not args.force_pass:
                retval = 1
        else:
            print("%-20s %s" %(cmd, present))

    # We need at least one C/C++ compiler
    gcc = which("gcc")
    gpp = which("g++")
    clang = which("clang")
    icc = which("icc")
    
    if not any([gcc, gpp, clang, icc]):
        print("%-20s %s" %("c/c++ compiler", missing))
        if not args.force_pass:
            retval = 1
    else:
        print("%-20s %s" %("c/c++ compiler", present))

    sys.exit(retval)

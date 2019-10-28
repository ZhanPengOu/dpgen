#!/usr/bin/env python3

import os,sys,json,glob,argparse,shutil
import numpy as np
import subprocess as sp
from dpgen.tools.stat_sys import stat_sys


def run_report(args):
    report_count = 0
    if args.stat_sys:
        stat_sys(args.JOB_DIR, args.param, args.verbose)            
        report_count += 1
    # other stats added in the following

    if report_count == 0:
        print('nothing to report, rerun with -h for help')

    return report_count

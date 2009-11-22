#!/usr/bin/env
"""
Wrapper around the matlab command play_en from Dan
needs to have the matlab files + matlab installed!
"""

import os
import shutil
import sys
import string
import numpy as N
import scipy
import scipy.io

sys.path.append('../PythonSrc')
import feats_utils
import lsh


#########################################################################
# read from a process
# originally written by Douglas Eck: douglas.eck@umontreal.ca
#########################################################################
def command_with_output(cmd):
    if not type(cmd) == unicode :
        cmd = unicode(cmd,'utf-8')
    # hack just for Darwin, those lucky people
    if sys.platform=='darwin' :
        cmd = unicodedata.normalize('NFC',cmd)
    child = os.popen(cmd.encode('utf-8'))
    data = child.read()
    err = child.close()
    return data




def play_en(enid,beat,matdir) :
    """Try to call play_en matlab code from python."""

    tmpFileIn = 'dummy_playenwrapperpy_infile.mat'
    tmpFileOut = 'dummy_playenwrapperpy_outfile.mat'

    # find the right file
    matfile = feats_utils.get_matfile_from_enid(matdir, enid)

    # copy it
    shutil.copyfile(matfile,tmpFileIn)

    # save M to file
    #d = dict()
    #d['M'] = M
    #print 'm.shape:'
    #print M.shape
    #scipy.io.savemat(tmpFileIn,d)

    cmd = './run_matlab_command.sh play_en_wrapper '
    #cmd = cmd + tmpFileIn + ' ' + tmpFileOut

    # call
    result = lsh.command_with_output(cmd)

    # read file
    mfile = scipy.io.loadmat(tmpFileOut)

    return mfile['signal']


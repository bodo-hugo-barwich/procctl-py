'''
This module provides static functions to interact with `ProcessController` objects

@version: 2025-09-26

@author: Bodo Hugo Barwich
'''
__docformat__ = "restructuredtext en"

from .controller import ProcessController


def runProcess(scommandline='', options={}):
    '''
    This Method launches a process defined by `scommandline` in a separate child process

    :param scommandline: The commmand and its parameters to be executed in the child process
    :type scommandline: string
    :param options: Additional options for the execution as key - value pairs
    :type options: dictionary
    :returns: Returns a Tuple with the STDOUT, STDERR and EXIT Code
    :rtype: tuple
    '''

    arrrs = ['', '', 0]

    ctl = ProcessController(scommandline, options)

    if (ctl.Launch()):
        ctl.Wait()

    arrrs[0] = ctl.getReportString()
    arrrs[1] = ctl.getErrorString()
    arrrs[2] = ctl.getProcessStatus()

    if arrrs[2] == -1:
        arrrs[2] = ctl.getErrorCode()

    ctl.freeResources()
    ctl = None

    return arrrs


def runProcessWithOptions(commandoptions={}):
    '''
    This Method launches a process defined by `commandoptions['command']` in a separate child process
    Additional options in `commandoptions` are also configured before launching the child process

    :returns: Returns a Tuple with the STDOUT, STDERR and EXIT Code
    :rtype: tuple
    '''
    arrrs = ['', '', 0]

    if ('command' in commandoptions):
        ctl = ProcessController()

        ctl.setDictOptions(commandoptions)

        if (ctl.Launch()):
            ctl.Wait()

            arrrs[0] = ctl.getReportString()
            arrrs[1] = ctl.getErrorString()
            arrrs[2] = ctl.getProcessStatus()

            if arrrs[2] == -1:
                arrrs[2] = ctl.getErrorCode()

            ctl.freeResources()

        else:  # if(cmd.Launch())
            arrrs[2] = 1

    else:
        arrrs[0] = ''
        arrrs[1] = ''
        arrrs[2] = 3

    return arrrs

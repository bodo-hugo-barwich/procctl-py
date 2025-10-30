#!/usr/bin/python3
'''
Tests to verify the ProcessGroup Class Functionality

@version: 2025-09-26

@author: Bodo Hugo Barwich
'''
import sys
import os
import unittest
import time
#import re
#from re import IGNORECASE

sys.path.append("./")
sys.path.append("../")

from procctl import ProcessController
from procctl import ProcessGroup



class TestProcessGroup(unittest.TestCase):

  _sdirectory = ''
  _smodule = ''
  _stestscript = 'command_script.py'
  _iteststatus = 4


  def setUp(self):
    print("{} - go ...".format(sys._getframe().f_code.co_name))

    self._sdirectory = os.getcwd() + '/'
    self._stestscript = 'command_script.py'

    spath = os.path.abspath(__file__);

    slashpos = spath.rfind('/', 0)

    if slashpos != -1 :
      self._sdirectory = spath[0 : slashpos + 1]
      self._smodule = spath[slashpos + 1 : len(spath)]
    else :
      self._smodule = spath

    print("setUp - Test Directory: '{}'".format(self._sdirectory))
    print("setUp - Test Module: '{}'".format(self._smodule))
    print("")


  def tearDown(self):
    pass


  def test_ProcessGroupRun(self):
    print("{} - go ...".format(sys._getframe().f_code.co_name))

    self._stestscript = 'command_script.py'

    cmdgrp = ProcessGroup();
    imaxpause = 3

    cmd = ProcessController("{}{} {}".format(self._sdirectory, self._stestscript, 2)\
    , {'name': 'command-script:2s'})

    cmdgrp.Add(cmd)

    cmd = ProcessController("{}{} {}".format(self._sdirectory, self._stestscript, 3)\
    , {'name': 'command-script:3s'})

    cmdgrp.Add(cmd)

    cmd = ProcessController("{}{} {}".format(self._sdirectory, self._stestscript, 1)\
    , {'name': 'command-script:1s'})

    cmdgrp.Add(cmd)

    cmdcnt = cmdgrp.len

    self.assertEqual(cmdcnt, 3, "scripts (count: '{}'): were not added correctly".format(cmdcnt))

    itm = -1
    itmstrt = time.time()
    itmend = -1

    print("Process Group Execution Start - Time Now: '{}' s".format(itmstrt))

    #Execute the Processs
    bcmdrs = cmdgrp.Run()

    itmend = time.time()
    itm = (itmend - itmstrt) * 1000;

    print("Process Group Execution End - Time Now: '{}' s".format(itmend))
    print("Process Group Execution finished in '{}' ms".format(itm))

    itm = int(itmend - itmstrt)

    print("Process Group Execution Time '{} / {}' s".format(itm, imaxpause))

    print("Process Group ERROR CODE: '{}'".format(cmdgrp.code))
    print("Process Group STDOUT:\n'{}'".format(cmdgrp.report))
    print("Process Group STDERR:\n'{}'".format(cmdgrp.error))

    self.assertTrue(bcmdrs, "Process Group Execution: Execution was not correct");

    self.assertEqual(itm, imaxpause, "Process Group Execution longer than maximal Execution Time '{}' s"\
    .format(imaxpause))

    self.assertEqual(cmdgrp.code, 0, "Process Group Execution: ERROR CODE is not correct")

    for icmd in range(0, cmdcnt) :
      cmd = cmdgrp.getiCommand(icmd);

      self.assertIsNotNone(cmd, "Command No. '$iprc': Not listed correctly".format(icmd))

      if cmd is not None :
        print("Process {}:".format(cmd.getNameComplete()))

        scriptlog = cmd.report
        scripterror = cmd.error
        iscriptstatus = cmd.status

        print("ERROR CODE: '{}'".format(cmd.code))
        print("EXIT CODE: '{}'".format(iscriptstatus))

        if scriptlog is not None :
          print("STDOUT:\n'{}'".format(scriptlog))
        else :
          self.assertIsNotNone(scriptlog, "STDOUT was not captured")

        if scripterror is not None :
          print("STDERR:\n'{}'".format(scripterror))
        else :
          self.assertIsNotNone(scripterror, "STDERR was not captured")

      #if cmd is not None
    #for icmd in range(0, cmdcnt)

    print("")


  def test_ProcessGroupProfiling(self):
    print("{} - go ...".format(sys._getframe().f_code.co_name))

    self._stestscript = 'command_script.py'

    cmdgrp = ProcessGroup()
    imaxpause = 9

    cmd = ProcessController("{}{} {}".format(self._sdirectory, self._stestscript, 9)\
    , {'name': 'command-script:9s', 'profiling': True})

    self.assertTrue(cmd.profiling, 'Profiling is not activated')

    cmdgrp.Add(cmd)

    cmd = ProcessController("{}{} {}".format(self._sdirectory, self._stestscript, 3)\
    , {'name': 'command-script:3s', 'profiling': True})

    self.assertTrue(cmd.profiling, 'Profiling is not activated')

    cmdgrp.Add(cmd)

    cmd = ProcessController("{}{} {}".format(self._sdirectory, self._stestscript, 5)\
    , {'name': 'command-script:5s', 'profiling': True})

    self.assertTrue(cmd.profiling, 'Profiling is not activated')

    cmdgrp.Add(cmd)

    cmdgrp.setReadTimeout(2)

    cmdcnt = cmdgrp.len

    self.assertEqual(cmdcnt, 3, "scripts (count: '{}'): were not added correctly".format(cmdcnt))

    itm = -1
    itmstrt = time.time()
    itmend = -1

    print("Process Group Execution Start - Time Now: '{}' s".format(itmstrt))

    #Execute the Processes
    bcmdrs = cmdgrp.Run()

    itmend = time.time()
    itm = (itmend - itmstrt) * 1000;

    print("Process Group Execution End - Time Now: '{}' s".format(itmend))
    print("Process Group Execution finished in '{}' ms".format(itm))

    itm = int(itmend - itmstrt)

    print("Process Group Execution Time '{} / {}' s".format(itm, imaxpause))

    print("Process Group ERROR CODE: '{}'".format(cmdgrp.code))
    print("Process Group STDOUT:\n'{}'".format(cmdgrp.report))
    print("Process Group STDERR:\n'{}'".format(cmdgrp.error))

    self.assertTrue(bcmdrs, "Process Group Execution: Execution was not correct");

    for icmd in range(0, cmdcnt) :
      cmd = cmdgrp.getiCommand(icmd);

      self.assertIsNotNone(cmd, "Process No. '$iprc': Not listed correctly".format(icmd))

      if cmd is not None :
        print("Process {}:".format(cmd.getNameComplete()))

        scriptlog = cmd.report
        scripterror = cmd.error
        iscriptstatus = cmd.status

        print("Read Timeout: '{}'".format(cmd.read_timeout));
        print("Execution Time: '{}'".format(cmd.execution_time));

        self.assertNotEqual(cmd.read_timeout, 0, "Read Timeout was not activated")
        self.assertNotEqual(cmd.execution_time, -1, "Execution Time was not measured")

        print("ERROR CODE: '{}'".format(cmd.code))
        print("EXIT CODE: '{}'".format(iscriptstatus))

        if scriptlog is not None :
          print("STDOUT:\n'{}'".format(scriptlog))
        else :
          self.assertIsNotNone(scriptlog, "STDOUT was not captured")

        if scripterror is not None :
          print("STDERR:\n'{}'".format(scripterror))
        else :
          self.assertIsNotNone(scripterror, "STDERR was not captured")

      #if cmd is not None
    #for icmd in range(0, cmdcnt)

    print("")


  def test_ProcessGroupProfilingQuiet(self):
    print("{} - go ...".format(sys._getframe().f_code.co_name))

    self._stestscript = 'quiet_script.py'

    cmdgrp = ProcessGroup()
    imaxpause = 9

    cmd = ProcessController("{}{} {}".format(self._sdirectory, self._stestscript, 9)\
    , {'name': 'quiet-script:9s', 'profiling': True})

    self.assertTrue(cmd.profiling, 'Profiling is not activated')

    cmdgrp.Add(cmd)

    cmd = ProcessController("{}{} {}".format(self._sdirectory, self._stestscript, 3)\
    , {'name': 'quiet-script:3s', 'profiling': True})

    self.assertTrue(cmd.profiling, 'Profiling is not activated')

    cmdgrp.Add(cmd)

    cmd = ProcessController("{}{} {}".format(self._sdirectory, self._stestscript, 5)\
    , {'name': 'quiet-script:5s', 'profiling': True})

    self.assertTrue(cmd.profiling, 'Profiling is not activated')

    cmdgrp.Add(cmd)

    cmdcnt = cmdgrp.len

    self.assertEqual(cmdcnt, 3, "scripts (count: '{}'): were not added correctly".format(cmdcnt))

    cmdgrp.setCheckInterval(6)

    self.assertNotEqual(cmdgrp.setCheckInterval(6), -1, "Check Interval was not activated")

    itm = -1
    itmstrt = time.time()
    itmend = -1

    print("Process Group Execution Start - Time Now: '{}' s".format(itmstrt))

    #Execute the Processes
    bcmdrs = cmdgrp.Run()

    itmend = time.time()
    itm = (itmend - itmstrt) * 1000;

    print("Process Group Execution End - Time Now: '{}' s".format(itmend))
    print("Process Group Execution finished in '{}' ms".format(itm))

    itm = int(itmend - itmstrt)

    print("Process Group Execution Time '{} / {}' s".format(itm, imaxpause))

    print("Process Group ERROR CODE: '{}'".format(cmdgrp.code))
    print("Process Group STDOUT:\n'{}'".format(cmdgrp.report))
    print("Process Group STDERR:\n'{}'".format(cmdgrp.error))

    self.assertTrue(bcmdrs, "Process Group Execution: Execution was not correct");

    for icmd in range(0, cmdcnt) :
      cmd = cmdgrp.getiCommand(icmd);

      self.assertIsNotNone(cmd, "Process No. '$iprc': Not listed correctly".format(icmd))

      if cmd is not None :
        print("Process {}:".format(cmd.getNameComplete()))

        scriptlog = cmd.report
        scripterror = cmd.error
        iscriptstatus = cmd.status

        print("Read Timeout: '{}'".format(cmd.read_timeout));
        print("Execution Time: '{}'".format(cmd.execution_time));

        self.assertNotEqual(cmd.read_timeout, 0, "Read Timeout was not activated")
        self.assertNotEqual(cmd.execution_time, -1 , "Execution Time was not measured")

        print("ERROR CODE: '{}'".format(cmd.code))
        print("EXIT CODE: '{}'".format(iscriptstatus))

        if scriptlog is not None :
          print("STDOUT:\n'{}'".format(scriptlog))
        else :
          self.assertIsNotNone(scriptlog, "STDOUT was not captured")

        if scripterror is not None :
          print("STDERR:\n'{}'".format(scripterror))
        else :
          self.assertIsNotNone(scripterror, "STDERR was not captured")

      #if cmd is not None
    #for icmd in range(0, cmdcnt)

    print("")



if __name__ == "__main__":
  print("test module: '{}'".format(__file__))

  spath = os.path.abspath(__file__)

  print("test module absolute path: '{}'".format(spath))

  print("tests starting ...\n")
  #import sys;sys.argv = ['', 'Test.testConstructor']
  unittest.main()

  print("tests done.\n")

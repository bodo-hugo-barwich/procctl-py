[![Automated Tests](https://github.com/bodo-hugo-barwich/procctl-py/actions/workflows/python-package.yml/badge.svg)](https://github.com/bodo-hugo-barwich/pycommand/actions/workflows/python-package.yml)

# ProcessController

ProcessController - Python Package for Multiprocessing

Provides classes to launch child processes asynchronously.\
The **Object Oriented Design** allows to create groups of child processes to launch several child processes in an organized manner.

## Features
Some important Features are:
* Low Dependencies (uses only _Python_ core packages)\
  Low Dependency Usage leads to:
  	* Very High Compatibility (only _Python 3_ is required)
  	* Easy Installation
	* Small Memory Footprint (simple structure design leads to low memory usage)
	* Fast Startup (very few additional libraries to load)
* Asynchronous Launch
* Reads Big Outputs
* Execution Timeout
* Configurable Read Interval
* Captures possible System Errors at Launch Time like "file not found" Errors
* Streamlined Error Handling while still providing the Outputs

## Motivation
This Module was conceived out of the need to launch multiple tasks simultaneously while still keeping each Log and error messages and Exit Codes separately. \
As it is documented in [Python Documentation - Thread-based parallelism](https://docs.python.org/3.8/library/threading.html?highlight=thread#module-threading)
and [Python - Global Interpreter Lock](https://docs.python.org/3.8/glossary.html#term-global-interpreter-lock)
processor intensive tasks cannot run in _Python_ threads and are advised to be executed in multiple processes. \
The _Python_ implementation was derived from a prototype I developed at:
[Multi Process Manager](https://stackoverflow.com/questions/50177534/why-do-pipes-from-child-processes-break-sometimes-and-sometimes-not)\
The **Object Oriented Design** permits the implementation of the **[Command Pattern / Manager-Worker Pattern](https://en.wikipedia.org/wiki/Command_pattern)**.\
Providing a similar functionality as the [`subprocess.run()` Function](https://docs.python.org/3/library/subprocess.html#subprocess.run) it can serve as a Procedural Replacement for this function without the need of special error handling of possible Exceptions. \
This implementation aimes especially for Low Dependencies and Easy Installation.

### Example Use Case
The power of this library is best shown by an example use case as seen in the `test_CommandGroupRun()` Test:\
Having 3 Jobs at hand of 2 seconds, 3 seconds and 1 second running them sequencially would take aproximately **6 seconds**.\
But using the `CommandGroup` Class it takes effectively only **3 seconds** to complete.\
And still each job can be evaluated separately by their own results keeping log message separate from error messages and viewing them in their context.
```plain
test module absolute path: '/home/runner/work/procctl-py/procctl-py/tests/processgrouptests.py'
tests starting ...

setUp - go ...
setUp - Test Directory: '/home/runner/work/procctl-py/procctl-py/tests/'
setUp - Test Module: 'processgrouptests.py'

test_ProcessGroupProfiling - go ...
Process Group Execution Start - Time Now: '1761894376.4318516' s
Process Group Execution End - Time Now: '1761894387.4570518' s
Process Group Execution finished in '11025.200128555298' ms
Process Group Execution Time '11 / 9' s
Process Group ERROR CODE: '0'
Process Group STDOUT:
'2025-10-31 07:06:16 : Sub Process No. '0' - 'command-script:9s': Launching ...
2025-10-31 07:06:16 : Sub Process No. '0' - 'command-script:9s': Launch OK - PID (2143)
2025-10-31 07:06:16 : Sub Process No. '1' - 'command-script:3s': Launching ...
2025-10-31 07:06:16 : Sub Process No. '1' - 'command-script:3s': Launch OK - PID (2144)
2025-10-31 07:06:16 : Sub Process No. '2' - 'command-script:5s': Launching ...
2025-10-31 07:06:16 : Sub Process No. '2' - 'command-script:5s': Launch OK - PID (2145)
2025-10-31 07:06:20 : Sub Process (2144) 'command-script:3s': finished with [0]
2025-10-31 07:06:23 : Sub Process (2145) 'command-script:5s': finished with [0]
2025-10-31 07:06:27 : Sub Process (2143) 'command-script:9s': finished with [0]
'
Process Group STDERR:
''
Command (2143) 'command-script:9s':
Read Timeout: '2'
Execution Time: '9.022975206375122'
ERROR CODE: '0'
EXIT CODE: '0'
STDOUT:
'Start - Time Now: '1761894376.4508772'
Number of arguments: 2 arguments.
Argument List: ['/home/runner/work/procctl-py/procctl-py/tests/command_script.py', '9']
test script absolute path: '/home/runner/work/procctl-py/procctl-py/tests/command_script.py'
script 'command_script.py' START 0
script 'command_script.py' PAUSE '9' ...
script 'command_script.py' END 1
End - Time Now: '1761894385.4511173'
script 'command_script.py' done in '9000.240087509155' ms
script 'command_script.py' EXIT '0'
'
STDERR:
'script 'command_script.py' START 0 ERROR
script 'command_script.py' END 1 ERROR
'
Command (2144) 'command-script:3s':
Read Timeout: '2'
Execution Time: '4.0230114459991455'
ERROR CODE: '0'
EXIT CODE: '0'
STDOUT:
'Start - Time Now: '1761894376.4463177'
Number of arguments: 2 arguments.
Argument List: ['/home/runner/work/procctl-py/procctl-py/tests/command_script.py', '3']
test script absolute path: '/home/runner/work/procctl-py/procctl-py/tests/command_script.py'
script 'command_script.py' START 0
script 'command_script.py' PAUSE '3' ...
script 'command_script.py' END 1
End - Time Now: '1761894379.4465017'
script 'command_script.py' done in '3000.1840591430664' ms
script 'command_script.py' EXIT '0'
'
STDERR:
'script 'command_script.py' START 0 ERROR
script 'command_script.py' END 1 ERROR
'
Command (2145) 'command-script:5s':
Read Timeout: '2'
Execution Time: '7.020789623260498'
ERROR CODE: '0'
EXIT CODE: '0'
STDOUT:
'Start - Time Now: '1761894376.4510567'
Number of arguments: 2 arguments.
Argument List: ['/home/runner/work/procctl-py/procctl-py/tests/command_script.py', '5']
test script absolute path: '/home/runner/work/procctl-py/procctl-py/tests/command_script.py'
script 'command_script.py' START 0
script 'command_script.py' PAUSE '5' ...
script 'command_script.py' END 1
End - Time Now: '1761894381.4512694'
script 'command_script.py' done in '5000.212669372559' ms
script 'command_script.py' EXIT '0'
'
STDERR:
'script 'command_script.py' START 0 ERROR
script 'command_script.py' END 1 ERROR
----------------------------------------------------------------------
Ran 3 tests in 26.051s
```

## Usage
### runProcess() Function
The `runProcess()` Function is easy to use and straight forward.\
It is best seen in the `pytest` `test_RunProcess()` Test:\
```python
from procctl import runProcess


sdirectory = os.getcwd() + '/'
smodule = ''
stestscript = 'command_script.py'
itestpause = 3
iteststatus = 4

spath = os.path.abspath(__file__);

print("test script absolute path: '{}'".format(spath))

slashpos = spath.rfind('/', 0)

if slashpos != -1 :
  sdirectory = spath[0 : slashpos + 1]
  smodule = spath[slashpos + 1 : len(spath)]
else :
  smodule = spath

print("Test Directory: '{}'".format(sdirectory))
print("Test Module: '{}'".format(smodule))


def test_RunProcess():
    print("{} - go ...".format(sys._getframe().f_code.co_name))

    stestscript = 'command_script.py'
    itestpause = 3

    arrrs = runProcess(
        "{}{} {} {}".format(
            sdirectory,
            stestscript,
            itestpause,
            iteststatus))

    print("EXIT CODE: '{}'".format(arrrs[2]))

    assert arrrs[0] != '', "STDOUT was not captured."

    print("STDOUT: '{}'".format(arrrs[0]))

    assert arrrs[1] != '', "STDERR was not captured."

    print("STDERR: '{}'".format(arrrs[1]))

    print("")

```

The output shows how `STDOUT`, `STDERR` and **EXIT Code** are cleanly separated.\
This will produce the output:
```plain
setUp - go ...
setUp - Test Directory: '/home/runner/work/procctl-py/procctl-py/tests/'
setUp - Test Module: 'controllertests.py'

test_RunProcess - go ...
EXIT CODE: '4'
STDOUT: 'Start - Time Now: '1761894373.3652184'
Number of arguments: 3 arguments.
Argument List: ['/home/runner/work/procctl-py/procctl-py/tests/command_script.py', '3', '4']
test script absolute path: '/home/runner/work/procctl-py/procctl-py/tests/command_script.py'
script 'command_script.py' START 0
script 'command_script.py' PAUSE '3' ...
script 'command_script.py' END 1
End - Time Now: '1761894376.3653963'
script 'command_script.py' done in '3000.1778602600098' ms
script 'command_script.py' EXIT '4'
'
STDERR: 'script 'command_script.py' START 0 ERROR
script 'command_script.py' END 1 ERROR
'
```

# -*- coding: utf-8 -*-
"""
Systems Overview – Error Handler
================================
The main error handler and custom errors

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
import logging

# Initiating logging
logger = logging.getLogger(__name__)

class CLIOptionsError(Exception):
    """Raised when there is a problem with the command line input.
    """
    pass

def exceptionHandler(exType, exValue, exTrace):
    """Function to catch unhandled global exceptions.
    """
    from traceback import print_tb

    logger.critical(exType.__name__)
    logger.critical(str(exValue))

    if logger.getEffectiveLevel() <= logging.DEBUG:
        print("")
        print("Traceback")
        print("=========")
        print("")
        print_tb(exTrace)
        print("")
    else:
        print("")
        print(">>> socli exited with an error")
        print("")

    return

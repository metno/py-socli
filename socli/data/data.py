# -*- coding: utf-8 -*-
"""
Systems Overview CLI - Data Class
=================================
Class wrapping the TOML data

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

import os
import logging

from ..error import CLIOptionsError

logger = logging.getLogger(__name__)

class SOData():

    def __init__(self, srcPath):

        self.srcPath = str(srcPath)
        self.srcList = []

        # Prepare Class
        self._scanSourceData()

        return

    ##
    #  Internal Functions
    ##

    def _scanSourceData(self):
        """Scan the source path and (recursively) build a list of all
        toml files in its tree.
        """
        self.srcList = []

        if os.path.isfile(self.srcPath):
            # Input is a single file
            logger.info(f"Input file: {self.srcPath}")
            if self.srcPath.endswith(".toml"):
                self.srcList.append(self.srcPath)
                return
            else:
                raise CLIOptionsError("Input file is not a .toml file.")

        elif os.path.isdir(self.srcPath):
            # Input is a directory
            logger.info(f"Input folder: {self.srcPath}")

        else:
            # Input path is not valid
            raise FileNotFoundError(f"Input path is not valid: {self.srcPath}")

        return

# END Class SOData

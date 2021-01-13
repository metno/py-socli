# -*- coding: utf-8 -*-
"""Systems Overview CLI

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

import sys
import logging

__copyright__ = "Copyright 2021, MET Norway"
__license__   = "Apache 2"
__version__   = "0.0.1"
__date__      = "2021-01-01"

# Initiating logging
logger = logging.getLogger(__name__)

def main(sysArgs=None):
    """Entry function for the command line client.
    """
    if sysArgs is None:
        sysArgs = sys.argv

    return

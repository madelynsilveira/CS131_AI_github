#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

from enum import Enum

# Definition of some common types
EnvironmentKeyType = str
NodeIdType = int

# Possible results of an evaluation
class ResultEnum(Enum):
    UNDEFINED = 0
    FAILED = 1
    RUNNING = 2
    SUCCEEDED = 3

# State information keys
ADDITIONAL_INFORMATION = "additional_information"
NODE_RESULT = "result"
RUNNING_CHILD = "running_child"

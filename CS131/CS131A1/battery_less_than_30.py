#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from bt_library.tree_node import TreeNode
from globals import BATTERY_LEVEL


# conditional battery check
class BatteryLessThan30(btl.Condition):
    """
    Implementation of the condition "battery_level < 30".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking battery < 30")

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(BATTERY_LEVEL, 0) < 30 \
            else self.report_failed(blackboard)


    

#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
# Nothing Module
#

import bt_library as btl

class DoNothing(btl.Task):
    """
    Implementation of the Task "Do Nothing".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Doing nothing")

        return self.report_succeeded(blackboard)
    
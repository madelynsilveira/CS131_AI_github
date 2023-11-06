#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
#
# Version 1.0.2 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from globals import HOME_PATH, BATTERY_LEVEL


class FindHome(btl.Task):
    """
    Implementation of the Task "Find Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Looking for a home")

        blackboard.set_in_environment(HOME_PATH, "Up Left Left Up Right")

        return self.report_succeeded(blackboard)


class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Going to my home")

        blackboard.get_in_environment(HOME_PATH, "Up Left Up Right")

        return self.report_succeeded(blackboard)
    

class Dock(btl.Task):
    """
    Implementation of the Task "Dock".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Docking")
        
        blackboard.set_in_environment(BATTERY_LEVEL, 100)

        return self.report_succeeded(blackboard)
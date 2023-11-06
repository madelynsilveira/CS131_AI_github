#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
# General Cleaning Module
#

import random
import bt_library as btl
from globals import GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR


class General(btl.Condition):
    """
    Implementation of the condition "general".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking for general cleaning")

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(GENERAL_CLEANING, False) == True \
            else self.report_failed(blackboard)


class DustySpot(btl.Condition):
    """
    Implementation of the condition "dusty spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking for dusty spots")

        # simulation of the dusty spot sensor: 17% dusty
        sensor = random.randint(0, 100)

        if sensor % 2 == 0 and sensor % 3 == 0:
            blackboard.set_in_environment(DUSTY_SPOT_SENSOR, True)
            blackboard.set_in_environment(SPOT_CLEANING, True)

        # succeeded if dusty, failed otherwise
        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(DUSTY_SPOT_SENSOR, False) \
            else self.report_failed(blackboard)
    
    
class CleanFloor(btl.Task): # Repeats until failure
    """
    Implementation of the Task "Clean Floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning the floor")

        # simulation of the dusty spot sensor: 6% dusty
        sensor = random.randint(0, 100)

        if sensor % 15 == 0:
            blackboard.set_in_environment(GENERAL_CLEANING, False)
            blackboard.set_in_environment(SPOT_CLEANING, False)
            return self.report_failed(blackboard)

        return self.report_running(blackboard)

class DoneGeneral(btl.Task):
    """
    Implementation of the Task "Done General".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Done with general cleaning")

        blackboard.set_in_environment(GENERAL_CLEANING, False)

        return self.report_succeeded(blackboard)


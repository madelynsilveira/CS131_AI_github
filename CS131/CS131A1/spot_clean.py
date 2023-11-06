#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS131 - Artificial Intelligence
# Spot Cleaning Module
#

import random
import bt_library as btl
from globals import SPOT_CLEANING, DUSTY_SPOT_SENSOR


class Spot(btl.Condition):
    """
    Implementation of the condition "spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking for a spot")

        # simulation of spot sensor: 10% dusty
        sensor = random.randint(0, 100)

        if sensor % 2 == 0 and sensor % 5 == 0:
            blackboard.set_in_environment(SPOT_CLEANING, True)

        # if spot_cleaning is true, succeeded, otherwise failed
        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(SPOT_CLEANING, False) \
            else self.report_failed(blackboard)


class CleanSpot(btl.Task):
    """
    Implementation of the Task "Clean Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning the spot!")

        # timer will report succeeded when done
        return self.report_running(blackboard)
        


class DoneSpot(btl.Task):
    """
    Implementation of the Task "Done Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Done with the spot")

        blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
        blackboard.set_in_environment(SPOT_CLEANING, False)

        return self.report_succeeded(blackboard)


#!/usr/bin/env python

""" Main driver module.

Main driver module for the robot simulator. Acts as a façade to hide most of
the underlying complexity of the simulator itself.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Mario Cobos Maestre"
__authors__ = ["Mario Cobos Maestre"]
__contact__ = "mario.cobos@edu.uah.es"
__copyright__ = "Copyright 2019, UAH"
__credits__ = ["Mario Cobos Maestre"]
__date__ = "2019/03/18"
__deprecated__ = False
__email__ =  "mario.cobos@edu.uah.es"
__license__ = "GPLv3"
__maintainer__ = "Mario Cobos Maestre"
__status__ = "Development"
__version__ = "1.0.0b"


import argparse
from simulation import Simulation

class R2P2():
    scenario = '../config/scenario-default.json'

    def __init__(self) -> None:
        """
            Initialize the R2P2 program and sets it ready to run a simulation
        """
        # Initialize the parser
        self.__parser_init()
        # Load atributes
        self.__update__dict()
        # Load simulation
        self.__load_simulation()


    def __parser_init(self):
        """
            Creates the ArgumentParser to parse console arguments when running the program
        """
        # Parser initial conf
        prog = 'python r2p2.py'
        description = 'Run a simulation using a specified scenario.'
        epilog = 'Any extra argument passed through the CLI will be ignored'
        allow_abbrev = False
        formatter_class = argparse.RawDescriptionHelpFormatter

        # Parser initialization
        self.parser = argparse.ArgumentParser(prog=prog, description=description, epilog=epilog,
            allow_abbrev=allow_abbrev, formatter_class=formatter_class)

        # Adding possible arguments
        self.parser.add_argument('-V', '--version', action='version', version=__version__,
            help='Displays the current version of the simulator and exit')

        self.parser.add_argument('--scenario', metavar='S', nargs='?',
            help='Path to the configuration JSON in which the scenario is defined')


    def __update__dict(self):
        """
            Updates the object __dict__ with the parameters got from the CLI parsing
        """
        global DEFAULT
        # Get default atribute values
        self.__dict__.update(DEFAULT)
        # Delete DEFAULT to save memory. We are no longer needing it
        del DEFAULT
        # Parse CLI args
        args, unknown = self.parser.parse_known_args()
        # Get CLI atribute values if any
        self.__dict__.update(args.__dict__)

    def __load_simulation(self):
        """
            Creates a simulation and sets it ready for its execution
        """
        self.simulation = Simulation()

    def run_simulation(self):
        """
            Runs the simulation
        """
        self.simulation.run()







if __name__ == '__main__':

    # Create the main R2P2 class
    r2p2 = R2P2()
    r2p2.hola

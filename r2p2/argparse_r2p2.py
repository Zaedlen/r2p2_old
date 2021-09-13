import argparse
from r2p2 import __version__

class R2P2ArgumentParser(argparse.ArgumentParser):
    def __init__(self) -> None:
        """
            Constructor with custom parameters for the r2p2 program
        """

        prog = 'python r2p2.py'
        description = 'Run a simulation using a specified scenario.'
        epilog = 'Any extra argument passed through the CLI will be used to overwrite scenario parameters.\nDo not enter spaces in the values or add quotes!\nEx: --start [20,10] --goal "[21, 11]"'
        allow_abbrev = False
        formatter_class = argparse.RawDescriptionHelpFormatter

        super().__init__(prog=prog, description=description, epilog=epilog, allow_abbrev=allow_abbrev, formatter_class=formatter_class)

        self.add_argument('-V', '--version', action='version', version=__version__, help='Displays the current version of the simulator and exit')
    # parser.add_argument('--scenario', metavar='S', nargs='?',\
    #     help='Path to the configuration JSON in which the scenario is defined.')
    # parser.add_argument('--controller', metavar='C', nargs='?',\
    #     help='Path to the controller that you want to use. This will override the scenario one if there was any.')
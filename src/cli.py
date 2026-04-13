import argparse
from pathlib import Path


class HelpFormatter(argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass

parser = argparse.ArgumentParser(
    formatter_class=HelpFormatter,
    description="A command-line tool to process and rearrange stored boxes " \
                "based on movement instructions. Supports specifying input " \
                "instruction sets and selecting different heavy lifters " \
                "for flexible automation and analysis."
)

parser.add_argument(
    '-is',
    '--instruction-set',
    required=True,
    type=Path,
    metavar='\b',
    help="Instruction set absolute file path"
)

parser.add_argument(
    '-hl',
    '--heavy-lifter',
    required=True,
    type=str,
    choices=['v1'],
    help="The version of the heavy lifter to use"
)

args = parser.parse_args()


if not args.instruction_set.exists():
    parser.error("The specified file path does not exist. Please provide a valid one.")

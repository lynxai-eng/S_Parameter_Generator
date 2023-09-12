import argparse
import sys

from generator import sparm_gen

ver = float(sys.version.split(' ')[0][:3])
if ver < 3.9 :
    print('LynxAI application requires Python 3.9 or higher release')
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sparam", help="")

args = parser.parse_args()
sparm= args.sparam
sparm_gen(sparm)
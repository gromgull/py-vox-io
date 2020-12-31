import sys
import argparse
import logging
import coloredlogs
from pyvox.parser import VoxParser
from pyvox.writer import VoxWriter

log = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')

parser = argparse.ArgumentParser(description='Testing roundtrip for vox saving and parsing')
parser.add_argument("voxfilename", help="VOX model filename")
args = parser.parse_args()

log.info("Reading vox file: " + args.voxfilename)

m1 = VoxParser(args.voxfilename).parse()

log.info("File read; writing to test.vox")

VoxWriter('test.vox', m1).write()

log.info("Reading vox file: test.vox")

m2 = VoxParser('test.vox').parse()


if (m1.models == m2.models):
	log.info("Round trip: SUCCESS")
else:
	log.error("Round trip: FAILURE, models do not match")

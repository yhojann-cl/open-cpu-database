#!/usr/bin/env python3
import sys
import pprint
import argparse

sys.path.append('../src')
from cpu import find_cpu_by_name
from cpu import find_cpu_by_codename

# Parse arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--name')
group.add_argument('--codename')
args = parser.parse_args()

# Call CPURepository methods
if args.name:
	try:
		cpu = find_cpu_by_name(args.name)
	except StopIteration:
		print(f"'{args.name}' not found in database.")
	else:
		print(f"'{args.name}' found in database:")
		pprint.pprint(cpu)

elif args.codename:
	try:
		cpu = find_cpu_by_codename(args.codename)
	except StopIteration:
		print(f"'{args.codename}' not found in database.")
	else:
		print(f"'{args.codename}' found in database:")
		pprint.pprint(cpu)

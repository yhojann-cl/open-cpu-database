#!/usr/bin/env python3
import sys
import argparse

sys.path.append('../../database/python')
from cpu import CPURepository

# Parse arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--name')
group.add_argument('--codename')
args = parser.parse_args()

# Call CPURepository methods
if args.name:
	try:
		cpu = CPURepository.findByName(args.name)
	except StopIteration:
		print(f"'{args.name}' not found in database.")
	else:
		print(f"'{args.name}' found in database:\n{cpu}")
elif args.codename:
	try:
		cpu = CPURepository.findByCodename(args.codename)
	except StopIteration:
		print(f"'{args.codename}' not found in database.")
	else:
		print(f"'{args.codename}' found in database:\n{cpu}")

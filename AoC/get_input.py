#!/usr/bin/python3
import argparse
import subprocess
from contextlib import redirect_stdout
import sys

# import requests

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.
SESSION = '53616c7465645f5f73b82f49629d888a0085a89711dd400aa3a2d90c516489c24c2d5a73caf4742607141d76e2dfb055ec3d99fd0a3c72f136aa8404507e58d1'
path = "C:\\Users\\Arun\\Documents\\Arun\\dbrx_instruct\\DSA\\AoC\\2023\\input.txt"
useragent = 'ArunCSK'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2023)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A \'{useragent}\''
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)
with open(f'./{args.year}/input.txt', 'w') as f:
    with redirect_stdout(f):
        print(output)



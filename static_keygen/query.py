import random
import json
import sys
import os

def prechecks():
	if os.getuid() != 0:
		sys.exit("PermissionError: Insufficient Permissions")
	if len(sys.argv) < 2:
		sys.exit("python3 keygen.py [keyfile]")

prechecks()

def GET():
	file=sys.argv[1]
	content=json.loads(open(file, "r").read())
	ran=random.choice(list(content.keys()))
	print(f"{ran} :: {content[ran]}")

GET()
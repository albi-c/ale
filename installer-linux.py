#!/usr/bin/python3

import os
import shutil

scriptdir = os.path.dirname(os.path.realpath(__file__))
home = os.path.expanduser("~")

print("Installing ALE...")

shutil.copy(os.path.join(scriptdir, "main.py"), os.path.join(home, "bin", "ale"))
os.chmod(os.path.join(home, "bin", "ale"), 0o755)

print("Installed!")

print("\nUse \"ale\" command in terminal")

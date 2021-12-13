#!/usr/bin/env python3.8
import subprocess
import sys

#Setting the Packages names
vulners_package = "vulners"
nmap_package = "python-nmap"
mitre_package = "pyattck"
report_package = "reportlab==3.5.59"
visualization_package = "networkx==2.5"
math_package = "matplotlib"

# vulners install 
subprocess.check_call([sys.executable, "-m", "pip", "install", vulners_package])

# nmap install 
subprocess.check_call([sys.executable, "-m", "pip", "install", nmap_package])

# mitre install 
subprocess.check_call([sys.executable, "-m", "pip", "install", mitre_package])

# report install 
subprocess.check_call([sys.executable, "-m", "pip", "install", report_package])

# visualization install 
subprocess.check_call([sys.executable, "-m", "pip", "install", visualization_package])

# math install 
subprocess.check_call([sys.executable, "-m", "pip", "install", math_package])

print("------Done------")

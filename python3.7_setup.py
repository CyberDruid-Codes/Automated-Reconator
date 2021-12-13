#!/usr/bin/env python3.7
import subprocess
import sys

#Setting the Packages names
nltk_package = "nltk"
numpy_package = "numpy"
tensorflow_package = "tensorflow"


# vulners install 
subprocess.check_call([sys.executable, "-m", "pip", "install", nltk_package])

# nmap install 
subprocess.check_call([sys.executable, "-m", "pip", "install", numpy_package])

# mitre install 
subprocess.check_call([sys.executable, "-m", "pip", "install", tensorflow_package])

print("------Done------")

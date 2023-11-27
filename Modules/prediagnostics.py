from __future__ import print_function
import os
import re
import shutil
import sys
import subprocess

""""
try:
    import requests
except ImportError as ie:  # pragma: no cover
    print("ERROR:\tMissing Python module 'requests'.")
    print("\tPlease install this module and rerun rescueme")
    sys.exit(1)
    """
def get_distro():
    """
    Return the running Linux distribution.

    Returns:
        distro (str): the detected Linux distribution
    """

    distro = "unknown"
    rhel_regex = re.compile(r"^Red Hat Enterprise Linux*")
    
    if os.path.isfile("/etc/rhel-release"):
        with open("/etc/rhel-release", "r") as fp:
            # This file is a single line
            distro_str = fp.readline()
            if re.match(rhel_regex, distro_str) or re.match(r"^CentOS.*release (\d+)\.(\d+)", distro_str):
                distro = distro_str
       
    return distro
def list_network_drivers():
    try:
        network_drivers = subprocess.check_output(['lsmod']).decode('utf-8')
        return f"Network Drivers:\n{network_drivers}"
    except Exception as e:
        return f"Unable to list network drivers: {str(e)}"

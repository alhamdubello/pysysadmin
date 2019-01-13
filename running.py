#!/usr/bin/env python3.6

import os

from os import getenv
#stage = os.environ["STAGE"].upper()
stage = getenv("STAGE", default="dev").upper()

output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!!! - " + output
print(output)

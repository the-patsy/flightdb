#!/bin/bash/

# Setup script. If this fails you likely don't have postgresql installed. Tested on Linux Mint.

sudo apt update
sudo apt install python3 python3-pip postgresql libpq-dev git
git clone https://github.com/openskynetwork/opensky-api.git
pip install psycopg2
pip install datetime
pip install -e ./opensky-api/python/

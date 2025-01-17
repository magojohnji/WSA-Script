#!/usr/bin/python3
#
# This file is part of MagiskOnWSALocal.
#
# MagiskOnWSALocal is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# MagiskOnWSALocal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with MagiskOnWSALocal.  If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (C) 2023 LSPosed Contributors
#

import sys

import json
import requests
from pathlib import Path

#Android header
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36',
}

magisk_branch = sys.argv[1]
magisk_ver = sys.argv[2]
download_dir = Path.cwd().parent / "download" if sys.argv[2] == "" else Path(sys.argv[3])
tempScript = sys.argv[4]
print(f"Generating Magisk download link: branch={magisk_branch}, release type={magisk_ver}", flush=True)
if not magisk_branch:
    magisk_branch = "topjohnwu"
if not magisk_ver:
    magisk_ver = "stable"
if magisk_branch = "topjohnwu":
    try:
        magisk_link = json.loads(requests.get(
            f"https://github.com/{magisk_branch}/magisk-files/raw/master/{magisk_ver}.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/{magisk_branch}/magisk-files@master/{magisk_ver}.json").content)['magisk']['link']
if magisk_branch = "HuskyDG":
    try:magisk_link = json.loads(requests.get(
        f"https://github.com/HuskyDG/magisk-files/blob/main/canary.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/HuskyDG/magisk-files@main/canary.json").content)['magisk']['link']
if magisk_branch = "HuskyDG Lite"
    try:
        magisk_link = json.loads(requests.get(
            f"https://github.com/HuskyDG/magisk-files/blob/main/canary_lite.json").content)['magisk']['link']
    except Exception:
        print("Failed to fetch from GitHub API, fallbacking to jsdelivr...")
        magisk_link = json.loads(requests.get(
            f"https://fastly.jsdelivr.net/gh/HuskyDG/magisk-files@main/canary_lite.json").content)['magisk']['link']
if magisk_branch = "vvb2060":
    try:
        magisk_link = json.loads(requests.get(
            f"https://install.appcenter.ms/api/v0.1/apps/vvb2060/magisk/distribution_groups/public/releases/latest?is_install_page=true", headers=headers).content)['download_url']
    except Exception:
        print("Failed to fetch from AppCenter API...")
print(f"download link: {magisk_link}", flush=True)

with open(download_dir/tempScript, 'a') as f:
    f.writelines(f'{magisk_link}\n')
    f.writelines(f'  dir={download_dir}\n')
    f.writelines(f'  out=magisk-{magisk_ver}.zip\n')

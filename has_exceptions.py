#!/usr/bin/env python

# This is an example of using smeagle to parse over libraries in spack (to
# see if they have exceptions). We will be:

# 0. Adding smeagle to the path (in the smeagle development container)
# 1. Getting access to a bunch of spack binaries
# 2. For each package, downloading, and running smeagle

# The goal of this exercise to see what percentage of default packages in spack
# have exceptions (out of the possible ones that could). I noticed that libtcl
# did not have any, and found this very surprising!

# docker run -v $PWD:/code -v /home/vanessa/Desktop/Code/spack:/spack -it smeagle bash
# Add Smeagle and spack to the path
# export PATH=/code/build/standalone/:$PATH

import tempfile
from boto3 import client
import os
import shutil
import json
import subprocess

# Dump all binaries here for now
outdir = tempfile.mkdtemp()
results = {}

# assumes credentials exported in environment
conn = client("s3")
for key in conn.list_objects(Bucket="sandbox-cache")["Contents"]:

    if not key["Key"].endswith(".spack"):
        continue

    outfile = os.path.join(outdir, key["Key"])
    out_dir = os.path.dirname(outfile)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    print("Downloading %s" % key["Key"])
    with open(outfile, "wb") as f:
        conn.download_fileobj("sandbox-cache", key["Key"], f)

    # Extract it
    os.system("tar -xvf %s -C %s" % (outfile, out_dir))

    # Get all extracted files
    for name in os.listdir(out_dir):
        if name.endswith(".tar.gz"):
            os.system("tar -xf %s/%s -C %s" % (out_dir, name, out_dir))

    for name in os.listdir(out_dir):
        fullpath = os.path.join(out_dir, name)
        if os.path.isdir(fullpath):
            bins = os.path.join(fullpath, "bin")
            libs = os.path.join(fullpath, "lib")

            binaries = []
            if os.path.exists(bins):
                for binary in os.listdir(bins):
                    binaries.append(os.path.join(bins, binary))
            if os.path.exists(libs):
                for lib in os.listdir(libs):
                    if lib.endswith(".so"):
                        binaries.append(os.path.join(libs, lib))

            for binary in binaries:
                try:
                    res = subprocess.Popen(
                        ["Smeagle", "-l", binary, "--has-exceptions"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                    )
                    output = res.communicate()
                    results[binary] = (
                        output[0]
                        .decode("utf-8")
                        .strip()
                        .split(":")[-1]
                        .strip()
                        .replace(".", "")
                    )
                except:
                    pass

    # Clean up and save as we go
    shutil.rmtree(out_dir)
    with open("exception-counts.json", "w") as fd:
        fd.write(json.dumps(results, indent=4))

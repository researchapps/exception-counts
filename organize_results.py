#!/usr/bin/env python
import json
import os

with open("exception-counts.json", "r") as fd:
    data = json.loads(fd.read())

# Create re-structured (organized) results
results = {}
seen = set()

for key, result in data.items():
    package, dirname, binary = key.split(os.sep)[-3:]

    if not result.strip():
        continue
    if package not in results:
        results[package] = {}
    count = int(result.replace('exceptions', '').strip())
    if count != 0 and binary not in seen:
        print("%s %s has %s exceptions" %(package, binary, count))
    seen.add(binary)
    results[package][binary] = count

with open("exception-counts-processed.json", 'w') as fd:
    fd.write(json.dumps(results, indent=4))


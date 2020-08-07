import json
import sys

if len(sys.argv) < 3:
    print("You need to give at least two Squad like filenames to join them togeether!")
    exit()

file_names = sys.argv[1:]
jsons = []

try:
    for f in file_names:
        jsons.append(json.load(open(f)))
except:
    print(f"Could not load JSON file {f}")

if len(jsons) < 2:
    print("Could not read more than one Squad file. Try again.")
    exit()

pivot_json = jsons.pop(0)

for j in jsons:
    pivot_json["data"].extend(j["data"])

combined_name = "+".join([f[:-4][:5] for f in file_names])
json.dump(pivot_json, open(f"{combined_name}.json", "w"))
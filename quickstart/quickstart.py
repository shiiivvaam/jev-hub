"""Sends request.json to Jev and prints the answer. No dependencies.
Needs your own TypeSafe API key: export TYPESAFE_API_KEY=..."""
import json, os, urllib.request

body = open(os.path.join(os.path.dirname(__file__), "request.json"), "rb").read()
req = urllib.request.Request(
    "https://api.typesafe.ai/v1/systemone",
    data=body,
    headers={"Authorization": "Bearer " + os.environ["TYPESAFE_API_KEY"], "Content-Type": "application/json"},
)
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))

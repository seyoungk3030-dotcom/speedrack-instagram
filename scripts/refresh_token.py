"""Refresh the long-lived Instagram token (valid 60 days) and print the new one."""
import json, os, urllib.parse, urllib.request

q = urllib.parse.urlencode({"grant_type": "ig_refresh_token", "access_token": os.environ["IG_ACCESS_TOKEN"]})
with urllib.request.urlopen(f"https://graph.instagram.com/refresh_access_token?{q}", timeout=60) as r:
    data = json.load(r)
print(data["access_token"])

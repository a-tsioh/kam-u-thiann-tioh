import os, importlib, string

settings = importlib.import_module("server.settings.default")

for v in dir(settings):
  if v.startswith("__"): continue
  globals()[v] = getattr(settings, v)

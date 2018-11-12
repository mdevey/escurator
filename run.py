from elasticsearch import Elasticsearch
from subprocess import run

print("Running /run.py")
run(["python", "--version"])
print("")
print("curator --help\n")
run(["/curator/curator", "--help"])
print("curator_cli --help\n")
print("")
run(["/curator/curator_cli", "--help"])
print("")
print("Volume mount another file, -v $(PWD)/script.py:/run.py")



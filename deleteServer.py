import requests
import json 

environmentFile = open('env.json')
envs = json.load(environmentFile)
token = envs["ARVANTOKEN"]
datacenter = envs["DATACENTER"]
datacenters = {"b":"ir-thr-w1", "f":"ir-thr-c2","sh":"ir-tbz-dc1"}
get_servers = requests.get(
                f"https://napi.arvancloud.ir/ecc/v1/regions/{datacenters[datacenter]}/servers",
                headers={
                    "Accept":"application/json",
                    "Authorization":token
                })
servers = json.loads(get_servers.text)
for server in servers["data"]:
    id = server["id"]
    if id != "6e2e4001-5caf-402f-a025-6a1b18e96531" and id != "6d9c9855-7d0a-4dc7-a08c-3d378bbe0f84":
        deletedServer = requests.delete(f"https://napi.arvancloud.ir/ecc/v1/regions/{datacenters[datacenter]}/servers/{id}?forceDelete={True}",headers={
                        "Accept":"application/json",
                        "Authorization":token
                    })
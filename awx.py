import requests
import json

def add_host(token, datacenter, servers, inventoryId, awxHost, awxUser, awxPass):
    datacenters = {"b":"ir-thr-w1", "f":"ir-thr-c2","sh":"ir-tbz-dc1"}
    for server in servers:
        s = requests.get(
            f"https://napi.arvancloud.ir/ecc/v1/regions/{datacenters[datacenter]}/servers/{server}",
            headers={
                "Accept":"application/json",
                "Authorization":token
            }
        )
        serverDetail = json.loads(s.text)["data"]
        ip = serverDetail["addresses"][list(serverDetail['addresses'].keys())[0]][0]["addr"]
        hostData= {
            "name": ip,
            "description": "",
            "inventory": inventoryId,
            "enabled": True,
            "instance_id": "",
            "variables": ""
        }
        response = requests.post(
            f"http://{awxUser}:{awxPass}@{awxHost}/api/v2/hosts/", json=hostData, 
            headers={"Content-Type": "application/json;charset=UTF-8", "Accept":"application/json, text/plain, */*"}
        )
        print("Host added to ")
        print(response)


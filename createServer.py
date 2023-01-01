import requests
import random
import string
import os

def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def bamdad(n, serverOs, token):
    for i in range(n):
        if serverOs == "w":
            serverData = {
                "name": f"windows-ba-{id_generator()}",
                "count": 1,
                "network_ids": [
                    "33c37a96-8cdc-4f93-93ea-baf80b09de5a"
                ],
                "flavor_id": "g2-16-6-0",
                "image_id": "2002abd3-96e4-48a5-b2a5-9fbd7689f74f",
                "security_groups": [
                    {
                        "name": "a2f773b2-4f64-4e73-ad7c-0d5022f6c431"
                    }
                ],
                "ssh_key": False,
                "key_name": 0,
                "disk_size": 45,
                "init_script": "",
                "ha_enabled": True,
                "server_volumes": []
            }
        else:
            serverData = {
                "name": f"ubuntu-ba-{id_generator()}",
                "count": 1,
                "network_ids": [
                    "e9e69b5c-0a0a-4f72-a2d6-55cb81ae6912"
                ],
                "flavor_id": "g3-16-8-0",
                "image_id": "0a937fc8-ba42-4529-baf8-fbf94dbfdf56",
                "security_groups": [
                    {
                        "name": "a2f773b2-4f64-4e73-ad7c-0d5022f6c431"
                    }
                ],
                "ssh_key": True,
                "key_name": "AsaKey",
                "disk_size": 25,
                "init_script": "",
                "ha_enabled": True,
                "server_volumes": []
            }
        createServer = requests.pserverOst(
                        "https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-w1/servers",json=serverData,
                        headers={
                            "Accept":"application/json",
                            "Authorization":token
                        })
        print(f"server number {n} Created")
        print(createServer)
        n += 1

def foroogh(n, token):
    for i in range(n):
        if serverOs == "w":
            serverData = {
                "name": f"windows-fr-{id_generator()}",
                "count": 1,
                "network_ids": [
                    "ffc8dbf2-bdc1-4d9a-b64c-d0951d70d6a6"
                ],
                "flavor_id": "g1-16-6-0",
                "image_id": "c594929f-3592-4402-9605-4ebe92ebc35a",
                "security_groups": [
                    {
                        "name": "5a063eb4-1ce4-4e68-bd54-9e442f1aab86"
                    }
                ],
                "ssh_key": False,
                "key_name": 0,
                "disk_size": 45,
                "init_script": "",
                "ha_enabled": True,
                "server_volumes": []
            }
        createServer = requests.pserverOst(
                        "https://napi.arvancloud.ir/ecc/v1/regions/ir-thr-c2/servers",json=serverData,
                        headers={
                            "Accept":"application/json",
                            "Authorization":token
                        })
        print(f"server number {n} Created")
        print(createServer)
        n += 1


def shahriar(n, serverOs, token):
    for i in range(n):
        if serverOs == "w":
            serverData = {
                "name": f"windows-fr-{id_generator()}",
                "count": 1,
                "network_ids": [
                    "ffc8dbf2-bdc1-4d9a-b64c-d0951d70d6a6"
                ],
                "flavor_id": "g1-16-6-0",
                "image_id": "c594929f-3592-4402-9605-4ebe92ebc35a",
                "security_groups": [
                    {
                        "name": "5a063eb4-1ce4-4e68-bd54-9e442f1aab86"
                    }
                ],
                "ssh_key": False,
                "key_name": 0,
                "disk_size": 45,
                "init_script": "",
                "ha_enabled": True,
                "server_volumes": []
            }
        else:
            serverData = {
                "name": f"ubuntu-sh-{id_generator()}",
                "count": 1,
                "network_ids": [
                    "2a0c41fd-8fb4-48df-910d-62998783680d"
                ],
                "flavor_id": "g2-32-8-0",
                "image_id": "56331629-97ad-4460-910e-a95ebc35fe24",
                "security_groups": [
                    {
                    "name": "31ad35f7-9029-4fb5-a3c7-b89e81e33ac0"
                    }
                ],
                "ssh_key": True,
                "key_name": "AsaKey",
                "disk_size": 25,
                "init_script": "",
                "ha_enabled": True,
                "server_volumes": []
            }
        createServer = requests.pserverOst(
                        "https://napi.arvancloud.ir/ecc/v1/regions/ir-tbz-dc1/servers",json=serverData,
                        headers={
                            "Accept":"application/json",
                            "Authorization":token
                        })
        print(f"server number {n} Created")
        print(createServer)
        n += 1

token = os.environ["ARVANTOKEN"]
n = os.environ['SERVERCOUNT']
datacenter = os.environ['DATACENTER']
serverOs = os.environ['SERVEROS']
if datacenter == "b":
    bamdad(n,serverOs, token)
elif datacenter == "f":
    foroogh(n, token)
elif datacenter == "sh": 
    shahriar(n,serverOs, token)
import requests
import json
import urllib3

class ProxmoxAPI:
    def __init__(self, configData):
        # Initialize base URL and headers for Proxmox API
        self.baseUrl = configData["proxmox"]["baseURL"]
        self.headers = {
            'Authorization': f'PVEAPIToken={configData["proxmox"]["tokenID"]}={configData["proxmox"]["tokenSecret"]}'
        }
        # Disable SSL warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @classmethod
    def fromConfig(cls, configPath='config.json'):
        # Load configuration data from config file
        with open(configPath, 'r') as file:
            configData = json.load(file)
        return cls(configData)

    def getNodeStatus(self, node):
        # Construct the URL for fetching node status
        url = f"{self.baseUrl}/api2/json/nodes/{node}/status"
        response = requests.get(url, headers=self.headers, verify=False)
        if response.status_code == 200:
            data = response.json()['data']
            uptime = data.get("uptime", 0)
            status = "online" if uptime >= 1 else data.get("status", "Unknown")

            # Temporary debug line
            # print(json.dumps(data, indent=4))


            # TODO: Add customizability
            # Issue URL: https://github.com/goldentg/APIFetch/issues/1

            # Construct node status dictionary with relevant information
            nodeStatus = {
                "name": node,
                "status": status,
                "cpuUtil": float(data.get("cpu", 0)) * 100,  # Convert to percentage
                "memUtil": (data["memory"]["used"] / data["memory"]["total"]) * 100,  # Convert to percentage
                "diskUtil": (data.get("rootfs", {}).get("used", 0) / data.get("rootfs", {}).get("total", 1)) * 100,
                # Convert to percentage
                "loadAvg": [float(x) for x in data.get("loadavg", [0, 0, 0])],  # Convert to float
                "uptime": data.get("uptime", 0),
                "currentKernel": data.get("current-kernel", {}).get("version", "Unknown"),
                "netUpSpeed": data.get("netin", 0),  # Network up speed
                "netDownSpeed": data.get("netout", 0)  # Network down speed
            }
            return nodeStatus
        else:
            response.raise_for_status()

    def listNodes(self):
        # Construct the URL for listing nodes
        url = f"{self.baseUrl}/api2/json/nodes"
        response = requests.get(url, headers=self.headers, verify=False)
        if response.status_code == 200:
            return response.json()['data']
        else:
            response.raise_for_status()
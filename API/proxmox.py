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
                "currentKernel": data.get("current-kernel", {}).get("version", "Unknown")
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

    def getFormattedNodeStatus(self):
        nodes = self.listNodes()
        if nodes:
            nodeName = nodes[0]['node']  # Use the first node name from the list
            nodeStatus = self.getNodeStatus(nodeName)

            # Extracting relevant information with fallback values
            cpuUtilPercentage = float(nodeStatus.get('cpuUtil', 0))  # Ensure it's a float
            memUtilPercentage = nodeStatus.get("memUtil", 0)
            diskUtilPercentage = nodeStatus.get("diskUtil", 0)
            status = "online" if nodeStatus.get('uptime', 0) >= 1 else nodeStatus.get('status', 'Unknown')
            kernel = nodeStatus.get("currentKernel", "Unknown")

            loadAvg = nodeStatus.get('loadAvg', ['N/A', 'N/A', 'N/A'])
            loadAvgStr = ', '.join(map(str, loadAvg))

            uptimeSeconds = nodeStatus.get('uptime', 0)
            uptimeHours = uptimeSeconds // 3600

            # Constructing content for Proxmox panel
            proxmoxContent = (
                f"Node Name: {nodeName}\n"
                f"Status: {status}\n"
                f"CPU Utilization: {cpuUtilPercentage:.2f}%\n"
                f"Memory Utilization: {memUtilPercentage:.2f}%\n"
                f"Disk Utilization: {diskUtilPercentage:.2f}%\n"
                f"Load Average: {loadAvgStr}\n"
                f"Uptime: {uptimeHours} hours\n"
                f"Kernel Version: {kernel}"
            )
        else:
            proxmoxContent = "No nodes available in Proxmox."
        return proxmoxContent
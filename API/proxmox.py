import requests
import json
import urllib3

class ProxmoxAPI:
    def __init__(self, config_data):
        # Initialize base URL and headers for Proxmox API
        self.base_url = config_data["proxmox"]["baseURL"]
        self.headers = {
            'Authorization': f'PVEAPIToken={config_data["proxmox"]["tokenID"]}={config_data["proxmox"]["tokenSecret"]}'
        }
        # Disable SSL warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @classmethod
    def from_config(cls, config_path='config.json'):
        # Load configuration data from config file
        with open(config_path, 'r') as file:
            config_data = json.load(file)
        return cls(config_data)

    def get_node_status(self, node):
        # Construct the URL for fetching node status
        url = f"{self.base_url}/api2/json/nodes/{node}/status"
        response = requests.get(url, headers=self.headers, verify=False)
        if response.status_code == 200:
            data = response.json()['data']
            uptime = data.get("uptime", 0)
            status = "online" if uptime >= 1 else data.get("status", "Unknown")

            # Construct node status dictionary with relevant information
            # TODO: Add customizability
            # Issue URL: https://github.com/goldentg/APIFetch/issues/1

            node_status = {
                "name": node,
                "status": status,
                "cpu_util": data.get("cpu") * 100 if data.get("cpu") is not None else None,  # Convert to percentage
                "mem_util": (data.get("memory", {}).get("used") / data.get("memory", {}).get(
                    "total")) * 100 if data.get("memory", {}).get("used") is not None and data.get("memory", {}).get(
                    "total") is not None else None,  # Convert to percentage
                "disk_util": (data.get("rootfs", {}).get("used") / data.get("rootfs", {}).get(
                    "total")) * 100 if data.get("rootfs", {}).get("used") is not None and data.get("rootfs", {}).get(
                    "total") is not None else None,  # Convert to percentage
                "loadavg": data.get("loadavg", ['N/A', 'N/A', 'N/A']),
                "uptime": data.get("uptime"),
                "current-kernel": data.get("current-kernel", {}).get("version", "Unknown")
            }
            return node_status
        else:
            response.raise_for_status()

    def list_nodes(self):
        # Construct the URL for listing nodes
        url = f"{self.base_url}/api2/json/nodes"
        response = requests.get(url, headers=self.headers, verify=False)
        if response.status_code == 200:
            return response.json()['data']
        else:
            response.raise_for_status()
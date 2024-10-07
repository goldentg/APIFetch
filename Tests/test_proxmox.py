# test_proxmox.py
import pytest
from unittest.mock import patch, Mock
from API.proxmox import ProxmoxAPI

@pytest.fixture
def proxmox_api():
    config_data = {
        "proxmox": {
            "baseURL": "https://proxmox.example.com:8006",
            "tokenID": "test-token-id",
            "tokenSecret": "test-token-secret"
        }
    }
    return ProxmoxAPI(config_data)

@patch('API.proxmox.requests.get')
def test_getNodeStatus(mock_get, proxmox_api):
    # Mock the API response for getNodeStatus
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {
            "uptime": 3600,
            "cpu": 0.1,
            "memory": {"used": 1024, "total": 2048},
            "rootfs": {"used": 512, "total": 1024},
            "loadavg": [0.1, 0.2, 0.3],
            "current-kernel": {"version": "5.4.0-42-generic"}
        }
    }
    mock_get.return_value = mock_response

    # Call the method
    node_status = proxmox_api.getNodeStatus("test-node")

    # Assertions
    assert node_status["status"] == "online"
    assert node_status["cpuUtil"] == 10.0
    assert node_status["memUtil"] == 50.0
    assert node_status["diskUtil"] == 50.0
    assert node_status["loadAvg"] == [0.1, 0.2, 0.3]
    assert node_status["currentKernel"] == "5.4.0-42-generic"

@patch('API.proxmox.requests.get')
def test_listNodes(mock_get, proxmox_api):
    # Mock the API response for listNodes
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": [
            {"node": "node1"},
            {"node": "node2"}
        ]
    }
    mock_get.return_value = mock_response

    # Call the method
    nodes = proxmox_api.listNodes()

    # Assertions
    assert len(nodes) == 2
    assert nodes[0]["node"] == "node1"
    assert nodes[1]["node"] == "node2"
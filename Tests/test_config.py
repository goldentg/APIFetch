import pytest
import json
from Main import config, panels

def test_load_config():
    assert isinstance(config, dict), "Config should be a dictionary"

def test_panels_not_empty():
    assert len(panels) > 0, "Panels should not be empty"

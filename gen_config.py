import os
import sys
import yaml

config = {
    'name': 'pydap-test',
    'version': 0,
    'api_version': 0,
    'ensemble': 'test_ensemble',
    'root_url': 'root_url',
    'handlers': [{
        'url': os.path.basename(filename.strip()),
        'file': filename.strip()
    } for filename in sys.stdin]
}

with open('pydap_config.yaml', 'w') as f:
    yaml.dump(config, f)

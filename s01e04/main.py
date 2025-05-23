from common.requests.centrala_client import CentralaClient
from common.config import CENTRALA_KEY

if __name__ == "__main__":
    centrala = CentralaClient()

    headers = {
        "Accept": "text/plain"
    }

    fragile_data = centrala.get(['data', CENTRALA_KEY, 'cenzura.txt'], headers=headers).text
    print(fragile_data)
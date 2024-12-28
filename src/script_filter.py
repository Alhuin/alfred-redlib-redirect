import sys
import json
from utils import get_instances, NetworkError


def _get_formatted_results(usernames):
    return [
        {
            "title": username,
            "arg": username,
            "icon": {"path": "./icon.svg"},
        }
        for username in usernames
    ]


def _get_formatted_error(error):
    return [
        {
            "title": f"NetworkError: {error}",
            "valid": False,
            "icon": {"path": "./icon.svg"},
        }
    ]


if __name__ == "__main__":
    try:
        results = get_instances()
        alfred_json = json.dumps({"items": _get_formatted_results(results)}, indent=2)
    except NetworkError as e:
        alfred_json = json.dumps({"items": _get_formatted_error(e)}, indent=2)

    sys.stdout.write(alfred_json)
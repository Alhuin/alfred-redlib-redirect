import requests


class NetworkError(Exception):
    pass

# import re
# from bs4 import BeautifulSoup


# def get_robot_url():
#     url = "https://github.com/redlib-org/redlib-instances"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     link = soup.find('a', attrs={'href': re.compile("^https:\/\/stats\.uptimerobot\.com")})
#     return link["href"]


def get_instances():
    url = "https://stats.uptimerobot.com/api/getMonitorList/mpmqAs1G2Q"
    response = requests.get(url)

    if response.status_code == 200:
        instances = response.json()
        instances_by_30d_ratio = {
            f'https://{monitor["name"]}': {
                "status": monitor["statusClass"],
                "30dRatio": float(monitor['30dRatio']['ratio']),
            }
            for monitor in instances['psp']['monitors']
        }

        return dict(sorted(
            instances_by_30d_ratio.items(),
            key=lambda item: (item[1]["status"] == "success", item[1]["30dRatio"]),
            reverse=True
        ))
    else:
        raise NetworkError("Could not connect to the UptimeRobot, please try again later")


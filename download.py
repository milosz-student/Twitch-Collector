import json
import os
from datetime import datetime
import requests
from tqdm import tqdm

from download_cfg import *


def download_from_link(link, streamer, game_name):
    response = requests.get(link, stream=True)
    if response.status_code != 200:
        print(f"Niepoprawny status odpowiedzi dla {link} {streamer} {game_name}")
    else:
        date_today = datetime.now().strftime("%d_%m_%y")
        time_now = datetime.now().strftime("%H_%M_%S")
        total_length = int(response.headers.get("content-length", 0))
        if not os.path.exists(f"{PATH_OUTPUT_VIDEOS}/{date_today}"):
            os.mkdir(f"{PATH_OUTPUT_VIDEOS}/{date_today}")

        if not os.path.exists(f"{PATH_OUTPUT_VIDEOS}/{date_today}/{streamer}"):
            os.mkdir(f"{PATH_OUTPUT_VIDEOS}/{date_today}/{streamer}")

        with open(
            f"{PATH_OUTPUT_VIDEOS}/{date_today}/{streamer}/{time_now}.txt", "w"
        ) as f1:
            f1.write(streamer + "\n")
            f1.write(game_name + "\n")

        if total_length:
            with open(
                f"{PATH_OUTPUT_VIDEOS}/{date_today}/{streamer}/{time_now}.mp4", "wb"
            ) as f:
                for chunk in tqdm(
                    response.iter_content(chunk_size=4096),
                    total=total_length // 4096,
                    unit="KB",
                ):
                    if chunk:
                        f.write(chunk)

        print(f"Download complete = {link}")


class TwitchCollector:
    def __init__(self):
        self.time = TIME
        self.streamers_names = []

    def load_streamers(self):
        with open(PATH_STREAMERS_LIST, "r") as f:
            self.streamers_names = [s_name.strip() for s_name in f]

    def download_from_streamers(self):
        for streamer in self.streamers_names:

            data = f'{{"operationName":"ClipsCards__User","variables":{{"login": "{streamer}","limit":{LIMIT_PER_STREAMER},"criteria":{{"filter":"{self.time}"}}}},"extensions":{{"persistedQuery":{{"version":1,"sha256Hash":"b73ad2bfaecfd30a9e6c28fada15bd97032c83ec77a0440766a56fe0bd632777"}}}}}}'

            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()  # to raise HTTPError for bad status codes (>=400)
            if response.status_code != 200:
                print(f"Niepoprawny status odpowiedzi dla {streamer}")
            else:

                data = response.json()
                with open(PATH_RESPONSE, "w", encoding="utf-8") as f:
                    json.dump(data, f)

                save_links = [
                    edge["node"]["thumbnailURL"].split("-preview")[0] + ".mp4"
                    for edge in data["data"]["user"]["clips"]["edges"]
                ]

                for link in save_links:
                    download_from_link(link, streamer, GAME)

    def download_from_game(self):
        response = requests.post(url, headers=headers, json=json_data)
        if response.status_code != 200:
            print(f"Niepoprawny status odpowiedzi dla {GAME}")
        else:
            data = response.json()
            with open(PATH_RESPONSE, "w", encoding="utf-8") as f:
                json.dump(data, f)

            save_links = [
                edge["node"]["thumbnailURL"].split("-preview")[0] + ".mp4"
                for edge in data[3]["data"]["game"]["clips"]["edges"]
            ]
            author_links = [
                edge["node"]["broadcaster"]["login"]
                for edge in data[3]["data"]["game"]["clips"]["edges"]
            ]
            game_name = [
                edge["node"]["game"]["name"]
                for edge in data[3]["data"]["game"]["clips"]["edges"]
            ]

            for i in range(len(save_links)):
                download_from_link(save_links[i], author_links[i], game_name[i])


asd = TwitchCollector()
asd.load_streamers()
asd.download_from_streamers()
asd.download_from_game()

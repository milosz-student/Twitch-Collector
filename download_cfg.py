PATH_STREAMERS_LIST = "../streamers/choosen_list.txt"
PATH_OUTPUT_VIDEOS = "../videos"
PATH_RESPONSE = "../response.json"
LIMIT_PER_STREAMER = 5
LIMIT_PER_GAME = 10
TIME = "LAST_MONTH"  # LAST_DAY LAST_WEEK LAST_MONTH ALL_TIME
GAME = "League of Legends"


url = "https://gql.twitch.tv/gql"
headers = {
    "Host": "gql.twitch.tv",
    "Sec-Ch-Ua": '"Not A(Brand";v="24", "Chromium";v="110"',
    "Accept-Language": "pl-PL",
    "Client-Version": "8244571e-a43a-4b3b-bd82-94b1af88cf6c",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36",
    "Content-Type": "text/plain;charset=UTF-8",
    "Client-Session-Id": "2c5be3742cc2f649",
    "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
    "X-Device-Id": "ypfRZaJlU8MvC03esXIqvOeQwrYTMpjG",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept": "/",
    "Origin": "https://www.twitch.tv",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.twitch.tv/",
}
json_data = [
    {
        "operationName": "Directory_DirectoryBanner",
        "variables": {"name": "League of Legends"},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "2670fbecd8fbea0211c56528d6eff5752ef9d6c73cd5238d395784b46335ded4",
            }
        },
    },
    {
        "operationName": "DirectoryRoot_Directory",
        "variables": {"name": "league of legends"},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "9f4f6ae67f21ee50b454fcf048691107a52bfe7907ead73b9427398e343ca319",
            }
        },
    },
    {
        "operationName": "PersonalSections",
        "variables": {
            "input": {
                "sectionInputs": ["RECOMMENDED_SECTION"],
                "recommendationContext": {
                    "platform": "web",
                    "clientApp": "twilight",
                    "location": "clips_game",
                    "referrerDomain": "",
                    "viewportHeight": 942,
                    "viewportWidth": 929,
                    "channelName": "None",
                    "categoryName": "league of legends",
                    "lastChannelName": "None",
                    "lastCategoryName": "league of legends",
                    "pageviewContent": "None",
                    "pageviewContentType": "None",
                    "pageviewLocation": "clips_game",
                    "pageviewMedium": "None",
                    "previousPageviewContent": "None",
                    "previousPageviewContentType": "None",
                    "previousPageviewLocation": "None",
                    "previousPageviewMedium": "None",
                },
            },
            "creatorAnniversariesExperimentEnabled": False,
            "sideNavActiveGiftExperimentEnabled": False,
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "469b047f12eef51d67d3007b7c908cf002c674825969b4fa1c71c7e4d7f1bbfb",
            }
        },
    },
    {
        "operationName": "ClipsCards__Game",
        "variables": {
            "gameName": "League of Legends",
            "limit": LIMIT_PER_GAME,
            "criteria": {"filter": "LAST_DAY"},
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "0d8d0eba9fc7ef77de54a7d933998e21ad7a1274c867ec565ac14ffdce77b1f9",
            }
        },
    },
]

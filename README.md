# Twitch-Collector
 TwitchCollector is an application that allows download of materials from Twitch. It allows you to download materials from a specific streamer or from a selected category.

How you initialize class.
```python
asd = TwitchCollector()
```
This will load streamers list from .txt file declared in config file.
```python
asd.load_streamers()
```
We can download from streamers
```python
asd.download_from_streamers()
```
or from specifc game
```python
asd.download_from_game()
```
In addition you need change some values in download_cfg.py
I hidden my ID to not cause any trouble :P
You can easily get them by using BURP or something.
```python
headers = {
    "Host": "gql.twitch.tv",
    "Sec-Ch-Ua": '"Not A(Brand";v="24", "Chromium";v="110"',
    "Accept-Language": "pl-PL",
    "Client-Version": "XXXXXXXXXXXXXXXXXXXXXXX",
    "User-Agent": "Mozilla/5.0 ",
    "Content-Type": "text/plain;charset=UTF-8",
    "Client-Session-Id": "XXXXXXXXXXXXXXXXXXXXXXX",
    "Client-Id": "XXXXXXXXXXXXXXXXXXXXXXX",
    "X-Device-Id": "XXXXXXXXXXXXXXXXXXXXXXX",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept": "/",
    "Origin": "https://www.twitch.tv",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.twitch.tv/",
}
```


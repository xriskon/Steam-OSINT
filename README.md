# Steam-OSINT

![GitHub last commit](https://img.shields.io/github/last-commit/xriskon/Steam-OSINT) ![GitHub repo size](https://img.shields.io/github/repo-size/xriskon/Steam-OSINT) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/xriskon/Steam-OSINT?color=orange) ![GitHub](https://img.shields.io/github/license/xriskon/Steam-OSINT)

An OSINT tool based on Steam API

![](D:\Projects\Python\Steam-OSINT\.images\banner.svg)

Disclaimer: **FOR EDUCATIONAL PURPOSE ONLY! The contributors do not assume any responsibility for the use of this tool.**

## Usage

Run the script through a terminal/command line with `python3 main.py USERNAME`, where USERNAME is the target's Custom URL or SteamID64.

**Arguments**

id            			username (required)

-o, --output		enables output to file

## Command List

```
[target]	change target user
[info]		get target's info
[friends]	get friends list
[games]		get owned games
```

## Installation

- Create a directory and name it "config" and inside it create "key.txt" and put your Steam API key in it.

Alternatively run the following commands:

- `mkdir config`

- `cd config`

- `echo API_KEY > key.txt`

Where API_KEY is your own key.

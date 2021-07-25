# Steam OSINT

<p align="center">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/xriskon/Steam-OSINT">
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/xriskon/Steam-OSINT">
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/xriskon/Steam-OSINT?color=orange">
<img alt="GitHub" src="https://img.shields.io/github/license/xriskon/Steam-OSINT">
</p>

<p align="center">
<img align="center" src=".images/banner.png">
</p>

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

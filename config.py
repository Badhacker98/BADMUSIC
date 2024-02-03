import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID"))

#Put your bot username here
BOT_USERNAME = getenv("New_Music_Test_Bot")

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/MXNIHACKER/PbxMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Team_Hunter_X")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", None )

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



#  ██████╗░███████╗██╗░░░██╗██╗██╗░░░░░
#  ██╔══██╗██╔════╝██║░░░██║██║██║░░░░░
#  ██║░░██║█████╗░░╚██╗░██╔╝██║██║░░░░░
#  ██║░░██║██╔══╝░░░╚████╔╝░██║██║░░░░░
#  ██████╔╝███████╗░░╚██╔╝░░██║███████╗
#  ╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚══════╝

#                   ██╗░░██╗
#                   ╚██╗██╔╝
#                   ░╚███╔╝░
#                   ░██╔██╗░
#                   ██╔╝╚██╗
#                   ╚═╝░░╚═╝

#  ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░
#  ████╗░████║██║░░░██║██╔════╝██║██╔══██╗
#  ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝
#  ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗
#  ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝
#  ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░




BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/958f6eea876a36437e879.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/c1dda633c676eb3a9b8a0.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/40513bcf8a1a5c92e0a9c.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

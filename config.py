import os
import aiohttp
from Python_ARQ import ARQ
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Oashu Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/f5305458102a5094996f7.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/85ab03ab419b0b658c5e1.png")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/1d75a8fa2f1e6bc5d3278.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "OashuMusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "oashumusic_assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "OashuSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Oashu_Channel")
OWNER_NAME = getenv("OWNER_NAME", "dwpryga") # isi dengan username kamu tanpa simbol @
ALIVE_EMOJI = getenv("ALIVE_EMOJI", "⚡")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/yogaadtma/OashuMusic")
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

aiohttpsession = aiohttp.ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)

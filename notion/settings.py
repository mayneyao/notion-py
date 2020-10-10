import os
from pathlib import Path

BASE_URL = "https://www.notion.so/"
API_BASE_URL = BASE_URL + "api/v3/"
SIGNED_URL_PREFIX = "https://www.notion.so/signed/"
S3_URL_PREFIX = "https://s3-us-west-2.amazonaws.com/secure.notion-static.com/"
S3_URL_PREFIX_ENCODED = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/"
DATA_DIR = os.environ.get("NOTION_DATA_DIR", str(Path(os.path.expanduser("~")).joinpath(".notion-py")))
CACHE_DIR = str(Path(DATA_DIR).joinpath("cache"))
LOG_FILE = str(Path(DATA_DIR).joinpath("notion.log"))

DO_NOT_MAKE_DIR = os.environ.get("DO_NOT_MAKE_DIR", False)

if not DO_NOT_MAKE_DIR:
	try:
		if  log_level != "disabled":
			os.makedirs(DATA_DIR)
	except FileExistsError:
		pass

	try:
		if  log_level != "disabled":
			os.makedirs(CACHE_DIR)
	except FileExistsError:
		pass

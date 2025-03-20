import dotenv
dotenv.load_dotenv()

import os
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

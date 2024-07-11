import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22349624"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "47b2f281e462d5cd3d832957f02911ad")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sainiankit17201:HLFQk3Ww9V2z3pTA@cluster0.jmjoo0d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

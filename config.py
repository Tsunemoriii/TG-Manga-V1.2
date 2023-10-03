API_ID = "25697264"
API_HASH = "fc1bce8441f3c90b719bc86098137a3d"
BOT_TOKEN = "5179913360:AAFwC8igG3hhcWNclnmDxntS-rdJFK9iCTI"
CHANNEL = "Sonic_Otakus"
DATABASE_URL_PRIMARY = "postgres://nmudsxqm:rNHvqk6zK4C9SftNfxIzFpE9ReuHEg5c@peanut.db.elephantsql.com/nmudsxqm"

if DATABASE_URL_PRIMARY.startswith('postgres://'):
    DATABASE_URL_PRIMARY = DATABASE_URL_PRIMARY.replace('postgres://', 'postgresql://', 1)

REQ_CHANNEL = "https://t.me/+UYVBj-9UFzYyZDQ9"        # channel link for requests
REQ_CHANNEL_ID = -1001912478564     # channel id
FORCE_CHANNEL = "https://t.me/Sonic_Otakus"      # channel link for force sub
FORCE_CHANNEL_ID = -1001514116490   # channel id

DB_URL = "mongodb+srv://utahakane003:utahakane003@cluster0.xyoubmt.mongodb.net/?retryWrites=true&w=majority"     # database url
DB_NAME = "MangaReqDB"    # database name


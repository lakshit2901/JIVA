from ROBOT.sample_config import Config


class Development(Config):
    OWNER_ID =  927708047 # my telegram ID
    OWNER_USERNAME = "Goku"  # my telegram username
    API_KEY = "1393696282:AAFJBBBroyOhrISfH0FN6c6qoVXziBmOASU"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = "postgres://xeywggvo:6adtLhos4J0nqZdRpiJlwcrOXhSkE_Al@kashin.db.elephantsql.com:5432/xeywggvo"  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = False
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = []
    TELETHON_HASH = "a9cff900e67dfac6df95320120526d42" # for purge stuffs
    TELETHON_ID = 658724
from ROBOT.sample_config import Config


class Development(Config):
    OWNER_ID = 1663038733 # my telegram ID
    OWNER_USERNAME = "Florals_crown"  # my telegram username
    API_KEY = "1615763754:AAGh-MSNn86sL4DwfsJuaHkoD4-jz57uIYQ"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = "postgres://aguifliw:HkQsU9p6bGklhl4-XS32a5_BVpUZrs1L@queenie.db.elephantsql.com:5432/aguifliw"  # sample db credentials
    MESSAGE_DUMP = '-1001424495148' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = False
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = []
    TELETHON_HASH = "9c0a2ec452bd926590d12a5817466bf1" # for purge stuffs
    TELETHON_ID = 4444607
    SPAMWATCH = "2~VfIItjiGlgERR8tNfUXqGi4EkzTzF5ZV8X_7fBkL_~4HIU4nQpZ~LdabOY~KCd"

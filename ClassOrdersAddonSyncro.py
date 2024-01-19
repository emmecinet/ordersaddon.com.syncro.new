#general class
import configparser
import this

class OrdersAddonSyncro:

    def get_configuration():
        config = configparser.ConfigParser()
        config.read(['_config.ini'])
        #config.get("general", "general_test")
        #config.sections()
        return config


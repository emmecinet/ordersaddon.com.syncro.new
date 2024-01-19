#general class
import configparser

class OrdersAddonSyncro_:

    def get_configuration():
        config = configparser.ConfigParser()
        config.read(['_config.ini'])
        #config.get("general", "general_test")
        #config.sections()
        return config


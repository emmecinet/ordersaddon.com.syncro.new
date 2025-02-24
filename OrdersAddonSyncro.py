#general class
import configparser
import this

class OrdersAddonSyncro:

    #this.config_path = 'C:/Zucchetti.Ordersaddon.UDDistribuzione.2.0/'
    #this.config_path = 'C:/Zucchetti.Ordersaddon.Curafarma.2.0/'
    #this.config_path = 'C:/Zucchetti/uddistribuzione/'
    
    def get_configuration():
        config_general = configparser.ConfigParser()
        config_general.read('_config.general.ini')
        app_path = config_general.get("general", "app_path")
        #print(app_path)
        
        config = configparser.ConfigParser()
        config.read(app_path + '_config.user.ini')
        #config.get("general", "general_test")
        #config.sections()
        return config


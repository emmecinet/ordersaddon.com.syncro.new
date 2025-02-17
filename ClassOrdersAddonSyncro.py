#general class
import configparser
import this

class OrdersAddonSyncro:

    #this.config_path = 'C:/Zucchetti.Ordersaddon.UDDistribuzione.2.0/'
    #this.config_path = 'C:/Zucchetti.Ordersaddon.Curafarma.2.0/'
    #this.config_path = 'C:/Zucchetti/uddistribuzione/'

    def get_configuration_general():
        config_general = configparser.ConfigParser().read('_config.general.ini')
        #config_general = config_general.get("general", "app_path")
        return config_general
    
    def get_configuration():
        app_path = OrdersAddonSyncro.get_configuration_general().get("general", "app_path")
        
        config = configparser.ConfigParser()
        config.read(app_path + '_config.ini')
        #config.get("general", "general_test")
        #config.sections()
        return config


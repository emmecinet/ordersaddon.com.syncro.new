#general class
import configparser
import this

class OrdersAddonSyncro:

    this.config_path = 'C:/Zucchetti.Ordersaddon.UDDistribuzione.2.0/'
    #this.config_path = 'C:/Zucchetti.Ordersaddon.Curafarma.2.0/'
    #this.config_path = 'C:/Zucchetti/uddistribuzione/'

    def get_configuration_path():
        return this.config_path
    
    def get_configuration():

        config = configparser.ConfigParser()
        config.read(this.config_path + '_config.ini')
        #config.get("general", "general_test")
        #config.sections()
        return config


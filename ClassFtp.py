import ftplib
from ClassOrdersAddonSyncro import OrdersAddonSyncro as oa
class Ftp:
    
    ftp_host = oa.get_configuration().get('ftp','ftp_server')
    ftp_user = oa.get_configuration().get('ftp','ftp_user')
    ftp_pass = oa.get_configuration().get('ftp','ftp_pass')
    
    #def __init__(self):
    #    self.ftp_host = ""

    def upload(localfile,remotefile):
        ftp = ftplib.FTP(Ftp.ftp_host)
        ftp.login(Ftp.ftp_user,Ftp.ftp_pass)
        
        with open(localfile,"rb") as file:
            ftp.storbinary('STOR %s' % remotefile, file)
import ftplib
from OrdersAddonSyncro import OrdersAddonSyncro

class Ftp:
    
    def __init__(self):
        self.ftp_host = ''
        
    def upload(localfile,remotefile,ftp_server,ftp_user,ftp_pass):

        ftp = ftplib.FTP(ftp_server)
        ftp.login(ftp_user,ftp_pass)
        
        with open(localfile,"rb") as file:
            ftp.storbinary('STOR %s' % remotefile, file)

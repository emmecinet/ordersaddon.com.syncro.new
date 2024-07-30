import ftplib
from ClassOrdersAddonSyncro import OrdersAddonSyncro as oa

class CustomUdFtp:
    
    ftp_host = 'ftp.uddistribuzione.it'
    ftp_user = 'ordersaddon@uddistribuzione.it'
    ftp_pass = '$yt~1@&c*d65'
    
    def upload(localfile,remotefile):
        ftp = ftplib.FTP(CustomUdFtp.ftp_host)
        ftp.login(CustomUdFtp.ftp_user,CustomUdFtp.ftp_pass)
        
        with open(localfile,"rb") as file:
            ftp.storbinary('STOR %s' % remotefile, file)
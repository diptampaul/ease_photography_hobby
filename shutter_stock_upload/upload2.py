import ftplib
import os

def transfer_zip(filename, host, host_path, user, password):
    with ftplib.FTP_TLS(host, timeout=180) as ftp:
        ftp.login(user, password)
        ftp.prot_p()  # Use explicit FTP over TLS
        # ftp.set_pasv(False)
        print(ftp.getwelcome())
        ftp.dir()
        with open(filename, 'rb') as file:
            print(file)
            print(f"STOR {os.path.basename(filename)}")
            ftp.storbinary(f"STOR {os.path.basename(filename)}", file)
        ftp.close()

transfer_zip("Gangasagar-24.jpg", "ftps.shutterstock.com", "", "diptampaul13@gmail.com", "FyyR1234@#$")
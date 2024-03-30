from ftplib import FTP_TLS, FTP
import os

# FTP credentials and server details
ftp_host = 'ftps.shutterstock.com'
ftp_username = 'diptampaul13@gmail.com'
ftp_password = 'FyyR1234@#4321'

# Path to the directory containing the files to upload
local_directory = '/path/to/your/local/directory'

# Connect to the FTP server
ftp = FTP_TLS(ftp_host)
print("login")
ftp.login(user=ftp_username, passwd=ftp_password)
print(ftp)

# Change to the desired directory on the FTP server
# ftp.cwd('upload')  # Change 'upload' to the appropriate directory

# Function to upload a file
def upload_file(filename):
    with open(filename, 'rb') as file:
        print(f"uploading {filename}")
        ftp.storbinary('STOR ' + os.path.basename(filename), file, 20000)

# Iterate over files in the local directory and upload them
# for filename in os.listdir(local_directory):
#     if os.path.isfile(os.path.join(local_directory, filename)):
#         upload_file(os.path.join(local_directory, filename))
upload_file("Jaipur and Agra Trip August 2023-37.jpg")

# Close the FTP connection
ftp.quit()

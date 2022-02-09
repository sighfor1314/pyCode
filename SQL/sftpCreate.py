import pysftp
import sys

sftp = pysftp.Connection(
  host="pg.qa.sis.ai",
  username="fileuser",
  password="jarvix123"
)
print(sftp)
with sftp.cd('./upload/DorisTest'):  # temporarily chdir to public
     sftp.put('test0087.csv')  # upload file to public/ on remote
# sftp.cd('./upload/DorisTest')
# sftp.put('test0087.xlsx')
# with pysftp.Connection('pg.qa.sis.ai', username='fileuser', password='jarvix123') as sftp:
#   with sftp.cd('./upload/DorisTest'):  # temporarily chdir to public
#     sftp.put('test0087.csv')  # upload file to public/ on remote
#     # sftp.get('remote_file')
sftp.close()


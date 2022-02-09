import cx_Oracle
import pandas as pd
import pymssql
import mysql.connector
import psycopg2
import pysftp
import configparser


cx_Oracle.init_oracle_client(lib_dir="/Users/synergies/Downloads/instantclient_19_8")


def connectDatabase(db):
    ini_file_name = ("qajarvix.ini")
    configuration = configparser.ConfigParser()
    configuration.optionxform = str
    configuration.read(ini_file_name)



    if configuration[db]['type'] == 'ORACLE':
        return cx_Oracle.connect(configuration[db]['db-username'], configuration[db]['db-password'],
                                    configuration[db]['db-host'] + ':' + configuration[db]['db-port'] + '/' +
                                    configuration[db]['db-name'])

    elif configuration[db]['type'] == 'MYSQL':
        return mysql.connector.connect(host=configuration[db]['db-host'], user=configuration[db]['db-username'],
                                          password=configuration[db]['db-password'],
                                          database=configuration[db]['db-name'])

    elif configuration[db]['type'] == 'MSSQL':
        return pymssql.connect(host=configuration[db]['db-host'], user=configuration[db]['db-username'],
                                  password=configuration[db]['db-password'], database=configuration[db]['db-name'])

    elif configuration[db]['type'] == 'POSTGRESQL':
        return psycopg2.connect(host=configuration[db]['db-host'], user=configuration[db]['db-username'],
                               password=configuration[db]['db-password'], database=configuration[db]['db-name'])

    elif configuration[db]['type'] == 'sftp':
        return pysftp.Connection(host=configuration[db]['sftp-host'], username=configuration[db]['sftp-username'],
                                 password=configuration[db]['sftp-password'])



def setSftpInsertion(sftp,file_path,sftp_path):
    connect=connectDatabase(sftp)
    with connect.cd(sftp_path):  # temporarily chdir to public
        connect.put(file_path)  # upload file to public/ on remote
    connect.close()
def setSftpDeletion(sftp,file_name,sftp_path):
    connect = connectDatabase(sftp)
    with connect.cd(sftp_path):  # temporarily chdir to public
        connect.remove(file_name)  # upload file to public/ on remote
    connect.close()


def setSqlInsertion(db, file_path, table_name):
    connect=connectDatabase(db)
    cur = connect.cursor()
    try:
        with open(file_path, newline=''):
            data = pd.read_csv(file_path)
            column_length = len(data.values[0])
            column_count = ""

            if isinstance(connect, cx_Oracle.Connection):
                for i in range(1, column_length + 1):
                    column_count += ':' + str(i)
                    if i != column_length:
                        column_count += ','
            else:
                for i in range(1, column_length + 1):
                    column_count += '%s'
                    if i != column_length:
                        column_count += ','

            rows = [tuple(x) for x in data.values]
            sql_insert = "INSERT INTO %s VALUES (%s)" % (table_name, column_count)
            cur.executemany(sql_insert, rows)
            connect.commit()
    except Exception as e:
        print(e)
    finally:
        connect.close()


def setSqlDeletion(db, table_name, condition=''):
    connect= connectDatabase(db)
    cur = connect.cursor()
    sql_delete = 'delete from %s  %s' % (table_name, condition)
    cur.execute(sql_delete)
    connect.commit()
    connect.close()

sftp_path = './upload/DorisTest'
file_path = 'test005.csv'
table_name = 'test0087'
condition = ''


setSftpDeletion('sftp-qa',file_path,sftp_path)
# setDeleteSql('mssql 1433',table_name,condition)
# DataBase.setSqlInsertion('oracle 10g')

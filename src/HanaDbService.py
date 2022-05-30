from pickle import TRUE
from hdbcli import dbapi
from cfenv import AppEnv

class HanaDb(object):
    def __init__(self):
        env = AppEnv()
        hana_service = 'hana'
        hana = env.get_service(label=hana_service)
        self.conn = dbapi.connect(address=hana.credentials['host'],
                             port=int(hana.credentials['port']),
                             user=hana.credentials['user'],
                             password=hana.credentials['password'],
                             encrypt='true',
                             sslTrustStore=hana.credentials['certificate'])

        self.db_schema = '301CF7B2C5DF4AF6B3384D9A522D94DD'

    def __del__(self):
        self.conn.close()

    def get_table_name_with_schema(self, table_name):
        table_name_with_schema = self.db_schema + "." + table_name
        return table_name_with_schema

    def query_all(self, sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as ex:
            print("query_all>>>>>>", ex)
    
    def query_one(self, sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchone() 
        except Exception as ex:
            print("query_one>>>>>>", ex)
    
    def add_one(self, sql, vals):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, vals)
                self.conn.commit()
                return True
        except Exception as ex:
            print("add_one>>>>>>", ex)
        return False
         

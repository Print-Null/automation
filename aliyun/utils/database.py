import pymysql
from common.readconfig import ReadConfig
import utils.redisbase as redisbase
import logging


class Database:
    def __init__(self, name):
        self.redisObj = redisbase.RedisBase()
        runenv = self.redisObj.get("runenv_py")
        if runenv == False:
            runenv = "trunk"
        confObj = ReadConfig()
        runenv = "trunk"
        if name == "fle":
            host = confObj.get_config(runenv, "database_fle_host")
            user = confObj.get_config(runenv, "database_fle_username")
            password = confObj.get_config(runenv, "database_fle_password")
            database = confObj.get_config(runenv, "database_fle_dbname")
            port = confObj.get_config(runenv, "database_fle_port")
        elif name == "bi":
            host = confObj.get_config(runenv, "database_rbi_host")
            user = confObj.get_config(runenv, "database_rbi_username")
            password = confObj.get_config(runenv, "database_rbi_password")
            database = confObj.get_config(runenv, "database_rbi_dbname")
            port = confObj.get_config(runenv, "database_rbi_port")
        else:
            host = confObj.get_config(runenv, "database_rbi_host")
            user = confObj.get_config(runenv, "database_rbi_username")
            password = confObj.get_config(runenv, "database_rbi_password")
            database = confObj.get_config(runenv, "database_rbi_dbname")
            port = confObj.get_config(runenv, "database_rbi_port")
        self._db_args = dict(use_unicode = True, charset = "utf8", host = host, user = user,
                             password = password, database = database,
                             port = int(port),
                             db = database, init_command = 'SET time_zone = "+8:00"',
                             sql_mode = "TRADITIONAL")
        self._db = None
        try:
            self.reconnect()
        except pymysql.Error:
            logging.error("Cannot connect to MySQL on %s", host, exc_info = True)

    def reconnect(self):
        self.close()
        self._db = pymysql.Connection(**self._db_args)
        self._db.autocommit(False)

    def close(self):
        if self._db is not None:
            self._db.close()
            self._db = None

    def query(self, query, *parameters):
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters)
            column_names = [d[0] for d in cursor.description]
            return [ObjDict(zip(column_names, row)) for row in cursor]
        finally:
            cursor.close()

    def _cursor(self):
        if self._db is None:
            self.reconnect()
        try:
            self._db.ping()
        except pymysql.MySQLError:
            self.reconnect()
        return self._db.cursor()

    def _execute(self, cursor, query, parameters):
        try:
            return cursor.execute(query, parameters)
        except pymysql.OperationalError:
            logging.error("Error connecting to MySQL on %s", self.host)
            self.close()
            raise

    def __del__(self):
        self.close()

    def get(self, query, *parameters):
        rows = self.query(query, *parameters)
        if not rows:
            return None
        elif len(rows) > 1:
            raise Exception("Multiple rows returned for Database.get() query")
        else:
            return rows[0]

    def execute(self, query, *parameters):
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def executemany(self, query, parameters):
        cursor = self._cursor()
        try:
            cursor.executemany(query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()


class ObjDict(dict):

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            return "0"

    def __setattr__(self, key, value):
        self[key] = value

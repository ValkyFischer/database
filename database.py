"""https://valky.dev/"""

import pymysql
import pyodbc


class Database:
	def __init__(self, logger, config):
		self.log = logger
		self.cfg = config

	def testMssql(self) -> bool:
		host = self.cfg['MsSQL']['host']
		user = self.cfg['MsSQL']['user']
		password = self.cfg['MsSQL']['pass']
		database = self.cfg['MsSQL']['base']
		driver = '{SQL Server Native Client 11.0}'

		try:
			conn = pyodbc.connect(
				f'Driver={driver};'
				f'Server={host};'
				f'Database={database};'
				f'UID={user};'
				f'PWD={password};'
			)
			link = conn.cursor()
			link.execute("SELECT * FROM DbInfo")
			data = link.fetchone()

			self.log.Info(f"Connection established: {database} v{data[0]}")

			conn.close()
			return True
		except:
			self.log.Error(f"'{database}' cannot be reached!")
			return False


	def testMysql(self) -> bool:
		host = self.cfg['MySQL']['host']
		user = self.cfg['MySQL']['user']
		password = self.cfg['MySQL']['pass']
		database = self.cfg['MySQL']['base']
		charset = 'utf8mb4'
		cursorclass = pymysql.cursors.DictCursor

		try:
			conn = pymysql.connect(
				host=host,
				user=user,
				password=password,
				database=database,
				charset=charset,
				cursorclass=cursorclass
			)
			link = conn.cursor()
			link.execute("SELECT VERSION()")
			data = link.fetchone()

			self.log.Info(f"Connection established: {database} v{data['VERSION()']}")

			conn.close()
			return True
		except:
			self.log.Error(f"'{database}' cannot be reached!")
			return False


	def connectMysql(self):

		host = self.cfg['MySQL']['host']
		user = self.cfg['MySQL']['user']
		password = self.cfg['MySQL']['pass']
		database = self.cfg['MySQL']['base']
		charset = 'utf8mb4'
		cursorclass = pymysql.cursors.DictCursor

		conn = pymysql.connect(
			host=host,
			user=user,
			password=password,
			database=database,
			charset=charset,
			cursorclass=cursorclass
		)

		link = conn.cursor()

		return link, conn

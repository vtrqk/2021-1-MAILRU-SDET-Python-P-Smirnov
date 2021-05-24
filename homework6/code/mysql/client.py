import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from mysql.models import Base


class MysqlClient:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = '127.0.0.1'
        self.port = 3306

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''

        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine,
                                    autocommit=True,
                                    expire_on_commit=False
                                    )()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def recreate_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)
        self.connection.close()

    def create_largest_req(self):
        if not inspect(self.engine).has_table('largest_req'):
            Base.metadata.tables['largest_req'].create(self.engine)

    def create_all_requests(self):
        if not inspect(self.engine).has_table('all_requests'):
            Base.metadata.tables['all_requests'].create(self.engine)

    def create_post_and_get(self):
        if not inspect(self.engine).has_table('post_and_get'):
            Base.metadata.tables['post_and_get'].create(self.engine)

    def create_favorite_req(self):
        if not inspect(self.engine).has_table('favorite_req'):
            Base.metadata.tables['favorite_req'].create(self.engine)

    def create_top_users(self):
        if not inspect(self.engine).has_table('top_users'):
            Base.metadata.tables['top_users'].create(self.engine)

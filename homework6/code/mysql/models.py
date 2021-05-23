from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PostAndGet(Base):
    __tablename__ = 'post_and_get'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    get_count = Column(Integer, nullable=False)
    post_count = Column(Integer, nullable=False)


class AllRequests(Base):
    __tablename__ = 'all_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    count_all = Column(Integer, nullable=False)


class FavoriteRequests(Base):
    __tablename__ = 'favorite_req'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_url = Column(String(50), nullable=False)
    count = Column(String(20), nullable=False)


class LargestReq(Base):

    __tablename__ = 'largest_req'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_req = Column(String(50), nullable=False)
    name_url = Column(String(50), nullable=False)
    code_err = Column(String(10), nullable=False)
    size = Column(String(20), nullable=False)


class TopUsers(Base):
    __tablename__ = 'top_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)

    ip_user = Column(String(50), nullable=False)
    count = Column(String(20), nullable=False)



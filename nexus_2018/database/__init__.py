import app.config as Config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Table_Prefix = Config.Table_Prefix

Database_Engine_URL = (
    '%s://%s:%s@%s/%s' % (
        Config.Database_Engine,
        Config.Database_Username,
        Config.Database_Password,
        Config.Database_Hostname,
        Config.Database_Name)
    )

engine = create_engine(Database_Engine_URL)

Base = declarative_base()
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
DBH = DBSession()


from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

conn = create_engine(url='sqlite:///DataBase/gestao_usuario.db')

Session = sessionmaker(bind=conn)

session = Session()
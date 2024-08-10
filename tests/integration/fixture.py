import pytest
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infrastructure.database import Base
from app.infrastructure.database import get_db
from app.main import app

@pytest.fixture(scope='function')
def db():
    # Criar uma conexão com o banco de dados em memória
    engine = create_engine('sqlite:///./fastapitest.db')
    # Limpar o banco de dados antes de cada teste
    Base.metadata.create_all(bind=engine)
    
    # Criar uma sessão para a conexão
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Substituir a sessão de banco de dados padrão pela sessão de teste
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    
    yield {
      'session': session,
      'client': client
    }

    # Limpar os dados após cada teste
    session.close()
    Base.metadata.drop_all(bind=engine)
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test cases for the '/topic' endpoint
def test_valid_topic():
    response = client.get('/topic?topic=pokemon&n=5')
    assert response.status_code == 200
    assert 'most_common_words' in response.json()

def test_invalid_topic():
    response = client.get('/topic?topic=goravar inu&n=5')
    assert response.status_code == 404

def test_topic_with_a_non_english_character():
    response = client.get('/topic?topic=Pokémon&n=5')
    assert response.status_code == 200
    assert 'most_common_words' in response.json()

def test_topic_with_non_enlish_word():
    response = client.get('/topic?topic=ポケモン&n=5')
    assert response.status_code == 200
    assert 'most_common_words' in response.json()
    
def test_fewer_words_than_n():
    response = client.get('/topic?topic=panda&n=10000')
    assert response.status_code == 200
    assert 'most_common_words' in response.json()
    assert len(response.json()['most_common_words']) <= 10000  
       
# Test cases for the '/history' endpoint
def test_history_file_exists():
    response = client.get('/history')
    assert response.status_code == 200
    assert 'history' in response.json()

def test_history_file_not_exists(monkeypatch):
    def mock_open(*args, **kwargs):
        raise FileNotFoundError
    monkeypatch.setattr('builtins.open', mock_open)
    
    response = client.get('/history')
    assert response.status_code == 200
    assert response.json() == {'history': []}

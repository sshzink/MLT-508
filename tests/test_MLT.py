import pytest
from app.services import *
from model.enums import *

@pytest.fixture
def services():
    return Services()
def test_translate_word(services):
    # Assuming the word "cat" is already in the database with its translations

    # Test translation from English to Spanish
    translation_es = services.translate_word("cat", LANG.es)
    assert translation_es == "gato, noun"

    # Test translation from English to French
    translation_fr = services.translate_word("cat", LANG.fr)
    assert translation_fr == "chat, noun"
import pytest
from app.services import *
from model.enums import *

@pytest.fixture
def services():
    return Services()
def test_translate_word(services):

    translation_es = services.translate_word("cat", LANG.ENGLISH, LANG.SPANISH)
    assert translation_es == "gato, NOUN"

    translation_fr = services.translate_word("cat", LANG.ENGLISH, LANG.FRENCH)
    assert translation_fr == "chat, NOUN"

from model.enums import *


class Word:

    def __init__(self, id, form, lang: LANG, pos: POS):
        self.id = id
        self.form = form
        self.lang = lang
        self.pos = pos
        self.eq_in_en = []
        self.eq_in_es = []
        self.eq_in_fr = []

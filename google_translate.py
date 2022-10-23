from googletrans import Translator

def sourceTranslate(text, lang_src, lang_dest):
    if lang_src == lang_dest:
        return text

    translator = Translator()

    return translator.translate(text, src=lang_src, dest=lang_dest).text
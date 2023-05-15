# import os
# from dotenv import load_dotenv
# import deepl
from translate_shell.translate import translate

# .envファイルの内容を読み込見込む
# load_dotenv()

# API_KEY = os.environ['DEEPL_API_KEY']
# translator = deepl.Translator(API_KEY)

def jp_en_translate(text):
    # source_lang = 'JA'
    # target_lang = 'EN-US'
    source_lang = "ja_JP"
    target_lang = "en_US"
    # result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    result = translate(text, target_lang=target_lang, source_lang=source_lang).results[0]["paraphrase"]
    return result
    
def en_jp_translate(text):
    # source_lang = 'EN'
    # target_lang = 'JA'
    source_lang = "en_US"
    target_lang = "ja_JP"
    # result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    result = translate(text, source_lang=source_lang, target_lang=target_lang).results[0]["paraphrase"]
    return result

if __name__ == '__main__':
    test = 'これは日本語です'
    en = "this is a pen."
    print(en_jp_translate(en))
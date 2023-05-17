# import os
# from dotenv import load_dotenv
# import deepl
from translate_shell.translate import translate

# .envファイルの内容を読み込見込む
# load_dotenv()

# API_KEY = os.environ['DEEPL_API_KEY']
# translator = deepl.Translator(API_KEY)

def jp_en_translate(text: str):
    # source_lang = 'JA'
    # target_lang = 'EN-US'
    # result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    source_lang = "ja_JP"
    target_lang = "en_US"
    result = translate_lines(text, source_lang=source_lang, target_lang=target_lang)
    return result
    
def en_jp_translate(text: str):
    # source_lang = 'EN'
    # target_lang = 'JA'
    # result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    source_lang = "en_US"
    target_lang = "ja_JP"
    result = translate_lines(text, source_lang=source_lang, target_lang=target_lang)
    return result

def translate_lines(text: str, source_lang, target_lang):
    text_lines = text.split("\n")
    result_lines = []
    for l in text_lines:
        if l == "":
            result_lines.append("")
        else:
            result_lines.append(translate(l, target_lang=target_lang, source_lang=source_lang).results[0]["paraphrase"])
    result = "\n".join(result_lines)
    return result

if __name__ == '__main__':
    test = 'これは日本語です'
    en = "this is a pen.\nthis is an apple.\n\nahh!!!"
    print(en_jp_translate(en))
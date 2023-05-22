# import os
# from dotenv import load_dotenv
# import deepl
from translate_shell.translate import translate
import re

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
            l, repl = replace_url_string(l)
            translated_l = translate(l, target_lang=target_lang, source_lang=source_lang).results[0]["paraphrase"]
            translated_l = undo_replaced_string(translated_l, repl)
            result_lines.append(translated_l)

    result = "\n".join(result_lines)
    return result

def replace_url_string(text: str):
    repl_strs = {}
    url_matches = re.findall(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", text)
    rac_matches = re.findall(r":[\w\-]+:", text)
    for i, repl_from in enumerate(url_matches):
        repl_to = f"{{{{ URL{i:02d} }}}}"
        text = text.replace(repl_from, repl_to)
        repl_strs[repl_to] = repl_from
    for i, repl_from in enumerate(rac_matches):
        repl_to = f"{{{{ RAC{i:02d} }}}}"
        text = text.replace(repl_from, repl_to)
        repl_strs[repl_to] = repl_from
    
    return text, repl_strs

def undo_replaced_string(text: str, repl_strs: dict):
    for repl_from, repl_to in repl_strs.items():
        text = text.replace(repl_from, repl_to)
    return text

if __name__ == '__main__':
    test = 'これは日本語です'
    en = "this is a pen.\nthis is an apple.\n\nahh!!!"
    print(en_jp_translate(en))
import translators as ts
from typing import List

from logging_utils import get_logger

logger = get_logger()


class TranslationService:
    @staticmethod
    def translate_google(phrase: str, language: str):
        return ts.translate_text(phrase, translator='google', to_language=language, sleep_seconds=1)

    @staticmethod
    def translate_bing(phrase: str, language: str):
        return ts.translate_text(phrase, translator='bing', to_language=language)

    @staticmethod
    def translate_deepl(phrase: str, language: str):
        return ts.translate_text(phrase, translator='deepl', to_language=language, sleep_seconds=1)

    @staticmethod
    def get_translated_subtitles(subtitles: List[str], language: str):
        # subtitles files contains block with logical groups:
        # 0. number
        # 1. time
        # 2..... k. actual text
        # k+1. empty
        # so, we translate after 2 line until new line

        translated = []

        count = 0
        total_lines = len(subtitles)
        current = 0

        while current < total_lines:
            line = subtitles[current]

            if count < 2:
                count += 1
            else:
                sentence = ""

                while subtitles[current] != "\n" and current < total_lines:
                    sentence += subtitles[current]
                    current += 1

                sentence = sentence.replace("\n", " ")
                sentence = TranslationService.translate_google(sentence, language)
                sentence = sentence + "\n"
                sentence = sentence.replace(" - ", "\n- ")

                print(sentence)

                line = sentence + "\n"
                count = 0

            translated.append(line)
            current += 1

        return translated

        # return ts.deepl(phrase, to_language=language, sleep_seconds=5)

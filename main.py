from logging_utils import get_logger
from services.translation_service import TranslationService
from services.txt_service import TxtService

TARGET_LANGUAGE = "lt"
INPUT_FILE_PATH = "data/Kung.Fu.Panda.4.2024.720p.AMZN.WEBRip.800MB.x264-GalaxyRG.Hi.srt"
OUTPUT_FILE_PATH = "data/done-v3.srt"

logger = get_logger()


def start_stt():
    logger.info("Starting application")
    original_file = TxtService.read_lines(INPUT_FILE_PATH)

    translation = TranslationService.get_translated_subtitles(original_file, TARGET_LANGUAGE)

    TxtService.write_lines(OUTPUT_FILE_PATH, translation)

    logger.info("Application stopped")


if __name__ == "__main__":
    start_stt()

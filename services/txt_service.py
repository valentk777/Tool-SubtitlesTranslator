from os import path
from typing import List

from logging_utils import get_logger
from services.file_service import FileService

logger = get_logger()


class TxtService(FileService):
    @staticmethod
    def read(file_path: str) -> str:
        logger.info("Started")

        if not path.exists(file_path):
            raise Exception(f"file not found. Path {file_path}")

        with open(file_path, 'r', encoding="utf-8") as f:
            text = f.read()

            logger.info("Completed")

            return text

    @staticmethod
    def read_lines(file_path: str) -> List[str]:
        logger.info("Started")

        if not path.exists(file_path):
            raise Exception(f"file not found. Path {file_path}")

        with open(file_path, 'r', encoding="utf-8") as f:
            lines = f.readlines()

            logger.info("Completed")

            return lines

    @staticmethod
    def write_lines(file_path: str, data: List[str]) -> None:
        logger.info("Started")

        with open(file_path, 'w', encoding="utf-8") as f:
            f.writelines(data)

            logger.info("Completed")


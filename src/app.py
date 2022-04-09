import json
from file_reader import FileReader


def main():
    file_reader = FileReader()

    file_reader.parse_logs(
        ["../source_logs/prod_jmsserver_OLIN_s1a-prod_jmsserver_OLIN_s1a.log.2022-03-31"])


if __name__ == '__main__':
    main()

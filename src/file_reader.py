import regex


class FileReader:
    def __init__(self) -> None:
        self.__date = "([A-Z]{1}[a-z]{2}\s[0-9]{2}[,]{1}\s[0-9]{4}\s[0-9]{2}:[0-9]{2}:[0-9]{2}[,]{1}[0-9]{3})"
        self.__message_id = "(<ID:)(<.{23}>)"
        self.__queue_and_action = "([a-z12]{3})(.{1})([a-zA-Z]{7,12})(>.<)([A-Z]{1}[a-z]{0,9})(>\s<)([a-z]{4,12})"
        #self.__producer = "(Produced>\s<)([a-z]{4})"
        #self.__consumer = "(Consumed>\s<)([a-z]{4})"
        #self.__jms_queue = "(olinModule!prod_jmsserver_OLIN_)([a-z12]{3})(.{1})([a-zA-Z]{7})"

    def parse_logs(self, file_list: list) -> list:
        for file_name in file_list:
            with open(file_name, "r") as file:
                for line in file:
                    self.__analyze_line(line)

    def __analyze_line(self, line: str) -> None:
        regex_matches = regex.findall(self.__date, line)

        if (len(regex_matches) >= 1):
            date = regex_matches[0]
            message_id = regex.findall(self.__message_id, line)[0][1]
            queue_and_action = regex.findall(self.__queue_and_action, line)[0]
            member = queue_and_action[0]
            queue = queue_and_action[2]
            action = queue_and_action[4]
            user = queue_and_action[6]

            print(f"Date: {date}\nMessage_id: {message_id}\nMember: {member}\nQueue: {queue}\nAction: {action}\nUser: {user}")

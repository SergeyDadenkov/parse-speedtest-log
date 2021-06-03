import argparse
import utils
from app.db.client import DB
from app.server.config import PATH_SPEEDTEST_LOG, INSERT_SPEEDTEST

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, dest='config', default='./db/config.txt')
    args = parser.parse_args()
    # print(args)
    config = utils.config_parser(args.config)

    CONNECTION_STRING = f'DRIVER={config["DB_DRIVER"]};SERVER={config["DB_HOST"]};PORT={config["DB_PORT"]};DATABASE={config["DB_NAME"]};UID={config["DB_USER"]};PWD={config["DB_PASSWORD"]}'
    db = DB(CONNECTION_STRING)

    lines = []
    with open(PATH_SPEEDTEST_LOG, 'r') as file_read:
        lines = file_read.readlines()

    with open(PATH_SPEEDTEST_LOG, 'w') as file_write:
        for line in lines:
            dict = eval(line.replace('false', 'False'))
            # 123
            # print(f'timestamp: {dict["timestamp"]}, download.bandwidth: {dict["download"]["bandwidth"]}, upload.bandwidth: {dict["upload"]["bandwidth"]},'
            #       f'interface.internalIp: {dict["interface"]["internalIp"]}, interface.externalIp: {dict["interface"]["externalIp"]}, server.ip: {dict["server"]["ip"]}')
            QUERY = INSERT_SPEEDTEST.format(dict["timestamp"], dict["download"]["bandwidth"], dict["upload"]["bandwidth"], dict["interface"]["internalIp"], dict["interface"]["externalIp"], dict["server"]["ip"])
            if not db.execute(QUERY):  # Запись в БД
                print(f'Выполнение запроса привело к ошибке: {QUERY}')
                file_write.write(line)

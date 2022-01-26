import vk_api
import sys
from report.parser import parse_arg
from report.vk_api_wrapper import VkApiWrapper
from report.friends_report import FriendsReport
from report.writer.csv_tsv_writer import WriterCsvTsv
from report.writer.json_data_writer import WriterJson


def main() -> None:

    parser = parse_arg(sys.argv[1:])
    token = parser.token
    user_id = parser.user_id
    format_file = parser.format
    session = vk_api.VkApi(token=token)
    vk = session.get_api()
    api = VkApiWrapper(vk)
    report = FriendsReport(api=api)
    print('Идет процесс получения данных')
    data = report.get_data(user_id=user_id)
    data.sort(key=lambda x: x['first_name'])
    print('Данные получены')
    if format_file == 'csv':
        writer = WriterCsvTsv(',')
        writer.write('report.csv', data)
    elif format_file == 'tsv':
        writer = WriterCsvTsv('\t')
        writer.write('report.tsv', data)
    elif format_file == 'json':
        writer = WriterJson(4)
        writer.write(data, 'report.json')
    else:
        print('Неизвестная ошибка')
    print('Отчет записан')
    return


if __name__ == '__main__':
    main()

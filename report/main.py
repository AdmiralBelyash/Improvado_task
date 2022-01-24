import vk_api
from vk_api_wrapper import VkApiWrapper
from friends_report import FriendsReport
from report.writer.csv_tsv_writer import WriterCsvTsv
from report.writer.json_data_writer import WriterJson


def main() -> None:
    while True:
        token = input('Введите ваш токен: ')
        user_id = input('Введите id пользователя для поиска друзей: ')
        session = vk_api.VkApi(token=token)
        vk = session.get_api()
        api = VkApiWrapper(vk)
        try:
            friends = api.get_user_friends(user_id=user_id)
        except vk_api.exceptions.ApiError:
            print('Неверный токен или id пользователя')
            continue

        report = FriendsReport(api=api)
        print('Идет процесс получения данных')
        data = []
        for friend in friends:
            data.append(report.get_data(friend))
        data.sort(key=lambda x: x['first_name'])
        print('Данные получены')
        while True:
            print('Выберите формат отчета: '
                  '1 - CSV\n'
                  '2 - TSV\n'
                  '3 - JSON\n'
                  '0 - Выход\n')

            key = int(input('Ключ: '))
            if key == 1:
                writer = WriterCsvTsv(',')
                writer.write('report.csv', data)
            elif key == 2:
                writer = WriterCsvTsv('\t')
                writer.write('report.tsv', data)
            elif key == 3:
                writer = WriterJson(4)
                writer.write(data, 'report.json')
            elif key == 0:
                return
            else:
                writer = WriterCsvTsv(',')
                writer.write(data, 'report.csv')
            print('Отчет выгружен')
            continue


if __name__ == '__main__':
    main()

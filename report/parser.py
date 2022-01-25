import argparse


def parse_arg(args: list[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', help="Токен для авторизации vk api", type=str, required=True)
    parser.add_argument('-u', '--user_id', help="Id пользователя для поиска друзей", type=int, required=True)
    parser.add_argument('-f', '--format', help='Формат вывода отчета', default='csv',
                        type=str, choices=['csv', 'tsv', 'json'])

    return parser.parse_args(args)
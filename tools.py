import argparse
import os, shutil
import re


# parse args
def set_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo",
        dest="repo",
        help="репозиторий для клонирования или переменная окружения GIT_CLONE_REPO"
    )
    parser.add_argument(
        "--branch",
        dest="branch",
        help="ветка для клонирования или переменная окружения GIT_CLONE_BRANCH"
    )
    parser.add_argument(
        "--default",
        dest="default",
        default=False,
        # type=bool,
        help="если true(bool) или переменная окружения GIT_CLONE_DEFAULT. Если задано, то GIT_CLONE_REPO=CI_REPOSITORY_URL, GIT_CLONE_BRANCH=CI_COMMIT_REF_NAME"
    )
    parser.add_argument(
        "--force",
        dest="force",
        default=False,
        # type=bool,
        help="если true(bool), или переменная окружения GIT_CLONE_FORCE. Если задано, то пересоздаем целевой каталог клонируем (если он по какой-то причине есть)"
    )
    parser.add_argument(
        "--path",
        dest="path",
        help="целевой каталог для репозитория или переменная окружения GIT_CLONE_DIR, в каталог по имени репозитория"
    )
    parser.add_argument(
        "--user",
        dest="user",
        help="пользователь от которого клонируем (по http) или переменная окружения GIT_CLONE_USER, или GITLAB_BOT_USER"
    )
    parser.add_argument(
        "--pass",
        dest="passw",
        help="пароль пользователя от которого клонируем (по http) или переменная окружения GIT_CLONE_PASS, или GITLAB_BOT_PASS"
    )
    parser.add_argument(
        "--token",
        dest="token",
        help="токен для клонирования (по http) или переменная окружения GIT_CLONE_TOKEN, или GITLAB_BOT_TOKEN"
    )
    parser.add_argument(
        "--key",
        dest="key",
        help="путь до id_rsa ключа для клонирования (по ssh) или переменная окружения GIT_KEY_PATH, или ~/.ssh/id_rsa"
    )

    args = parser.parse_args()
    return args


# check elements in args for None and set on env
def set_args_from_os_env(args):
    if args.default == True or os.getenv('GIT_CLONE_DEFAULT') == True:
        os.environ['GIT_CLONE_REPO'] = os.getenv('CI_REPOSITORY_URL')
        os.environ['GIT_CLONE_BRANCH'] = os.getenv('CI_COMMIT_REF_NAME')

    if os.getenv('GIT_CLONE_FORCE'):
        args.force = args.force or os.getenv('GIT_CLONE_FORCE')
    args.repo = args.repo or os.getenv('GIT_CLONE_REPO')
    args.branch = args.branch or os.getenv('GIT_CLONE_BRANCH')
    args.path = args.path or os.getenv('GIT_CLONE_DIR')
    args.user = args.user or os.getenv('GIT_CLONE_USER') or os.getenv('GITLAB_BOT_USER')
    args.passw = args.passw or os.getenv('GIT_CLONE_PASS') or os.getenv('GITLAB_BOT_PASS')
    args.token = args.token or os.getenv('GIT_CLONE_TOKEN') or os.getenv('GITLAB_BOT_TOKEN')

    return args


# set bool elems in args
def set_bool(args):
    if args.default != False: args.default = get_bool(args.default)
    if args.force != False: args.force = get_bool(args.force)
    return args


## get_bool('yes') - return bool
def get_bool(arg):
    find = re.match('^(1|true|on|yes|y)$',arg, re.IGNORECASE)
    if find != None: return True
    else: return False


# check args for None
def check_none(args, check_args):
    # not_check_args = ['token', 'passw', 'key', 'default', 'force']
    if args.token is None:
        if args.passw is None:
            print('ОШИБКА: Не указаны данные для авторизации')
            return exit(1)
    args = args.__dict__
    dict_nones = []
    for arg, value in args.items():
        if arg in check_args:
            if value is None: dict_nones.append(arg)
    if dict_nones != []:
        print('ОШИБКА: У Вас не заполнены: ' + ', '.join(dict_nones))
        return exit(1)



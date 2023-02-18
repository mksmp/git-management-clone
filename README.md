# git-management-clone
**скрипт для клонирования репозитория git-clone.py**
## Запуск
### *Необязательно, но рекомендуется:* Установка и активация виртуального окружения: 
- ```python -m venv venv```
- Активация
    - Windows: ```venv\Scripts\activate```
    - GNU/Linux: ```source venv/bin/activate```
- ```pip install -r requirements.txt```

```python.exe .\git-clone.py [-h] [--repo REPO] [--branch BRANCH] [--default DEFAULT] [--force FORCE] [--path PATH] [--user USER] [--pass PASSW] [--token TOKEN] [--key KEY]```

## Справка

**Переменные окружения имеют меньший приоритет чем ключ.**

**```-h, --help```** показать эту справку и завершить

**```--repo REPO```** репозиторий для клонирования или пустой, если есть переменная окружения ```GIT_CLONE_REPO```

**```--branch BRANCH```** ветка для клонирования или пустой, если есть переменная окружения ```GIT_CLONE_BRANCH```

**```--default DEFAULT```** **(если указаны значения 1|true|on|yes|y, то будет значение True, если указано что-то другое - False. По умолчанию, если не указывать, значение False)** если true(bool) или пустой, если есть переменная окружения ```GIT_CLONE_DEFAULT```. Если задано, то ```GIT_CLONE_REPO=CI_REPOSITORY_URL```, ```GIT_CLONE_BRANCH=CI_COMMIT_REF_NAME```

**```--force FORCE```** **(если указаны значения 1|true|on|yes|y, то будет значение True, если указано что-то другое - False. По умолчанию, если не указывать, значение False)** если true(bool), или пустой, если есть переменная окружения ```GIT_CLONE_FORCE```. Если задано, то пересоздаем целевой каталог клонируем (если он по какой-то причине есть)

**```--path PATH```** целевой каталог для репозитория или переменная окружения ```GIT_CLONE_DIR```, в каталог по имени репозитория

**```--user USER```** пользователь от которого клонируем (по http) или пустой, если есть переменная окружения ```GIT_CLONE_USER```, или ```GITLAB_BOT_USER```

**```--pass PASSW```** пароль пользователя от которого клонируем (по http) или переменная окружения ```GIT_CLONE_PASS```, или ```GITLAB_BOT_PASS```

**```--token TOKEN```** токен для клонирования (по http) или переменная окружения ```GIT_CLONE_TOKEN```, или ```GITLAB_BOT_TOKEN```

**```--key KEY```** путь до id_rsa ключа для клонирования (по ssh) или переменная окружения ```GIT_KEY_PATH```, или ```~/.ssh/id_rsa```

## Troubleshooting

Пока не отработано клонирование по SSH
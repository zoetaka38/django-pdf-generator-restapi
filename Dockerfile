# どこのイメージを元にするか(今回debianベース)
FROM python:3.9.5

# 必要なOSのライブラリのインストール
RUN apt update
RUN apt install -y openssl

# pipenv環境を整える
RUN pip install -U --no-cache-dir pipenv

# Pipfileからpythonパッケージをインストール
RUN mkdir /app
ADD ./Pipfile /app/Pipfile
ADD ./Pipfile.lock /app/Pipfile.lock
WORKDIR /app/
RUN pipenv install

# アプリのデータを追加する
ADD ./src /app/

CMD [ "pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
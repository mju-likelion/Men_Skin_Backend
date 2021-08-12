# Men_Skin_Backend

Men_Skin_Backend는 백엔드 프레임워크 Django와
오픈소스 데이터베이스인 Mysql을 사용하여 데이터베이스를 구축한다.

## Requirements

- requirements.txt

## HOW to runserver?

- 가상환경 생성

```
python -m venv myvenv # 원하는 가상환경 이름을 설정하면 된다.
```

- 가상환경 실행

```shell
source myvenv/Scripts/activate  # Windows
source myvenv/bin/activate # Mac
```

- 패키지 설치

```
pip install -r requirements.txt
```

- 프로젝트 생성

```shell
django-admin startproject mens
cd mens
```

- 서버 실행

```
python manage.py runserver

python mens/manage.py/runserver
```

## Men_Skin_Backend
- Men_Skin_Backend는 백엔드 프레임워크 Django와 <br>
  오픈소스 데이터베이스인 Mysql을 사용하여 데이터베이스를 구축한다.

### DB Schema(v3)
<img src= "https://user-images.githubusercontent.com/79985009/127145832-32347d1e-4d01-4dfa-abdb-1f4e67c4eaa0.png" width="60%" height="30%">

---

#### HOW to runserver?
- 가상환경 생성
~~~
python -m venv myvenv  - 원하는 가상환경 이름을 설정하면 된다.
~~~

- 가상환경 실행
~~~
source myvenv/Scripts/activate  # Windows
~~~

- 장고 설치
~~~
pip install django
~~~

- 프로젝트 생성
~~~
django-admin startproject men_skin
cd men_skin
~~~

- 서버 실행
~~~
python manage.py runserver
~~~




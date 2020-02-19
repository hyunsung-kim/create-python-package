# create-python-package
In this tutorials, you'll cover how to *upload your own package to PyPI*. 
While getting your project published is easier than it used to be. 

**You should consider:**
  - Python package for publication.
  - Versioning.
  - Compatible with python version. 

**Terminology**
```
- Module: 모듈(module)은 변수, 함수, 클래스 등을 모아 놓은 스크립트 파일임
- Package: 여러 모듈을 묶은 것
- PyPI: Python Package Index 약자로, 패키지 저장소를 의미함
```

**Features**
- [PyPI](https://pypi.org/)
- [S3](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/Welcome.html)

---

## Generating package
패키지를 만들기 전에 라이브러리 구조를 알아보자. 그리고 필요한 파일에 대하여 알아보자.

### `setup.py`
`setup.py` 파일의 속성 및 사용 방법에 대하여 삺펴 보자.
- name: PyPI에서 보여주는 패키지 이름
- version: 패키지의 현재 버전
- packages: 소스 코드에 포함한 패키지와 서브 패키지
- install_requires: 패키지에 포함 시킬 라이브러리
- entry_point: 실행 가능한 스크립트
- setup_requires: `setup.py` 파일 자체에서 필요한 패키지
- setup.cfg: setup.py에 전달하는 명령에 대한 기본 값을 포함(optional)
```ini
# setup.cfg
[nosetests]
verbose=1
nocapture=1
```

## .pypirc 설정
배포 할 곳에 대한 정보를  `$HOME/.pypirc`에 추가한다.

- Example
  ```
  # .pypirc
  [distutils]
  index-servers = 
    pypitest
    pypi
  
  [pypitest]
  repository: https://test.pypi.org/legacy/
  username: __token__
  password: pypi-AgENdGVzdC5weXBpLm9yZwIkMTQ0OGUwODEtMDc1Mi00YzMwLTkwYjMtMzE4NTZmMDIzZjAxAAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiDn4XAx-2xzwJkuJP_Rv7X0P8fvvyioTvNGscRX0FJZSg

  [pypi]
  repository = https://pypi.python.org/pypi
  username = the_gigi
  ```

### Publication
아래에서는 어떻게 패키지를 배포하고 설치하는 지 확인해 보자.

- Build PyPI package
  ```bash
  $ pipenv run python setup.py build
  ```

- Create distribute 
  ```
  $ python setup.py sdist bdist_wheel
  ```

- Registry Test PyPI(only for testing purpose)
  ```bash
  $ twine upload dist/* -r pypitest --verbose
  ```

- Registry Official PyPI 
  ```bash
  $ wine upload dist/* -r pypi
  ```

## Reference
- [Program Configuration in Python](https://www.drdobbs.com/open-source/program-configuration-in-python/240169310)
- [S3 Private PyPI](https://www.novemberfive.co/blog/opensource-pypi-package-repository-tutorial)
- [Package to PyPI](https://realpython.com/pypi-publish-python-package/)
- [나만의 패키지 작성방법](https://code.tutsplus.com/ko/tutorials/how-to-write-your-own-python-packages--cms-26076)
- [Web Classifiers](https://pypi.org/classifiers/)
# KAMI Airlines

Limitation: Only Linux and MacOS

Steps:

* Activate virtual environment
  `$ source ./setupvenv.sh`
* Run project
  `$ cd airlines`
  `$ ./manage.py runserver`

Coverage

From project root:

```
$ cd airlines
```

Run coverage for tests:

```
$ coverage run -m pytest && coverage report && coverage html
```

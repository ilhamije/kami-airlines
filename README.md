# KAMI Airlines

Limitation: Only Linux and MacOS

## Usage

### Activate virtual environment

`source ./setupvenv.sh`

### To do a test coverage:

From project root:

```
cd airlines
```

Run coverage for tests:

```
coverage run -m pytest && coverage report && coverage html
```

Sample Coverage Return

```
Name                                                          Stmts   Miss  Cover
---------------------------------------------------------------------------------
airlines/__init__.py                                              0      0   100%
airlines/settings.py                                             21      0   100%
airlines/urls.py                                                  3      0   100%
airplanes/__init__.py                                             0      0   100%
airplanes/admin.py                                                5      0   100%
airplanes/apps.py                                                 4      0   100%
airplanes/migrations/0001_initial.py                              6      0   100%
airplanes/migrations/0002_airplane_fuel_capacity.py               4      0   100%
airplanes/migrations/0003_auto_20231222_0754.py                   4      0   100%
airplanes/migrations/0004_auto_20231222_0759.py                   4      0   100%
airplanes/migrations/0005_auto_20231222_0815.py                   4      0   100%
airplanes/migrations/0006_rename_id_airplane_airplane_id.py       4      0   100%
airplanes/migrations/0007_auto_20231225_0633.py                   5      0   100%
airplanes/migrations/__init__.py                                  0      0   100%
airplanes/models.py                                              15      1    93%
airplanes/serializers.py                                         21      0   100%
airplanes/tests/__init__.py                                       0      0   100%
airplanes/tests/mock_data.py                                      5      0   100%
airplanes/tests/test_models.py                                   39      2    95%
airplanes/tests/test_views.py                                    70      0   100%
airplanes/urls.py                                                 4      0   100%
airplanes/views.py                                               84      2    98%
---------------------------------------------------------------------------------
TOTAL                                                           302      5    98%
Wrote HTML report to htmlcov/index.html
```

For **detail**, you open htmlcov/index.html in your browser

### To run project

```
cd airlines$
./manage.py runserver
```

If necessary, do a migrations

```
./manage.py migrate
```

### Open in your browser or Postman:

```
http://localhost:8000/airlines
```

#### Airlines API List

| Method | Endpoints | Payload                                      |
| ------ | --------- | -------------------------------------------- |
| GET    | /airlines | None                                         |
| POST   | /airlines | `{ "airplane_id": int, "passenger": int }` |

#### Results Sample

```
[
    {
        "uid": "CBJfSLH6zgAQpAP",
        "airplane_id": 3,
        "passenger": 402,
        "fuel_capacity": "600.000 liters",
        "fuel_consumption": "1.683 liters per min",
        "flight_endurance": "356.506 minutes",
        "created_at": "2023-12-26 07:55:08"
    }
]
```

#### Airlines API Detail

| Method | Endpoints           | Payload                                            |
| ------ | ------------------- | -------------------------------------------------- |
| GET    | /airlines/`<uid>` | None                                               |
| PATCH  | /airlines/`<uid>` | `either/both airplane_id or/and passenger value` |
| DELETE | /airlines/`<uid>` | None                                               |

### (Optional)

To create your admin page

```
./manage.py createsuperuser
```

Fill-in the credentials then open up in your browser:

```
http://localhost:8000/admin
```

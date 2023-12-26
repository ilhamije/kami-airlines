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

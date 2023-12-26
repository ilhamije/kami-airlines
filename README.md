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

| Method | Endpoints | Payload |
| ------ | --------- | ------- |
| GET    | /airlines | None    |
| POST   | /airlines | None    |

#### Airlines API Detail

| Method | Endpoints           | Payload                                      |
| ------ | ------------------- | -------------------------------------------- |
| GET    | /airlines/`<uid>` | `{ "airplane_id": int, "passenger": int }` |
| PATCH  | /airlines/`<uid>` | `{ "airplane_id": int, "passenger": int }` |
| DELETE | /airlines/`<uid>` | None                                         |

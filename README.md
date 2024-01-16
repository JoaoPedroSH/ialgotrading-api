# ialgotrading-api
 

Create and Activate the environment

Linux
```sh
python3 -m venv .venv
. .venv/bin/activate
```

Windows
```sh
py -3 -m venv .venv
.venv\Scripts\activate
```

Install Dependencies
```sh
pip install fastapi[all]
```
```sh
pip install -r requirements.txt
```

Run server

```sh
uvicorn app.main:app --reload
```

## [https://fastapi.tiangolo.com/tutorial/]
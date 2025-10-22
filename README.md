# README

## SETUP: LINUX/MAC

```bash

python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

```
## SETUP: WINDOWS(PS)

```bash

python -m venv venv;  .\venv\Scripts\Activate.ps1; python -m pip install -- upgrade pip; pip install -r requirements.txt

```

## RUN BACKEND

```bash

uvicorn main:app --reload

```

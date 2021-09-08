from fastapi import FastAPI
import datetime
import asyncio
from logging import getLogger

from test_fastapi.apis import first_names

app = FastAPI()
app.include_router(first_names.router)

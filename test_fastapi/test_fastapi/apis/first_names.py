from datetime import datetime
from typing import List
from fastapi import APIRouter
from httpx import AsyncClient

from test_fastapi.apis.schemas.person import PersonRequest, Person

router = APIRouter()

ENDPOINT = "http://localhost:9518/first_names"
PARAMS = (
        (dict(count=100, waiting_time=100), ) * 5 +
        (dict(count=50, waiting_time=80), ) * 5 +
        (dict(count=70, waiting_time=50), ) * 5
)

@router.get("/first_names")
async def first_names() -> List[Person]:
    """Ping an external server for first_name collection."""
    users = []
    async with AsyncClient() as client:
        for params in PARAMS:
            request = await client.get(ENDPOINT, params=params)
            assert r.status_code == 200
            parsed = PersonResponse.parse_obj(request.json())
            users.extend(parsed.items)

    return users

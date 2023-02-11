import requests

from src.constants import URL
# from src.json_schemas.post_schema import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post


def test_correct_url():
    r = requests.get(url=URL)
    response = Response(r)
    response.assert_status_code(200)
    response.validate(Post)

from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int         # = Field(ge=2)   # вместо 10-15 строк
    title: str
    #name: str       #= Field(alias='_name')

    # _name: str  приватная переменная и нельзя провалидировать
    @validator("id")
    def check_id_less_than_two(cls, v):
        if v > 4:
            raise ValueError("Id is not less that two")
        else:
            return v


# {'id': 1, 'title': 'Post 1'}
# {'id': 1, 'title': 'Post 1'Б} '_name': 'Nikita'}

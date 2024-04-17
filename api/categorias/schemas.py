from typing import Annotated

from pydantic import Field
from api.contrib.schemas import BasSchema

class Categoria(BasSchema):
    nome: Annotated[str, Field(description="Nome da categoria", examples="Scale", max_length=10)]

from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import List, Annotated


class DataSerializer(BaseModel):
    out_data: List[str]


app = FastAPI()


@app.get("/{number}", response_model=DataSerializer)
async def get_data(number: Annotated[int, Path(ge=1, le=10000)]):
    out_lst: List[str] = []
    for _ in range(1, number + 1):
        if not (_ % 3) and not(_ % 5):
            out_lst.append("FizzBuzz")
        elif not (_ % 3):
            out_lst.append("Fizz")
        elif not (_ % 5):
            out_lst.append("Buzz")
        else:
            out_lst.append(str(_))
    dct = {"out_data": out_lst}
    return dct

from typing import Optional

from data import User, get_user
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/users/{user_id}")
def read_user(user_id: int) -> dict[str, int | str]:
    user: Optional[User] = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.id, "username": user.name}

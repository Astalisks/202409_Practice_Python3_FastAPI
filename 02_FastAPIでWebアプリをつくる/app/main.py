from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# FastAPIのインスタンス化、タイトル、バージョン、説明の指定
app = FastAPI(
    title="Enhanced FastAPI Application",
    description="This is a sample FastAPI application with path, query, request body, and error handling features.",
    version="1.0.0"
)

# Pydanticモデル: リクエストボディに使用されるデータモデル
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
def read_root():
    return {"message": "Welcome to the Enhanced FastAPI Application!"}


# パスパラメータ、クエリパラメータ、リクエストボディを使用するエンドポイント
@app.post("/items/{item_id}")
def create_item(item_id: int, q: Optional[str] = None, item: Item = None):
    # パスパラメータとしてitem_id、クエリパラメータとしてq、リクエストボディとしてitemを受け取る
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid item_id. It must be greater than 0.")
    
    response = {"item_id": item_id, "item": item.dict()}
    
    if q:
        response.update({"query": q})
    
    return response


# エラーハンドリング例: IDが存在しない場合
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid item_id. It must be greater than 0.")
    
    return {"item_id": item_id, "name": "Sample Item", "description": "This is a sample item."}


# 404エラーに対するカスタムエラーハンドリング
@app.get("/nonexistent")
def nonexistent_route():
    raise HTTPException(status_code=404, detail="This route does not exist.")

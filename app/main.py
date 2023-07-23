from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import PlainTextResponse
from time import sleep
from model.model import Item

app = FastAPI(
    title="IIJ Bootcamp HandsOn",
    description="IIJ Bootcamp Web Application by FastAPI.",
    version="1.0",
)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
items = {"hoge": "This is hoge"}

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    """クエリパラメータ"""
    return fake_items_db[skip: skip + limit]

@app.post("/items/")
def create_item(item: Item):
    """リクエストボディ"""
    return item

@app.get("/plaintext/ok", response_class=PlainTextResponse)
def return_plain_text() -> str:
    return "OK"

@app.get("/error/{item_id}")
def read_item_with_error_handling(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item is not found.")
    return {"item": items[item_id]}

@app.get("/wait/{count}")
async def asgi_task(count: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(print_wait_time, count)
    return {"status": "see the console log for wait time."}

def print_wait_time(count: int):
    print(f"{count}")
    sleep(count)
    print(f"Wait {count} sec & print!")

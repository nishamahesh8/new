from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from auth import register_user, login_user, get_current_user
from crud import get_images_by_filter, save_list, get_lists, delete_list, edit_list_name
from schemas import UserCreate, UserLogin, ListCreate, ListUpdate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
def register(user: UserCreate):
    return register_user(user)

@app.post("/login")
def login(user: UserLogin):
    return login_user(user)

@app.get("/search")
def search(pattern: str):
    return get_images_by_filter(pattern)

@app.post("/lists")
def create_list(list_data: ListCreate, user=Depends(get_current_user)):
    return save_list(list_data, user)

@app.get("/lists")
def read_lists(user=Depends(get_current_user)):
    return get_lists(user)

@app.delete("/lists/{list_id}")
def remove_list(list_id: str, user=Depends(get_current_user)):
    return delete_list(list_id, user)

@app.patch("/lists/{list_id}")
def update_list(list_id: str, update: ListUpdate, user=Depends(get_current_user)):
    return edit_list_name(list_id, update, user)

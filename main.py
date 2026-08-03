from fastapi import FastAPI

app = FastAPI()


#Home Route
@app.get("/")
def home():
    return {"message": "welcome to fast api"}


#About route
@app.get("/about")
def about():
    return {"message": "This is about page"}


#User route
@app.get("/users")
def about():
    return {"data": "this is users data"}
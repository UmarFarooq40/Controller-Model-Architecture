
from app import app
from model.user_model import user_model
obj=user_model()
@app.route('/')
def signup():
    return obj.model()
from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI
import happybase
import uuid


class Chatroom(BaseModel): # models.py
    room_name: str

class Message(BaseModel):
    room_id: str
    text: str

connection = happybase.Connection(host='localhost', port=9090)
connection.open()

app = FastAPI()

@app.get('/')   # => urls.py
def index():    # => views.py
    return {'hello': 'world'}

@app.post('/chatrooms') # Create
def create_chatroom(chatroom: Chatroom):
    table = connection.table('chattings')
    chatroom_id = str(uuid.uuid4())

    table.put(chatroom_id, {'info:room_name': chatroom.room_name})
    
    return {'chatroom_id': chatroom_id, 'room_name': chatroom.room_name}

@app.get('/chatrooms') # Read
def get_chatrooms():
    table= connection.table('chattings')
    rows = table.scan()

    result = []

    for k, v in rows:
        result.append(
            {
                'chatroom_id': k,
                'room_name': v[b'info:room_name']
            }
        )
    return result

@app.post('/messages')
def create_message(message: Message):
    table = connection.table('messagings')

    room_id = message.room_id
    timestamp = int(datetime.now().timestamp() * 1000)
    message_id = f'{room_id}-{timestamp}'

    table.put(message_id, {'info:room_id': room_id, 'info:text': message.text})

    return {
        'message_id': message_id,
        'room_id': room_id,
        'text': message.text
    }

@app.get('/chatrooms/{room_id}/messages')
def get_messages(room_id: str):
    table = connection.table('messagings')
    prefix = room_id.encode('utf-8')

    rows = table.scan(row_prefix=prefix, reverse=True)

    result = []

    for k, v in rows:
        result.append(
            {
                'message_id': k,
                'room_id': v[b'info:room_id'],
                'text': v[b'info:text']
            }
        )
    return result
import uuid
import datetime

from app.main import db
from app.main.model.user import User

# 신규 유저 추가
def save_new_user(data):
    # email이 같은 유저가 있는지 확인
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

# 모든 User 정보를 불러오는 기능
def get_all_users():
    return User.query.all()

# public_id를 조호;하고 매칭되는 User 정보를 불러옴
def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

# User 데이터를 저장(업데이트)하는 함수
def save_changes(data):
    db.session.add(data)
    db.session.commit()
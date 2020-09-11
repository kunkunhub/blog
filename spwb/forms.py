from flask_wtf import FlaskForm
from wtforms import (
    Form,
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    InputRequired,
)

class LoginForm(Form):
    username = StringField(
        '用户名',
        validators=[
            DataRequired(), 
            Length(8, 128), 
            InputRequired()
        ]
    )
    password = PasswordField(
        '密码', 
        validators=[
            DataRequired(), 
            Length(8, 128), 
            InputRequired()
        ]
    )
    remember = BooleanField("记住我")
    submit = SubmitField("登录")
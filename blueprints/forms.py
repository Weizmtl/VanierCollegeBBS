import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel, EmailCaptchaModel
from exts import db


# Verify that the data submitted by the front-end meets the requirements
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Email format is incorrect!!")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="Captcha format is incorrect!!")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="Username format is incorrect!!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Password format is incorrect!!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # Whether the mailbox is registered
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="The email has been registered!!")

    # whether the captcha is matched
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="email or captcha is incorrect!!")
        # else:
        #     db.session.delete(captcha_model)
        #     db.session.commit()


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Email format is incorrect!!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Password format is incorrect!!")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=10, max=300, message="Title format is incorrect!!")])
    content = wtforms.StringField(validators=[Length(min=10, message="context format is incorrect!!")])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=10, message="context format is incorrect!!")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="have to input question_id")])

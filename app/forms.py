from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    IntegerField,
    StringField,
)
from wtforms.validators import NumberRange
from flask_wtf.file import (
    FileField,
    FileAllowed,
    FileRequired,
)


class ExamUploadForm(FlaskForm):
    subject = StringField('과목')
    professor = StringField('교수명')
    year = IntegerField('시험 년도', validators=(NumberRange(1990, 2017, '올바른 연도를 입력해 주세요'),))
    semester = SelectField('학기', choices=[('1', '1학기'), ('여름', '여름학기'), ('2', '2학기'), ('겨울', '겨울학기')])
    case = SelectField('고사', choices=[('중간', '중간고사'), ('기말', '기말고사')])

    valid_ext = ('jpg', 'jpeg', 'png', 'bmp') + ('pdf', 'doc', 'docx', 'hwp', 'txt') + ('zip', '7z')
    file_ = FileField('시험 자료', validators=(
        FileRequired('파일을 첨부해주세요'),
        FileAllowed(valid_ext, '올바른 확장자가 아닙니다'),
    ))

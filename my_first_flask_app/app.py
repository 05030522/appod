# 1. Flask 라이브러리에서 Flask 라는 클래스를 가져옵니다.
# 기존 코드
from flask import Flask, render_template, request, redirect, url_for, flash
# 새로 추가
from flask_sqlalchemy import SQLAlchemy

# 2. Flask 애플리케이션 객체를 생성합니다.
#    __name__은 현재 실행 중인 파이썬 모듈의 이름을 담고 있습니다.
#    Flask는 이 값을 보고 애플리케이션의 경로를 파악합니다.
app = Flask(__name__)
app.secret_key = 'my_super_secret_key' # 실제 서비스에서는 아무도 모르는 복잡한 값으로 해야 합니다!


# --- 데이터베이스 설정 추가 ---
# 1. 데이터베이스 경로(URI) 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# 2. SQLAlchemy 이벤트 처리 옵션 (지금은 그냥 끈다고 생각하세요)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 3. SQLAlchemy 객체 생성
db = SQLAlchemy(app)
# -----------------------------




# db = SQLAlchemy(app) 아래에 추가합니다.

# --- 데이터베이스 모델(테이블) 정의 ---
class Post(db.Model):
    # 각 속성(변수)은 테이블의 컬럼(열)에 해당합니다.
    
    # 1. id 컬럼: 각 게시글을 구분하는 고유한 번호
    # db.Integer: 정수 타입
    # primary_key=True: 이 컬럼을 기본 키(Primary Key)로 설정. 중복될 수 없는 고유한 값.
    id = db.Column(db.Integer, primary_key=True)

    # 2. title 컬럼: 게시글의 제목
    # db.String(80): 최대 80자까지 저장할 수 있는 문자열 타입
    # nullable=False: 이 값은 비어있을 수 없음 (반드시 제목이 있어야 함)
    title = db.Column(db.String(80), nullable=False)

    # 3. content 컬럼: 게시글의 내용
    # db.Text: 긴 텍스트를 저장할 수 있는 문자열 타입
    # nullable=False: 내용도 비어있을 수 없음
    content = db.Column(db.Text, nullable=False)

    # (선택) 객체를 출력할 때 어떻게 보일지 설정하는 함수 (디버깅에 유용)
    def __repr__(self):
        return f'<Post {self.id}: {self.title}>'
    
    


# 3. 라우팅(Routing): 특정 URL 경로에 실행할 함수를 연결합니다.
#    @app.route('/')는 사용자가 웹사이트의 기본 주소("/")에 접속했을 때,
#    바로 아래에 있는 함수를 실행하라는 의미입니다.
@app.route('/')
def index():
    # HTML로 전달할 데이터 생성
    my_name = "김진형"
    my_age = 20
    # render_template을 통해 'index.html'에 데이터 전달
    return render_template('index.html', name_in_html=my_name, age_in_html=my_age)

@app.route('/about') # /about 경로를 새로 만듭니다.
def about():
    return '이곳은 저희 웹사이트의 소개 페이지입니다. 반갑습니다!'
# ---------------------------------



@app.route('/user/<username>')
def show_user_profile(username):
    # 사용자 정보를 딕셔너리로 만들어 전달해봅시다.
    user_data = {
        'name': username,
        'email': f"{username}@example.com",
        'skills': ['Python', 'Flask', 'HTML']
    }
    return render_template('user_profile.html', user=user_data)



@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 터미널에 post_id의 타입을 직접 출력해봅니다.
    print(f"터미널에서 확인 >> post_id: {post_id}, 타입: {type(post_id)}")
    
    # 웹 브라우저에는 일단 타입 정보 없이 출력해봅니다.
    return f"터미널에서 확인 >> post_id: {post_id}, 타입: {type(post_id)}"



@app.route('/profile/<name>/<int:age>')
def show_profile(name, age): # 1. 콜론(:) 추가
    # 2. return 추가, 3. name과 age 변수를 HTML로 전달
    return render_template('profile.html', name=name, age=age) 



@app.route('/search')
def search_page():
    return render_template('search.html')
    


@app.route('/search-result')
def search_result_page():
    # 1. 사용자가 보낸 데이터 꺼내기
    # request.args는 GET 방식으로 전달된 데이터들을 담고 있는 딕셔너리입니다.
    # .get('query')는 그중에서 이름이 'query'인 값을 꺼내옵니다.
    search_keyword = request.args.get('query')

    # 2. 받은 데이터를 활용해서 페이지 내용 만들기
    if search_keyword: # 검색어가 있다면
        return f"<h1>'{search_keyword}'(으)로 검색한 결과입니다.</h1>"
    else: # 검색어가 없다면
        return "<h1>검색어를 입력하지 않으셨습니다.</h1>"



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        # flash('보여줄 메시지', '메시지 카테고리(선택사항)')
        flash(f'{username}님, 환영합니다! 로그인에 성공했습니다.', 'success') # 'success'는 나중에 CSS로 꾸밀 때 사용 가능
        return redirect(url_for('show_user_profile', username=username))
    else: # GET 요청일 경우
        return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)


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
    # Post 테이블의 모든 데이터를 조회해서 리스트로 가져옵니다.
    # order_by(Post.id.desc())는 id를 기준으로 내림차순(최신 글이 위로) 정렬하는 코드입니다.
    all_posts = Post.query.order_by(Post.id.desc()).all()
    
    # index.html 템플릿에 'posts'라는 이름으로 all_posts 리스트를 전달합니다.
    return render_template('index.html', posts=all_posts)

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


# 터미널에서 'flask init-db' 명령을 실행할 수 있도록 새로운 명령어 정의
@app.cli.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    db.create_all()
    print("Initialized the database.")


# post_id에 해당하는 글을 수정하는 경로
@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # 수정할 게시글을 데이터베이스에서 찾습니다.
    # .get_or_404()는 해당 id의 데이터가 없으면 404 Not Found 오류를 자동으로 보여줍니다.
    post_to_update = Post.query.get_or_404(post_id)

    if request.method == 'POST': # 수정 폼이 '제출'되었을 때 (POST 요청)
        post_to_update.title = request.form['title']
        post_to_update.content = request.form['content']
        
        db.session.commit() # 변경사항을 데이터베이스에 최종 저장
        
        flash('게시글이 성공적으로 수정되었습니다!', 'success')
        return redirect(url_for('index')) # 수정 후 홈페이지로 리다이렉트
    else: # 페이지에 처음 '접속'했을 때 (GET 요청)
        # 기존 게시글 내용을 담아서 수정 페이지를 보여줌
        return render_template('update.html', post=post_to_update)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    post_to_delete = Post.query.get_or_404(post_id) # 삭제할 게시글 찾기
    
    try:
        db.session.delete(post_to_delete) # 세션에서 삭제
        db.session.commit() # 데이터베이스에 최종 반영
        flash('게시글이 성공적으로 삭제되었습니다.', 'success')
        return redirect(url_for('index')) # 홈페이지로 리다이렉트
    except:
        flash('오류가 발생하여 삭제에 실패했습니다.', 'error')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


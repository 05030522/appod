# 1. Flask 라이브러리에서 Flask 라는 클래스를 가져옵니다.
from flask import Flask, render_template # render_template 추가

# 2. Flask 애플리케이션 객체를 생성합니다.
#    __name__은 현재 실행 중인 파이썬 모듈의 이름을 담고 있습니다.
#    Flask는 이 값을 보고 애플리케이션의 경로를 파악합니다.
app = Flask(__name__)

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
    


if __name__ == '__main__':
    app.run(debug=True)


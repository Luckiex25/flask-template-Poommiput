from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = 'Home Page'
  return render_template('index.html', title=title)

@app.route('/about')
def about():
  title = 'About Page'
  name='Luckiex'
  email = 'std.67122420305@ubru.ac.th'
  mobile = '0658321234'
  age = 20
  return render_template('about.html', title=title, name=name, email=email, mobile=mobile, age=age)

@app.route('/favorite/foods')
def favorite_foods():
  title = 'Favorite Foods Page'
  foods = ['หมูทอดกระเทียม', 'ข้าวผัด', 'ก๋วยเตี๋ยว', 'ผัดกระเพรา', 'ต้มยำกุ้ง']
  return render_template('favorite_foods.html', title=title, foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
  title = 'Favorite Sports Page'
  sports = ['ฟุตบอล', 'บาสเกตบอล', 'เทนนิส', 'ว่ายน้ำ', 'บาสเกตบอล']
  return render_template('favorite_sports.html', title=title, sports=sports)
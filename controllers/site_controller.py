from controllers.controller import Controller
from services.db import Db

class SiteController(Controller):
    
  def index(self, request, response):
    print(123)
    db = Db()
    items = db.query("SELECT * FROM 'articles'")
    print(items)
    response.text = self.view.render_html('site/index.html', {'title' : 'MVC фрейворк', 'h1' : 'Главная страницы'})

  def about (self, request, response):
    response.text = self.view.render_html('site/about.html', {'title' : 'MVC фрейворк', 'h1' : 'Страницы о нас'})

  def hello(self, request, response, user_name):
    response.text = self.view.render_html('site/hello.html', {'title' : 'MVC фрейворк', 'h1' : 'Приветствие', 'user' : user_name})
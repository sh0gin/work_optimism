from views.view import View

class SiteController:
  def __init__(self):
    self.layout = 'default'
    self.view = View(self.layout)
    
  def index(self, request, response):
    response.text = self.view.render_html('site/index.html', {'title' : 'MVC фрейворк', 'h1' : 'Главная страницы'})

  def about (self, request, response):
    response.text = self.view.render_html('site/about.html', {'title' : 'MVC фрейворк', 'h1' : 'Страницы о нас'})
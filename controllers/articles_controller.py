from controllers.controller import Controller

class ArticlesController(Controller):
    
  def index(self, request, response):
    articles = Artocticles.findAll()
    response.text = self.view.render_html('articles/test.html', {'title' : 'MVC фрейворк - статьи', 'h1' : 'Тестовая страницы'})
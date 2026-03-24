from views.view import View

class TestController:
  def __init__(self):
    self.layout = 'default'
    self.view = View(self.layout)
    
  def test(self, request, response):
    response.text = self.view.render_html('test/test.html', {'title' : 'MVC фрейворк 2 ', 'h1' : 'Тестовая страницы'})

  def action(self, request, response):
    response.text = self.view.render_html('test/action.html', {'title' : 'MVC фрейворк 2', 'h1' : 'Информация о действии'})
from controllers.controller import Controller

class TestController(Controller):
    
  def test(self, request, response):
    response.text = self.view.render_html('test/test.html', {'title' : 'MVC фрейворк 2 ', 'h1' : 'Тестовая страницы'})

  def action(self, request, response):
    response.text = self.view.render_html('test/action.html', {'title' : 'MVC фрейворк 2', 'h1' : 'Информация о действии'})
from controllers.controller import Controller
from models.article import Article


class ArticlesController(Controller):

    def index(self, request, response):
      articles = Article.findAll(Article)
      print(articles)
      response.text = self.view.render_html('articles/index.html', 
      {
        'title': 'MVC Framework -= Posts',
        'h1' : 'Posts',
        'articles' : articles
      })
    
    def view(self, request, response, id):
      article = Article.get_by_id(id, Article)
      print(Article)
      response.text = self.view.render_html('articles/view.html', 
      {
        'title': f'MVC Framework -= {article.name}',
        'h1' : f'Posts - {article.name}',
        'articles' : article
      })
      

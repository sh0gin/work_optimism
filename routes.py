from controllers.site_controller import SiteController
from controllers.test_controller import TestController
from controllers.articles_controller import ArticlesController

routes = {
    '/articles': [ArticlesController, ArticlesController.index],
    '/home': [SiteController, SiteController.index],
    '/about': [SiteController, SiteController.about],
    '/test-action': [TestController, TestController.action],
    '/test': [TestController, TestController.test],
    r"^/hello/(.*)$": [SiteController, SiteController.hello],
    # '/articles': articles,
}
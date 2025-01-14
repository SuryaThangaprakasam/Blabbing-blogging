from django.apps import AppConfig


class BlogSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_site'

    def ready(self):
        import blog_site.signals
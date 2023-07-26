

from .models import Category


# context_processor 
## Pode ser acessado por qualquer template desde que 
## Add no settings em TEMPLATES / context_processors 'category.context_processors.menu_links',
            
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
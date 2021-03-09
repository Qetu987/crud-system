from .models import News


# функция для очистки полей оценок и присвоения им значения 0
def clear():
    news = News.objects.all()
    for new in news:
        new.upvotes = '0'
        new.save()

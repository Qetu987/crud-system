from .models import News


def clear():
        """Функция для очистки оценок"""
    news = News.objects.all()
    for new in news:
        new.upvotes = "0"
        new.save()

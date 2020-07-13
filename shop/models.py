from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class ProductGroup(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    group = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Группа Продуктов'
        verbose_name_plural = 'Группа Продуктов'

    def __str__(self):
        return self.group


class Product(models.Model):
    parent = models.ForeignKey(ProductGroup, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=True, verbose_name=u"Название")
    price = models.CharField(max_length=25, blank=True, verbose_name=u"Цена")
    slug = models.SlugField(blank=True, verbose_name=u"Артикул")
    body = models.TextField(max_length=150, blank=True, verbose_name=u"Аннотация")
    drop_body = models.TextField(max_length=350, blank=True, verbose_name=u"Описание")
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


from django.db import models


class ClothModel(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    code = models.CharField(max_length=50, blank=False, null=True)
    type = models.ForeignKey('ClothType', on_delete=models.CASCADE, blank=True, null=True)
    suit = models.ForeignKey('Suit', on_delete=models.CASCADE, blank=True, null=True)
    sizes = models.ManyToManyField('Size', blank=True, related_name='sizes')
    width = models.SmallIntegerField(blank=True, null=True)
    textile = models.ForeignKey('Textile', on_delete=models.PROTECT, blank=True, null=True)
    dublerin_usage = models.TextField(max_length=1000, blank=True, null=True)
    flizerin_usage = models.TextField(max_length=1000, blank=True, null=True)
    # colors = models.ManyToManyField('Color', blank=True) not sure
    # lining = models.CharField(max_length=100, blank=True, null=True) not sure
    # twist = models.CharField(max_length=100, blank=True, null=True) not sure
    # actual_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(max_length=2000,blank=True, null=True)
    # furniture = models.CharField(max_length=100, blank=True, null=True)
    # processing = models.CharField(max_length=100, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cloth model'
        verbose_name_plural = 'Cloth models'
        ordering = ['-added']


class ClothType(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cloth type'
        verbose_name_plural = 'Cloth types'
        ordering = ['-added']


class Suit(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Suit'
        verbose_name_plural = 'Suits'
        ordering = ['-added']


class Size(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    is_lekala = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'
        ordering = ['-added']


class Textile(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Textile'
        verbose_name_plural = 'Textiles'
        ordering = ['-added']


# class Color(models.Model):
#     name = models.CharField(max_length=100, blank=False, null=True)
#     added = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Color'
#         verbose_name_plural = 'Colors'
#         ordering = ['-added']

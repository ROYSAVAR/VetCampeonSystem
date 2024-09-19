from django.db import models

class Product(models.Model):
    
    CATEGORY_CHOICES = [
        ('insecticidas', 'Insecticidas'),
        ('antibioticos', 'Antibióticos'),
        ('vitaminicos', 'Vitaminicos'),
        ('antiinflamatorios', 'Antiinflamatorios'),
        ('desparasitantes', 'Desparasitantes'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='insecticidas')

    def __str__(self):
        return self.name

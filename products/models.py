
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True, null=True)
    trade_mark = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.CharField(max_length=255)
    electronic_contact = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    TYPE_CHOICES = [
        ('electrical', 'Electrical'),
        ('electronic', 'Electronic'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    model_identifier = models.CharField(max_length=255)
    unique_product_identifier = models.CharField(max_length=255, unique=True)
    global_trade_identification_number = models.CharField(max_length=255, unique=True)
    taric_code = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    compliance_documentation = models.TextField()
    user_manuals = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DigitalProductPassport(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    passport_data = models.JSONField()
    data_carrier = models.CharField(max_length=255)
    version = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Passport for {self.product.name}"

class Importer(models.Model):
    name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True, null=True)
    trade_mark = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.CharField(max_length=255)
    electronic_contact = models.CharField(max_length=255)
    product = models.ManyToManyField(Product, related_name='importers')

    def __str__(self):
        return self.name

class Dealer(models.Model):
    name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True, null=True)
    trade_mark = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.CharField(max_length=255)
    electronic_contact = models.CharField(max_length=255)
    product = models.ManyToManyField(Product, related_name='dealers')

    def __str__(self):
        return self.name

class EnvironmentalData(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='environmental_data')
    carbon_footprint = models.DecimalField(max_digits=10, decimal_places=2, help_text='Carbon footprint in kg CO2e')
    energy_consumption = models.DecimalField(max_digits=10, decimal_places=2, help_text='Energy consumption in kWh')
    water_usage = models.DecimalField(max_digits=10, decimal_places=2, help_text='Water usage in liters')
    recyclability_score = models.DecimalField(max_digits=5, decimal_places=2, help_text='Recyclability score out of 100')
    lifespan = models.IntegerField(help_text='Expected lifespan in years')
    hazardous_materials = models.TextField(help_text='List of hazardous materials present', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Environmental Data for {self.product.name}"

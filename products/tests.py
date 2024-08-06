
from django.test import TestCase
from .models import Manufacturer, Product, DigitalProductPassport, Importer, Dealer, EnvironmentalData

class ProductModelTest(TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(
            name='Test Manufacturer',
            postal_address='123 Test St',
            electronic_contact='contact@test.com'
        )
        self.product = Product.objects.create(
            name='Test Product',
            type='electrical',
            model_identifier='TP123',
            unique_product_identifier='123456789',
            global_trade_identification_number='987654321',
            manufacturer=self.manufacturer,
            compliance_documentation='Test compliance docs',
            user_manuals='Test user manuals'
        )
        self.environmental_data = EnvironmentalData.objects.create(
            product=self.product,
            carbon_footprint=10.5,
            energy_consumption=100.2,
            water_usage=50.3,
            recyclability_score=85.5,
            lifespan=10
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.manufacturer.name, 'Test Manufacturer')
        self.assertEqual(self.product.environmental_data.carbon_footprint, 10.5)

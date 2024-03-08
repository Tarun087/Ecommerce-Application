import unittest
from unittest.mock import Mock
from dao.OrderProcessorRepository import OrderProcessorRepository
from dao.productsdao import ProductsDao
from dao.customersdao import CustomersDao



class TestOrderProcessorRepository(unittest.TestCase):
    def setUp(self):
        # Set up any necessary objects or mocks
        self.order_processor_repo = OrderProcessorRepository

    def test_create_product(self):
        # Mocking a product
        product = ProductsDao()

        # Mocking the repository's interaction with the database
        self.order_processor_repo.create_product = Mock(return_value=True)

        # Testing the create_product method
        result = self.order_processor_repo.create_product(product)

        self.assertTrue(result)

    def test_add_to_cart(self):

        customer = CustomersDao()
        product = ProductsDao()
        quantity = 3

        self.order_processor_repo.add_to_cart = Mock(return_value=True)
        result = self.order_processor_repo.add_to_cart(customer, product,quantity)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

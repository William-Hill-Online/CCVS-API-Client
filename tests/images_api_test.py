import unittest
from unittest.mock import MagicMock

from ccvs_scanning_api_client.api.images_api import ImagesApi


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs."""

    def setUp(self):
        self.mock = MagicMock()
        self.mock.make_request.return_value = 'Mock'
        self.api = ImagesApi(self.mock)

    def tearDown(self):
        pass

    def test_images_create(self):
        """Test case for images_create."""
        self.api.images_create('data')
        self.api.api_client.make_request.call_args(
            'POST',
            'container-scanning/images/',
            data='data',
            response_type='Image')

    def test_images_list(self):
        """Test case for images_list."""
        self.api.images_list()
        self.api.api_client.make_request.call_args(
            'GET',
            'container-scanning/images/',
            response_type='list[Image]')

    def test_vendors_search(self):
        """Test case for vendors_search."""
        params = {'name': 'name123'}
        self.api.images_search(name='name123')
        self.api.api_client.make_request.call_args(
            'GET',
            'container-scanning/images/',
            params=params,
            response_type='list[Vendor]')

    def test_images_read(self):
        """Test case for images_read."""
        self.api.images_read('abc123')
        self.api.api_client.make_request.call_args(
            'GET',
            'container-scanning/images/abc123',
            response_type='Image')

    def test_images_vendor_create(self):
        """Test case for images_vendor_create."""
        self.api.images_vendor_create('abc123', 'def456')
        self.api.api_client.make_request.call_args(
            'POST',
            'container-scanning/images/abc123/vendor/def456/',
            response_type='ImageVendor')

    def test_images_vendor_read(self):
        """Test case for images_vendor_read."""
        self.api.images_vendor_read('abc123', 'def456')
        self.api.api_client.make_request.call_args(
            'POST',
            'container-scanning/images/abc123/vendor/def456/',
            response_type='dict')

    def test_images_vendor_vuln_list(self):
        """Test case for images_vendor_vuln_list."""
        self.api.images_vendor_vuln_list('abc123', 'def456')
        self.api.api_client.make_request.call_args(
            'POST',
            'container-scanning/images/abc123/vendor/def456/vuln/',
            response_type='dict')


if __name__ == '__main__':
    unittest.main()

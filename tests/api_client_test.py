import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from ccvs_scanning_api_client.api_client import ApiClient
from ccvs_scanning_api_client.configuration import Configuration
from ccvs_scanning_api_client.exceptions import ApiException
from ccvs_scanning_api_client.models import Image
from ccvs_scanning_api_client.models import ImageVendor
from ccvs_scanning_api_client.models import Vendor


class TestApiClient(unittest.TestCase):
    """ApiClient unit test stubs."""

    def setUp(self):
        config = Configuration(host='http://localhost', token='token123')
        self.api = ApiClient(config)

    def tearDown(self):
        pass

    @patch('ccvs_scanning_api_client.api_client.request')
    def test_make_request_get_image(self, mock):
        """Test case for make_request_get_image."""
        image = {
            'id': 1,
            'name': 'name123'
        }
        image_obj = Image(id=1, name='name123')
        json = MagicMock(return_value=image)
        mock.return_value = MagicMock(json=json, status_code=200)
        response = self.api.make_request(
            'GET', 'container-scanning/images/', response_type='Image')

        mock.assert_called_with(
            'GET',
            'http://localhost/container-scanning/images/',
            data=None,
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer token123'},
            params=None
        )
        self.assertEqual(response, image_obj)

        mock.assert_called_with

    @patch('ccvs_scanning_api_client.api_client.request')
    def test_make_request_search_image(self, mock):
        """Test case for make_request_search_image."""
        image = {
            'id': 1,
            'name': 'name123'
        }
        image_obj = Image(id=1, name='name123')
        json = MagicMock(return_value=image)
        mock.return_value = MagicMock(json=json, status_code=200)
        response = self.api.make_request(
            'GET',
            'container-scanning/images/',
            params={'name': 'nameabc'},
            response_type='Image')

        mock.assert_called_with(
            'GET',
            'http://localhost/container-scanning/images/',
            data=None,
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer token123'},
            params={'name': 'nameabc'}
        )
        self.assertEqual(response, image_obj)

        mock.assert_called_with

    @patch('ccvs_scanning_api_client.api_client.request')
    def test_make_request_get_vendor(self, mock):
        """Test case for make_request_get_vendor."""
        vendor = {
            'id': 1,
            'name': 'name123',
            'credentials': {'config': {}}
        }
        vendor_obj = Vendor(**vendor)
        json = MagicMock(return_value=vendor)
        mock.return_value = MagicMock(json=json, status_code=200)
        response = self.api.make_request(
            'GET', 'container-scanning/vendors/', response_type='Vendor')

        mock.assert_called_with(
            'GET',
            'http://localhost/container-scanning/vendors/',
            data=None,
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer token123'},
            params=None
        )

        self.assertEqual(response, vendor_obj)

    @patch('ccvs_scanning_api_client.api_client.request')
    def test_make_request_error_500(self, mock):
        """Test case for make_request_error_500."""
        image_vendor = {
            'id': 1,
            'vendor': 456,
            'image': 123,
            'image_vendor_id': 'abc123'
        }
        ImageVendor(**image_vendor)
        json = MagicMock(return_value=image_vendor)
        mock.return_value = MagicMock(json=json, status_code=500, ok=False)

        with self.assertRaises(ApiException):
            self.api.make_request(
                'GET',
                'container-scanning/images/123/vendor/456/',
                response_type='ImageVendor')

            mock.assert_called_with(
                'GET',
                'http://localhost/container-scanning/images/123/vendor/456/',
                data=None,
                headers={'Content-Type': 'application/json',
                         'Authorization': 'Bearer token123'},
                params=None
            )


if __name__ == '__main__':
    unittest.main()

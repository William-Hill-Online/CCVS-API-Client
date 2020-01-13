import unittest
from unittest.mock import MagicMock

from ccvs_scanning_api_client.api.jobs_api import JobsApi


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs."""

    def setUp(self):
        self.mock = MagicMock()
        self.mock.make_request.return_value = 'Mock'
        self.api = JobsApi(self.mock)

    def tearDown(self):
        pass

    def test_jobs_create(self):
        """Test case for jobs_create."""
        self.api.jobs_create('data')
        self.api.api_client.make_request.call_args(
            'POST',
            'container-scanning/jobs/',
            data='data',
            response_type='Job')

    def test_jobs_read(self):
        """Test case for jobs_read."""
        self.api.jobs_read('abc123')
        self.api.api_client.make_request.call_args(
            'GET',
            'container-scanning/jobs/abc123',
            response_type='Job')


if __name__ == '__main__':
    unittest.main()

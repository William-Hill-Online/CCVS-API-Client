class JobsApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def jobs_create(self, data, **kwargs):
        """
        jobs_create.

        :param Job data: (required)
        :return: Job
        """
        path = f'container-scanning/jobs/'
        return self.api_client.make_request(
            'POST', path=path, data=data, response_type='Job')

    def jobs_read(self, job_id,  **kwargs):
        """
        jobs_read.

        :param str job_id: (required)
        :return: Image
        """
        path = f'container-scanning/jobs/{job_id}/'
        return self.api_client.make_request(
            'GET', path=path, response_type='Job')

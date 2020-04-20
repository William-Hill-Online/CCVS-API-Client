class AnalysisApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def analysis_create(self, image, **kwargs):
        """
        analysis_create.

        :param analysis image: (required)
        :return: analysis
        """
        path = f'container-scanning/analysis/'
        return self.api_client.make_request(
            'POST', path=path, image=image, response_type='Analysis')

    def analysis_read(self, analysis_id,  **kwargs):
        """
        analysis_read.

        :param str analysis_id: (required)
        :return: Image
        """
        path = f'container-scanning/analysis/{analysis_id}/'
        return self.api_client.make_request(
            'GET', path=path, response_type='Analysis')

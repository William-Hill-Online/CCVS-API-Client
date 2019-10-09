class ImagesApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def images_create(self, data, **kwargs):
        """
        images_create.

        :param Image data: (required)
        :return: Image
        """
        path = f'container-scanning/images/'
        return self.api_client.make_request(
            'POST', path=path, data=data, response_type='Image')

    def images_list(self, **kwargs):
        """
        images_list.

        :return: list[Image]
        """
        path = f'container-scanning/images/'
        return self.api_client.make_request(
            'GET', path=path, response_type='list[Image]')

    def images_search(self, name,  **kwargs):
        """
        images_search.

        :param str name: (required)
        :return: list[Image]
        """
        path = f'container-scanning/images/'
        params = {'name': name}
        return self.api_client.make_request(
            'GET', path=path, params=params, response_type='list[Image]')

    def images_read(self, image_id,  **kwargs):
        """
        images_read.

        :param str image_id: (required)
        :return: Image
        """
        path = f'container-scanning/images/{image_id}/'
        return self.api_client.make_request(
            'GET', path=path, response_type='Image')

    def images_vendor_create(self, image_id, vendor_id,  **kwargs):
        """
        images_read.

        :param str image_id: (required)
        :param str vendor_id: (required)
        :return: ImageVendor
        """
        path = f'container-scanning/images/{image_id}/vendor/{vendor_id}/'
        return self.api_client.make_request(
            'POST', path=path, response_type='ImageVendor')

    def images_vendor_read(self, image_id, vendor_id,  **kwargs):
        """
        images_read.

        :param str image_id: (required)
        :param str vendor_id: (required)
        :return: ImageVendor
        """
        path = f'container-scanning/images/{image_id}/vendor/{vendor_id}/'
        return self.api_client.make_request(
            'GET', path=path, response_type='dict')

    def images_vendor_vuln_list(self, image_id, vendor_id,  **kwargs):
        """
        images_vendor_vuln_list.

        :param str image_id: (required)
        :param str vendor_id: (required)
        :return: dict
        """
        path = f'container-scanning/images/{image_id}/vendor/{vendor_id}/vuln/'
        return self.api_client.make_request(
            'GET', path=path, response_type='dict')

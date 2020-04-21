# Copyright 2019 WHG (International) Limited. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import os
from time import sleep

from ccvs_scanning_api_client.api.analysis_api import AnalysisApi
from ccvs_scanning_api_client.api_client import ApiClient
from ccvs_scanning_api_client.configuration import Configuration
from ccvs_scanning_api_client.models.analysis import Analysis

CCVS_API = os.environ.get('CCVS_API')


def analysis(image_name):
    analysis_api = AnalysisApi(ApiClient(Configuration(host=CCVS_API)))
    analysis_obj = analysis_api.analysis_create(Analysis(image=image_name))
    x = 0
    while True:
        analysis_result = analysis_api.analysis_read(analysis_obj.id)
        if analysis_result.result == 'pending':
            b = 'Analysing image' + '.' * x
            print(b, end='\r')  # noqa
            x += 1
            sleep(5)
        else:
            print('Image Analysed')  # noqa
            break
    return analysis_result


def resume(analysis_result):
    vulns = analysis_result.vulnerabilities.values()
    resume = {
        'image': analysis_result.image,
        'link': f'{CCVS_API}container-scanning/analysis/{analysis_result.id}',
        'result': analysis_result.result,
        'total_vulns': {
            'high_vulns': 0,
            'medium_vulns': 0,
            'critical_vulns': 0,
            'low_vulns': 0,
            'unknown_vulns': 0,
            'negligible_vulns': 0
        }
    }

    for vuln in vulns:
        for level in vuln.items():
            resume['total_vulns'][level[0]] += len(level[1])

    return resume

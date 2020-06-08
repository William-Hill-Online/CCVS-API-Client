# Copyright 2019 WHG (International) Limited. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import argparse
import json

from ccvs_scanning_api_client.command import analysis


def main():
    parser = argparse.ArgumentParser(
        description='List vulnabilities from analysis id.')

    parser.add_argument(
        '-i', '--id',
        help='analysis id',
        dest='analysis_id',
        required=True)

    analysis_id = parser.parse_args().analysis_id
    results = analysis.get_analysis_result(analysis_id)

    print(json.dumps(results))  # noqa


if __name__ == '__main__':
    main()

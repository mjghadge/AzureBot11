#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "8cb66373-64bf-43ca-b013-51b11ea96990")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "66723377-faf8-46c7-9d50-1499075253ba")

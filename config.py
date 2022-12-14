#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "3254bd71-fdf0-4bb6-a068-60c88df45224")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "357583c6-437d-4173-95cd-14b01b146864")

# Copyright 2023 HEARTBEATS Corporation. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from main import app
import json

j = json.dumps(app.openapi())
print(j)

from main import app
import json

j = json.dumps(app.openapi())
print(j)

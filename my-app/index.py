import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

# Load student data from the JSON file once
with open("q-vercel-python.json", "r") as file:
    STUDENT_DATA = json.load(file)

# Handler class to process incoming requests
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)

        # Get 'name' parameters from the query string
        names = query.get("name", [])

        # Prepare the result dictionary
        result = {"marks": [entry["marks"] for entry in STUDENT_DATA if entry["name"] in names]}

        # Send the response header
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Enable CORS for any origin
        self.end_headers()

        # Send the JSON response
        response_body = json.dumps(result).encode("utf-8")
        self.wfile.write(response_body)

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json, datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        url = q.get("url", [""])[0]

        with open("/tmp/cliques.json", "a") as f:
            f.write(json.dumps({
                "url": url,
                "ts": datetime.datetime.utcnow().isoformat()
            }) + "\n")

        self.send_response(302)
        self.send_header("Location", url)
        self.end_headers()
add redirect api

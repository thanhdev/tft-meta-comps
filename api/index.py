import json
from http.server import BaseHTTPRequestHandler

from api.crawler import crawl_team_comps


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        data = crawl_team_comps()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        return

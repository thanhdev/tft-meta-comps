import json
from http.server import BaseHTTPRequestHandler
from time import time

from api.crawler import crawl_team_comps


data, last_update = crawl_team_comps(), time()


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        global data, last_update

        if last_update + 3600 < time():
            last_update = time()
            data = crawl_team_comps()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        return

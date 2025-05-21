from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random


class DiceHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        if self.path != '/roll':
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Not Found'}).encode())
            return

        content_length = int(self.headers.get('Content-Length', 0))
        raw_data = self.rfile.read(content_length)
        try:
            data = json.loads(raw_data)
            dice = int(data.get("dice"))
            sides = int(data.get("sides"))

            if dice <= 0 or sides <= 0:
                raise ValueError

            rolls = [random.randint(1, sides) for _ in range(dice)]
            total = sum(rolls)
            response = {'total': total, 'rolls': rolls}
            self._set_headers(200)
            self.wfile.write(json.dumps(response).encode())
        except (ValueError, TypeError, json.JSONDecodeError):
            self._set_headers(400)
            self.wfile.write(json.dumps({'error': 'Invalid input. Expected JSON: {"dice": int > 0, "sides": int > 0}'}).encode())


def run(server_class=HTTPServer, handler_class=DiceHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Dice microservice running at http://localhost:{port}/roll")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

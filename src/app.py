from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
from parking.parking import calcular_cobro

class ParkingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/cobro":
            params = parse_qs(parsed.query)
            minutos = int(params.get("minutos", [0])[0])
            vip = params.get("vip", ["false"])[0] == "true"
            resultado = calcular_cobro(minutos, vip)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"total": resultado}).encode())

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), ParkingHandler)
    server.serve_forever()
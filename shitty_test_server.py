#!/usr/bin/python3
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler


def main(port):
    SimpleHTTPRequestHandler.extensions_map[".wasm"] = "application/wasm"
    server = HTTPServer(("localhost", port), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000, help="port to bind to", required=False)
    args = parser.parse_args()
    main(args.port)

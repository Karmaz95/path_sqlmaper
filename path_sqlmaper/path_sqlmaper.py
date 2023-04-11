#!/usr/bin/env python3

from urllib.parse import urlparse
import sys

for url in sys.stdin:
    o = urlparse(url.strip())
    parts = o.path.split('/')
    if len(parts) > 1:
        for i in range(1, len(parts)):
            wildcard_path = '/'.join(parts[:i] + ['*'] + parts[i+1:])
            wildcard_url = o.scheme + '://' + o.netloc + wildcard_path
            print(wildcard_url)

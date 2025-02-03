from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests
from urllib.parse import urlparse
from django.core.cache import cache

def convert_into_app(request):
    return render(request, 'index.html')

def normalize_url(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc.lower().replace('www.', '')
    normalized = f"{parsed_url.scheme}://{netloc}{parsed_url.path.rstrip('/')}"
    return normalized

def fetch_content(request):
    if request.method == 'POST':
        url = request.POST.get('page_url', '')
        if url:
            validate = URLValidator()
            try:
                validate(url)
                normalized_url = normalize_url(url)
                cached_data = cache.get(normalized_url)
                if cached_data:
                    data = cached_data
                else:
                    data = requests.get(url).text
                    cache.set(normalized_url, data, timeout=3600) 
                return render(request, 'index.html', {'message': 'Valid URL. Proceeding...', 'url': url, 'data': data})
            except ValidationError:
                return render(request, 'index.html', {'error': 'Invalid URL. Please enter a valid one.', 'url': url})
    return redirect('index')
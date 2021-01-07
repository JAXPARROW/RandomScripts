import requests
from django.http import StreamingHttpResponse


def strem_file(request, *args, **kwargs):
    r = requests.get("http://host.com/file.txt", stream=True)

    response = StreamingHttpResponse(streaming_content=r.raw)

    # In case you want to force file download in a browser 
    # resp['Content-Disposition'] = 'attachment; filename="saving-file-name.txt"'

    return response
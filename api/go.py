def handler(request):
    url = request.args.get("url", "")
    return {
        "statusCode": 302,
        "headers": {
            "Location": url
        }
    }



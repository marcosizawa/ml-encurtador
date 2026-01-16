from urllib.parse import parse_qs
import json, datetime

def handler(request):
    qs = parse_qs(request.query_string.decode())
    url = qs.get("url", [""])[0]

    # log simples (opcional)
    try:
        with open("/tmp/cliques.log", "a") as f:
            f.write(json.dumps({
                "url": url,
                "ts": datetime.datetime.utcnow().isoformat()
            }) + "\n")
    except:
        pass

    return {
        "statusCode": 302,
        "headers": {
            "Location": url
        }
    }
fix vercel handler


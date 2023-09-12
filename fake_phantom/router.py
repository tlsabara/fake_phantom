from views import request_recived_repot


def route_get_urls(url_path: str) -> any:
    if str(url_path) == "/repport":
        return request_recived_repot()
    return False
from orm import queries
from jinja2 import Environment, FileSystemLoader, select_autoescape


def render_template_like_flask(template_namefile:str, jinja_vars:dict):
    environment = Environment(loader=FileSystemLoader("./templates/"), autoescape=select_autoescape(['html', 'xml']))
    template = environment.get_template(template_namefile)
    try:
        return template.render(
            **jinja_vars
        )  # .encode('utf-8')
    except Exception as e:
        print(e)
        # TODO: dmp error on log file
        return False


def request_recived_repot():
    requests_list = queries.collect_last_50_recived_requests()
    requests_list = [{
        'requests_recived_id': request_._asdict().pop("TbRequestsRecived").requests_recived_id,
        'requests_recived_route': request_._asdict().pop("TbRequestsRecived").requests_recived_route,
        'requests_recived_content': request_._asdict().pop("TbRequestsRecived").requests_recived_content,
        'requests_recived_timestamp': request_._asdict().pop("TbRequestsRecived").requests_recived_timestamp
    } for request_ in requests_list]
    template_vars = {"request_list": requests_list}
    return render_template_like_flask('request_recived_report.html', template_vars)

from datetime import datetime

from sqlalchemy import select

from fake_phantom.logs import fn_app_log
from fake_phantom.orm.models import Session, Base, engine, TbDefaultResponses, TbRequestsRecived


def collect_last_50_recived_requests():
    try:
        with Session() as db:
            rows = db.execute(select(
                TbRequestsRecived).order_by(
                TbRequestsRecived.requests_recived_timestamp.desc()
            ).limit(50)).all()
            db.close()
    except Exception as e:
        fn_app_log('Erro ao salvar no DB', str(e))
        return False
    else:
        return rows


def initialize_data():
    try:
        with Session() as db:
            Base.metadata.create_all(engine)
            inst_get = TbDefaultResponses(
                default_reponses_route="*",
                default_reponses_tag="def_GET_200",
                default_reponses_content='{"method": "GET","status_code": 200,"message": "Request recebida com sucesso"}',
                default_reponses_is_active=True,
            )
            inst_post = TbDefaultResponses(
                default_reponses_route="*",
                default_reponses_tag="def_POST_200",
                default_reponses_content='{"method": "POST","status_code": 200,"message": "Request recebida com sucesso"}',
                default_reponses_is_active=True,
            )
            inst_put = TbDefaultResponses(
                default_reponses_route="*",
                default_reponses_tag="def_PUT_200",
                default_reponses_content='{"method": "PUT","status_code": 200,"message": "Request recebida com sucesso"}',
                default_reponses_is_active=True,
            )
            db.add(inst_post)
            db.add(inst_put)
            db.add(inst_get)
            db.commit()
    except Exception as e:
        return False
    else:
        return True


def insert_request_data(path: str, recived_content: str) -> bool:
    try:
        with Session() as db:
            request_inst = TbRequestsRecived(
                requests_recived_route=path,
                requests_recived_content=recived_content,
                requests_recived_timestamp=datetime.now()
            )
            db.add(request_inst)
            db.commit()
            fn_app_log('Dados Salvos corretamente.')
    except Exception as e:
        fn_app_log('Erro ao salvar no DB', str(e))
        return False
    else:
        return True


def collect_response_data(where_tag=None, where_id=None) -> str:
    response = ""
    try:
        if where_id is not None and where_tag is None:
            with Session() as db:
                response = db.execute(
                    select(TbDefaultResponses).where(
                        TbDefaultResponses.default_reponses_id == where_id
                    )
                ).one()
            fn_app_log('Dados Localizados corretamente.(by ID)')
        elif where_tag is not None and where_id is None:
            with Session() as db:
                response = db.execute(
                    select(TbDefaultResponses).where(
                        TbDefaultResponses.default_reponses_tag == where_tag
                    )
                ).one()
            fn_app_log('Dados Localizados corretamente.(by TAG)')
        else:
            raise ValueError("Parâmetros inválidos.")
    except Exception as e:
        fn_app_log('Erro ao carregar dados do DB', str(e))
        return "{'message':'data not found.'}"
    else:
        return response[0].default_reponses_content

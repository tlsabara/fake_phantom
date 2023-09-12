import os
from datetime import datetime
from sqlalchemy import String, Boolean, Text, DateTime, create_engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ.get("DATABASE_URL_ENDPOINT"), echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)


class TbDefaultResponses(Base):
    __tablename__ = "tb_default_reponses"

    default_reponses_id: Mapped[int] = mapped_column(primary_key=True)
    default_reponses_route: Mapped[str] = mapped_column(String(2083))
    default_reponses_tag: Mapped[str] = mapped_column(String(100))
    default_reponses_content: Mapped[str] = mapped_column(Text())
    default_reponses_is_active: Mapped[bool] = mapped_column(Boolean())

    def __repr__(self) -> str:
        return f"DefaultResponses(id={self.default_reponses_id!r}, " \
               f"route={self.default_reponses_route!r}, " \
               f"tag={self.default_reponses_tag!r}, " \
               f"is_active={self.default_reponses_is_active!r})"


class TbRequestsRecived(Base):
    __tablename__ = "tb_requests_recived"

    requests_recived_id: Mapped[int] = mapped_column(primary_key=True)
    requests_recived_route: Mapped[str] = mapped_column(String(2083))
    requests_recived_content: Mapped[str] = mapped_column(Text())
    requests_recived_timestamp: Mapped[datetime] = mapped_column(DateTime())

    def __repr__(self):
        return f"TbRequestsRecived(id={self.requests_recived_id!r}, " \
               f"route={self.requests_recived_route!r}, " \
               f"timestamp={self.requests_recived_timestamp!r})"

# TODO: Comentado para evoluir postriormente.
# @mapper_registry.mapped
# class TbQueryLogs:
#     __tablename__ = "tb_query_logs"
#
#     query_logs_id: Mapped[int] = mapped_column(primary_key=True)
#     query_logs_datetime: Mapped[datetime] = mapped_column(DateTime())
#     query_logs_message: Mapped[str] = mapped_column(Text())
#
#     def __repr__(self):
#         return f"TbQueryLogs(id={self.query_logs_id!r}, " \
#                f"datetime={self.query_logs_datetime!r}, " \
#                f"message={self.query_logs_message!r})"
#

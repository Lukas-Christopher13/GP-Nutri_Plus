from datetime import datetime, timedelta
from typing import List

from ..models.consulta_model import Consulta
from ..repository.consulta_repository import ConsultaRepository


DATE_NUM = 5

class ConsultaService:
    days = DATE_NUM
    today = datetime.today()
    calendar_list = None
    consulta_repository = None

    def __init__(self, consulta_repository: ConsultaRepository) -> None:
        self.consulta_repository = consulta_repository
        self.calendar_list = self.get_calendar()
         
    def filter(self, type: str, date=None, days=None):
        if date is None:
            date = self.today
        
        if days is None:
            days = self.days

        if type == "next":
            self.get_next(days)

    def get_next(self, days):
        calendar_list: List[CalendarConsulta] = []

        for day in range(1, days + 1):
            date = self.today + timedelta(day)
            date = date.strftime("%Y-%m-%d")

            calendar = CalendarConsulta(self.consulta_repository, date)

            calendar_list.append(calendar)
        
        self.calendar_list = calendar_list
        

    def get_calendar(self) -> List:
        calendar_list: List[CalendarConsulta] = []

        for dia in range(self.days):
            date = self.today + timedelta(dia)
            date = date.strftime("%Y-%m-%d")

            calendar = CalendarConsulta(self.consulta_repository, date)

            calendar_list.append(calendar)
        
        return calendar_list


class  CalendarConsulta:
    date = None
    consulta_list: List[Consulta] = None

    def __init__(self, consulta_repository: ConsultaRepository, date) -> None:
        self.consulta_repository = consulta_repository

        self.date = date
        self.consulta_list = consulta_repository.get_all_by_date(date)
    
    def get_date(self):
        if self.date == datetime.today().strftime("%Y-%m-%d"):
            return "HOJE!"
        
        return self.date

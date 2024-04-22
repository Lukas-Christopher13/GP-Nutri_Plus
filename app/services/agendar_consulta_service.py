from datetime import datetime, timedelta
from typing import List

from ..models.consulta_model import Consulta
from ..repository.consulta_repository import ConsultaRepository

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

    @staticmethod
    def get_calendar(days: int, consulta_repository: ConsultaRepository) -> List:
        calendar_list: List[CalendarConsulta] = []

        for dia in range(days):
            date = datetime.today()
            date = date + timedelta(dia)
            date = date.strftime("%Y-%m-%d")

            calendar = CalendarConsulta(consulta_repository, date)

            calendar_list.append(calendar)
        
        return calendar_list
        

    



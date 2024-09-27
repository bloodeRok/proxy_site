import pandas as pd

from app.models import Request
from app.repositories import RequestRepository
from app.utils.constants.defaults import EXCEL_LOGS


class RequestService:
    repository = RequestRepository()

    async def add_requests_to_db(self) -> None:
        async with self.repository.session_maker() as session:
            await self.repository.delete_all(session=session)
            all_requests = []
            for log_path in EXCEL_LOGS:
                sheets = pd.read_excel(log_path, sheet_name=None)
                for sheet_name, df in sheets.items():
                    requests = []
                    for _, row in df.iterrows():
                        request_data = row.to_dict()
                        request = Request(
                            date=request_data["DAT"].date(),
                            inn=request_data["INN"],
                            nickname=request_data["OP"],
                            fio=request_data["FIO"],
                            office=request_data["DEPT"],
                            module=request_data["MODUL"],
                        )
                        requests.append(request)
                    all_requests.extend(requests)

            await self.repository.bulk_create(
                requests=all_requests,
                session=session
            )

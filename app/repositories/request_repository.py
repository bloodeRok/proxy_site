from datetime import datetime
from typing import Optional

from sqlalchemy import select, func, delete, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Request
from app.repositories.connection import DBConnection
from app.utils.plot.data_classes import PlotData


class RequestRepository:
    model = Request

    def __init__(self) -> None:
        self.session_maker = DBConnection().get_session

    async def create(
            self,
            date: datetime,
            inn: str,
            nickname: str,
            fio: bool,
            office: bool,
            module: bool,
            session: AsyncSession
    ) -> Request:
        created_request = self.model(
            date=date,
            inn=inn,
            nickname=nickname,
            fio=fio,
            office=office,
            module=module
        )

        session.add(created_request)
        await session.commit()
        await session.refresh(created_request)

        return created_request

    async def get_by_nickname(
            self,
            nickname: str,
            session: AsyncSession
    ) -> Optional[Request]:
        result = await session.execute(
            select(self.model).where(self.model.nickname == nickname)
        )
        return result.scalars().first()

    async def get_by_id(
            self,
            request_id: int,
            session: AsyncSession
    ) -> Optional[Request]:
        result = await session.execute(
            select(self.model).where(self.model.id == request_id)
        )
        return result.scalars().first()

    async def bulk_create(
            self,
            requests: list[Request],
            session: AsyncSession
    ) -> list[Request]:
        session.add_all(requests)
        await session.commit()
        for req in requests:
            await session.refresh(req)

        return requests

    async def get_avg_daily_requests(
            self,
            session: AsyncSession,
            office: Optional[str] = None
    ) -> PlotData:
        query = select(
            func.to_char(self.model.date, "YYYY-MM").label('formatted_date'),
            func.count(self.model.id).label('total_requests'),
            func.count(func.distinct(self.model.date)).label('unique_dates')
        ).group_by('formatted_date')

        offices_count = len(await self.get_unique_office(session=session))

        if office:
            query = query.where(self.model.office == office)
            offices_count = 1
        result = await session.execute(query)

        data = result.all()

        points = {
            row.formatted_date:
                int(row.total_requests / (row.unique_dates * offices_count))
                if row.unique_dates != 0 else 0
            for row in data
        }

        title = office
        if not title:
            title = "Среднее количество запросов"

        return PlotData(
            points=points,
            title=title
        )

    async def get_unique_office(self, session: AsyncSession) -> list[str]:
        offices = await session.execute(
            select(func.distinct(self.model.office))
        )
        return [office[0] for office in offices.all()]

    async def delete_all(self, session: AsyncSession) -> None:
        await session.execute(delete(self.model))
        await session.execute(
            text(
                f"ALTER SEQUENCE {self.model.__tablename__}"
                f"_id_seq RESTART WITH 1"
            )
        )
        await session.commit()

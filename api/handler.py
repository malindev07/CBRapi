from fastapi import APIRouter, Request, Response
from fastapi.params import Query


crb_router = APIRouter(tags=["CBR valute market"])


@crb_router.get("/scripts/XML_daily.asp", status_code=200, response_class=Response)
async def get_day_market(
    request: Request, date_req: str = Query(..., alias="date_req")
) -> Response:
    try:
        res = await request.state.validator.validate_date(date_req)
        if not res:
            raise ValueError
        return Response(
            content=await request.state.service.get_successful_xml(
                date_req=date_req, valutes=request.state.valutes_config.valutes
            ),
            media_type="application/xml",
        )
    except ValueError:
        return Response(
            content=await request.state.service.get_error_xml(),
            status_code=500,
            media_type="application/xml",
        )

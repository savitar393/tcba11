import json

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


def kategori_pm25(nilai: float) -> str:
    if nilai < 0:
        raise ValueError("PM2.5 tidak boleh negatif")
    if nilai <= 15.5:
        return "baik"
    if nilai <= 55.4:
        return "sedang"
    if nilai <= 150.4:
        return "tidak sehat"
    return "sangat tidak sehat"


@app.route(route="L0224047", methods=["GET"])
def kategori(req: func.HttpRequest) -> func.HttpResponse:
    nilai = req.params.get("pm25")
    if nilai is None:
        return func.HttpResponse("Parameter pm25 wajib, contoh: ?pm25=60", status_code=400)
    try:
        hasil = kategori_pm25(float(nilai))
    except ValueError as e:
        return func.HttpResponse(str(e), status_code=400)
    body = json.dumps({"pm25": float(nilai), "kategori": hasil})
    return func.HttpResponse(body, mimetype="application/json")

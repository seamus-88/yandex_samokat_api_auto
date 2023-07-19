import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def create_order(h, body):
    # Выполнить запрос на создание заказа.
    req = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body,
                        headers=h)
    assert req.status_code == 201
    return req

# Сохранить номер трека заказа.
def get_order_track_from_req(r):
    tr = r.json()["track"]
    assert isinstance(tr, int)
    return tr

# Выполнить запрос на получения заказа по треку заказа.
def get_order_info_by_track(track):
    req = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_NUMBER + str(track))
    assert req.status_code == 200, "Код ответа для просмотра информации по номеру трека по заказу не 200"
    return req
import data
import sender_stand_request

# Андрей Семенов 6 когорта - финальный проект, инженер по тестированию плюс

# тест создания заказа и получения информации по нему по номеру трека
def test_create_order():
    req = sender_stand_request.create_order(data.headers, data.order_body)
    track_number = sender_stand_request.get_order_track_from_req(req)
    sender_stand_request.get_order_info_by_track(track_number)
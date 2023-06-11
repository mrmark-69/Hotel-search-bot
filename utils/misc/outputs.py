from telebot import types
from all_requests.details import get_detail
from keyboards.inline.link import get_site


def output_without_photo(bot, selected, message):
    for hotel in selected:
        details = get_detail(hotel['id'])
        bot.send_message(message.chat.id,
                         f'<b>Отель: {hotel["name"]}\n'
                         f'Цена за ночь: {hotel["price"]}\n'
                         f'Стоимость проживания: {hotel["total_price"]}\n'
                         f'Адрес отеля: {details["address"]}\n'
                         f'Рейтинг отеля: {details["rating"]}\n'
                         f'Расстояние от центра: {hotel["distance_from"]} km</b>',
                         reply_markup=get_site(hotel['id']))


def output_with_photos(bot, selected, message, user):
    for hotel in selected:
        details = get_detail(hotel['id'])
        images = details['images']
        medias = ([types.InputMediaPhoto(image,
                                         caption=images[image])
                   for i, image in
                   enumerate(images) if i < int(user.photo_num)])
        bot.send_media_group(message.chat.id, medias)
        bot.send_message(message.chat.id,
                         f'<b>Отель: {hotel["name"]}\n'
                         f'Цена за ночь: {hotel["price"]}\n'
                         f'Стоимость проживания: {hotel["total_price"]}\n'
                         f'Адрес отеля: {details["address"]}\n'
                         f'Рейтинг отеля: {details["rating"]}\n'
                         f'Расстояние от центра: {hotel["distance_from"]} km</b>',
                         reply_markup=get_site(hotel['id']))

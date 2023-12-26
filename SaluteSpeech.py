import requests
import uuid
from paswords import autoriz_data
import os


def key_generate():
    url = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'

    headers = {
        'Authorization': f'Basic {autoriz_data}',
        'RqUID': str(uuid.uuid4()),
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'scope': 'SALUTE_SPEECH_PERS',
    }

    response = requests.post(url, headers=headers, data=data, verify=False)

    return response.json()['access_token']


async def save_audio(bot, message):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"{file_id}")
    url = 'https://smartspeech.sber.ru/rest/v1/speech:recognize'
    headers = {
        'Authorization': f'Bearer {key_generate()}',
        'Content-Type': 'audio/ogg;codecs=opus',
    }

    with open(f'{file_id}', 'rb') as audio_file:
        response = requests.post(url, headers=headers, data=audio_file, verify=False)
        try:
            await bot.send_message(message.chat.id, f'{" ".join(response.json()["result"])}')
            if response.json()["emotions"][0]['negative'] == max(response.json()["emotions"][0]['negative'],
                                                                 response.json()["emotions"][0]['neutral'],
                                                                 response.json()["emotions"][0]['positive']):
                await bot.send_message(message.chat.id, f'произнес как злая истеричная сучка')
            elif response.json()["emotions"][0]['positive'] == max(response.json()["emotions"][0]['negative'],
                                                                   response.json()["emotions"][0]['neutral'],
                                                                   response.json()["emotions"][0]['positive']):
                await bot.send_message(message.chat.id, f'произнес так жизнерадостно, что аж бесит')
            else:
                await bot.send_message(message.chat.id, f'произнес нормально, не докопаться')
        except Exception:
            await bot.send_message(message.chat.id, f'Ошибка. Логи:{response.json()}')
        audio_file.close()
        os.remove(f"{file_id}")
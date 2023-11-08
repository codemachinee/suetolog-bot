import g4f, asyncio, random

_providers = [
    g4f.Provider.GptGo,
    g4f.Provider.ChatBase,
    g4f.Provider.Llama2,
    g4f.Provider.GPTalk,
    g4f.Provider.ChatgptAi,
    g4f.Provider.AiAsk,
    g4f.Provider.Liaobots,
    g4f.Provider.GeekGpt
]


async def Artur():
    try:
        prompt_text = (f'На русском языке в сатирической форме поздравь с днем рождения Алексея '
                       f'Леха это стиль и харизма Востока. Леха любит когда все '
                       f'в этой жизни не дольше 4 минут. Леха любит все что '
                       f'горит и дымит. Новое хобби Алексея заключается в комментировании фильмов под пиво. '
                       f'Леха заботливо следит чтобы все '
                       f'напились как следует и очень расстраивается если кто'
                       f'то не пьет. Леха бывший успешный тиктокер и школьный '
                       f'диджей!')
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": f'{prompt_text}'}],
            provider=random.choice(_providers))
        print(f'{response}')
    except Exception:
        await Artur()


asyncio.run(Artur())
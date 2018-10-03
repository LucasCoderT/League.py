import asyncio

import league


async def myfunc():
    client = league.Client(api_key="RGAPI-aaad4ad8-f06b-4e1c-b04c-23a67234ec0e")
    summoner = await client.get_summoner(summoner_name="That Mellow Guy")
    match_history = await summoner.match_history()
    print(match_history)


if __name__ == '__main__':
    loop = asyncio.get_event_loop().run_until_complete(myfunc())

.. py:currentmodule:: league

Quickstart
============


This page gives a brief introduction to the library.


This library revolves around object orientated programming, meaning that instead of getting *raw* ``json``/``dict``
responses you will be getting ``objects``. This allows for a layer of abstraction between the Riot API and the end
developer.

Lets take a look:

How to get a Summoner
---------------------

.. code-block:: python3

    import league

    async def get_summoner():
        client = league.Client(api_key="token")
        mysummoner = await client.get_summoner(summoner_name="mysummonername")



    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(get_summoner())


Now this is a pretty basic example, but let's walk through it.

1. You have to `import` the library of course.
2. you have to use an ``async def`` type function in order to use ``await``.
3. You have to create a :class:`Client` instance using your api_key as a required parameter. As a note, you can create this instance anywhere in your code.
4. To find a summoner you will use the :meth:`Client.get_summoner` function.
5. Once you have a summoner object you can start get any other data you may need. see :class:`Summoner` sections for a list.


Regions
-------

By default if no region is specified to a function it will assume `NA`. This can be fixed by providing a
:class:`Regions` object to the function as seen below:

.. code-block:: python3

    await client.get_summoner(summoner_name="HideonBush",region=Regions.kr)

all functions allow for a region parameter.



Static Cache
------------

.. note::
    Ideally you would call this function before using any of this lib, but it can be loaded at any point.

To truly bring out the magic of this library you can load the cache of all the static data via
:meth:`Client.cache_setup` This will load all of the static data endpoints into a cache. Which allows the lib to link
what the api would normally return as ID's would be automatically turned into their respective objects.

example without cache:

.. code-block:: python3

    recent_matches = await summoner.recent_matches()
    for match in recent_matches:
        print(match.champion) # Prints out the champion ID


with cache:

.. code-block:: python3

    recent_matches = await summoner.recent_matches()
    for match in recent_matches:
        print(match.champion.lore) # Prints out that champions lore


.. note::
    Once you call this function and the cache is loaded, methods like :meth:`Client.get_item_by_id`
    will access the cache instead of calling the API. If you want to bypass the cache simply use ``ignore_cache=True``.
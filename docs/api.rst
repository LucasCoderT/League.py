.. py:currentmodule:: league

API Reference
=============

The following section outlines the API of league.py.


Version Related Info
====================
.. automodule:: league
    :members:


Client
======

.. note::

    All functions of Client are ``kwarg`` only.

    For example::

        wrong :
            await client.get_summoner("rofl",Regions.na)

        correct :
            await client.get_summoner(summoner_name="rofl", region=Regions.na)


.. autoclass:: Client()

    .. automethod:: cache_setup()
    .. automethod:: get_summoner()
    .. automethod:: get_match()
    .. automethod:: get_requests_statistics()
    .. automethod:: get_challenger()
    .. automethod:: get_champion_by_name()
    .. automethod:: get_champion_by_id()
    .. automethod:: get_all_champions()
    .. automethod:: get_all_maps()
    .. automethod:: get_all_masteries()
    .. automethod:: get_all_profile_icons()
    .. automethod:: get_all_items()
    .. automethod:: get_all_runes()
    .. automethod:: get_rune_by_id()
    .. automethod:: get_item_by_id()
    .. automethod:: get_item_by_name()
    .. automethod:: get_status()


Statistics
==========
.. autoclass:: Statistics()
    :members:

RiotDto
=======

``Added in 0.0.9a``

The parent class to all other objects.

The goal of this class is to allow easy scaffolding for important variables that should be in all objects.

.. autoclass:: RiotDto()
    :members:


League Models
=============

The following section outlines the Models for league.py

.. note::
    the data classes listed below are **not intended to be created by users**.


Summoner
--------
.. autoclass:: Summoner()

    .. automethod:: current_match()
    .. automethod:: ranked_data()
    .. automethod:: champion_masteries()
    .. automethod:: champion_mastery()
    .. automethod:: champion_mastery_score()
    .. automethod:: recent_matches()
    .. automethod:: leagues()
    .. automethod:: find_matches()


League
------
.. note::
    It is important to note that leagues can span entire tiers

.. autoclass:: League()
    :members:

LeagueEntry
-----------
.. autoclass:: LeagueEntry()
    :members:

Series
------
.. autoclass:: Series()
    :members:

ChampionMastery
---------------

.. autoclass:: ChampionMastery()
    :members:

Match
-----

.. autoclass:: Match()
    :members:

PartialMatch
------------

.. autoclass:: PartialMatch()
    :members:


Player
------
.. autoclass:: Player()
    :members:

TeamStats
---------
.. autoclass:: TeamStats()
    :members:

Participant
-----------
.. autoclass:: Participant()
    :members:

ParticipantStats
----------------
.. autoclass:: Participant()
    :members:

ParticipantTimeLine
-------------------
.. autoclass:: ParticipantTimeLine()
    :members:

LiveMatch
---------

.. autoclass:: LiveMatch()
    :members:

LiveMatchParticipant
--------------------

.. autoclass:: LiveMatchParticipant()
    :members:

Champion
--------
.. autoclass:: Champion()
    :members:

ChampionStats
-------------
.. autoclass:: ChampionStats()
    :members:


Rune
----

``As of the Rune's reforge update these no longer exist``

.. autoclass:: Rune()
    :members:

RunePage
--------

``As of the Rune's reforge update these no longer exist``

.. autoclass:: RunePage()
    :members:

MasteryPage
-----------

``As of the Rune's reforge update these no longer exist``

.. autoclass:: MasteryPage()
    :members:

Recommended
-----------
.. autoclass:: Recommended()
    :members:

Spell
-----
.. autoclass:: Spell()
    :members:


Item
----
.. autoclass:: Item()
    :members:

Image
-----
.. autoclass:: Image()
    :members:

Map
---
.. autoclass:: Map()
    :members:

SummonerMastery
---------------
.. autoclass:: SummonerMastery()
    :members:

Queue
-----
.. autoclass:: Queue()
    :members:


Exceptions
==========

The following exceptions are thrown by the library.

.. autoexception:: NoMatchFound
.. autoexception:: NoSummonerFound
.. autoexception:: UnAuthorized
.. autoexception:: BadRequest
.. autoexception:: EmptyResponse
.. autoexception:: RateLimited()
.. autoexception:: ServiceUnavailable
.. autoexception:: InvalidRegionType
.. autoexception:: InactivePlayer
"""
There is an official Pydantic module for this: pydantic_extra_types.country
The implementation is great, but the dependency used for the data 'pycountry' is not so great.
It is a very large dependency (30M!) and it is not actively maintained,
and not set up to update the ISO data from the Debian source automatically, so it is out of date.

We can do better, hopefully!
If this was a full-fledged library, we plan would be to use the Debian data directly,
and use CI to update the data and release new patch versions of the library when needed.
Most of the data (translations, etc) should be extras to greatly reduce the size of the library.

For now, this is just a snippet for learning purposes, maybe I'll work on a library for this later.
"""

# from pydantic_extra_types import country

# TODO: rest of the owl
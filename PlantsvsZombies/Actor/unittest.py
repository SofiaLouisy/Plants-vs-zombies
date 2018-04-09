"""Unit test for Actor.py
run with python3 -m pytest file.py

kolla upp nose, det är det assa använder!
"""

from PlantsvsZombies.Actor.Actor import *
import _io
import pytest
actor = Actor()

#TypeCheck

def test_get_position():
    """
    tests if the returned position is a tuple of length 2
    """
    assert type(actor.getPosition()) == tuple and len(actor.getPosition()) == 2
    
def test_graphics():    
    """
    test is the grfx attribute is of type string and that file exists
    """
    assert type(actor.grfx) == str and _io.TextIOWrapper == type(open(actor.grfx))

#KnownValues

def test_is_blocked():
    """
    tests if the actor isBlocked
    """
    assert actor.isBlocked(actor) == True

#BadInputCheck

def test_is_blocked_wrong_type():
    """
    test if the input in actor.isblocked raises expected error
    """
    with pytest.raises(TypeError):
        actor.isBlocked("k")

#SanityCheck


#CaseCheck
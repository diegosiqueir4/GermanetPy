from pathlib import Path
import sys
import logging
from lxml import etree as ET
import numpy as np
from germanet import Germanet

logger = logging.getLogger('logging_test_frames')
d = str(Path(__file__).parent.parent) + "/data"
try:
    germanet_data = Germanet(d)
except ET.ParseError:
    message = ("Unable to load GermaNet data at {0} . Aborting...").format(d)
    logger.error(message,
                 ET.ParseError)
    sys.exit(0)
except IOError:
    message = ("GermaNet data not found at {0} . Aborting...").format(d)
    logger.error(message, IOError)
    sys.exit(0)


def test_accusative_complements():
    acc_complements = germanet_data.frames.extract_accusative_complemtent()
    sehen = germanet_data.get_lexunit_by_id('l82290')
    np.testing.assert_equal(sehen in acc_complements, True)

def test_dative_complements():
    dative_complements = germanet_data.frames.extract_dative_complement()
    print(dative_complements)
    print(type(dative_complements))
    schenken = germanet_data.get_lexunit_by_id('l73802')
    np.testing.assert_equal(schenken in dative_complements, True)

def test_genitive_complements():
    genitive_complements = germanet_data.frames.extract_gentive_complement()
    berauben = germanet_data.get_lexunit_by_id('l74138')
    np.testing.assert_equal(berauben in genitive_complements, True)

def test_praepositional_complements():
    praep_complements = germanet_data.frames.extract_prepositional_complement()
    klacken = germanet_data.get_lexunit_by_id('l82560')
    print(klacken.examples)
    np.testing.assert_equal(klacken in praep_complements, True)

def test_adverbial_complements():
    adverbials = germanet_data.frames.extract_adverbials()
    wohnen  = germanet_data.get_lexunit_by_id('l73312')
    kommen = germanet_data.get_lexunit_by_id('l73778')
    np.testing.assert_equal(wohnen in adverbials, True)
    np.testing.assert_equal(kommen in adverbials, True)

def test_expletives():
    expletives = germanet_data.frames.extract_expletives()
    regnen = germanet_data.get_lexunit_by_id('l82091')
    print(regnen.examples)
    np.testing.assert_equal(regnen in expletives, True)

def test_transitives():
    transitives = germanet_data.frames.extract_transitives()
    backen = germanet_data.get_lexunit_by_id('l84453')
    np.testing.assert_equal(backen in transitives, True)

def test_intransitives():
    intransitives = germanet_data.frames.extract_intransitives()
    liegen = germanet_data.get_lexunit_by_id('l80908')
    np.testing.assert_equal(liegen in intransitives, True)



def test_reflexives():
    reflexives = germanet_data.frames.extract_reflexives()
    raechen = germanet_data.get_lexunit_by_id('l76169')
    np.testing.assert_equal(raechen in reflexives, True)
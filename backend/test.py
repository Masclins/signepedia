import unittest

testmodules = [
    "test.test_cercador",
    "test.test_corrector",
    "test.test_diccionari",
    "test.test_signepedia",
    "test.test_sinonims"
    ]

suite = unittest.TestSuite()

for t in testmodules:
    try:
        mod = __import__(t, globals(), locals(), ["suite"])
        suitefn = getattr(mod, "suite")
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)

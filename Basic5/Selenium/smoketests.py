from unittest import TestLoader , TestSuite
from pyunitreport import HTMLTestRunner
from AssertionsTest import Assertions_test
from SearchTests import SearchTest

assertion_test = TestLoader().loadTestsFromTestCase(Assertions_test)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertion_test,search_test])

kwarg = {
    "output" : "smoke-report"
}

runner = HTMLTestRunner(**kwarg)
runner.run(smoke_test)
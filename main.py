import unittest
from HTMLTestRunner import HTMLTestRunner

test_suite = unittest.TestLoader().discover('.')

runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                        open_in_browser=True, description="HTMLTestReport")
runner.run(test_suite)

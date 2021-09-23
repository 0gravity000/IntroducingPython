# content of test_class_demo.py
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

# pytest -k TestClassDemoInstance -q
'''
.F                                                                                                            [100%]
===================================================== FAILURES =====================================================
__________________________________________ TestClassDemoInstance.test_two __________________________________________

self = <test_class_demo.TestClassDemoInstance object at 0x000001BE6FC95730>

    def test_two(self):
>       assert self.value == 1
E       assert 0 == 1
E        +  where 0 = <test_class_demo.TestClassDemoInstance object at 0x000001BE6FC95730>.value

test_class_demo.py:10: AssertionError
================================================= warnings summary =================================================
test_sample.py:11
  C:\as\v2\010_prg\040_python\IntroducingPython\pytest_documantation\01\test_sample.py:11: DeprecationWarning: invalid escape sequence \I

-- Docs: https://docs.pytest.org/en/stable/warnings.html
============================================= short test summary info ==============================================
FAILED test_class_demo.py::TestClassDemoInstance::test_two - assert 0 == 1
1 failed, 1 passed, 4 deselected, 1 warning in 0.32s

クラスレベルで追加された属性はクラス属性であるため、テスト間で共有されることに注意してください。

'''
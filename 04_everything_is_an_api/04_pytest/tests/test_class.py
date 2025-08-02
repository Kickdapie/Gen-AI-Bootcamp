# content of test_class.py
class HasCheck:
    def check(self):
        return True

class TestClass:
    def test_one(self):
        x = "this"
        assert "t" in x

    def test_two(self):
        x = HasCheck()
        assert hasattr(x, "check")
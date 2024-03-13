import pytest 
from source import shapes
import math
class TestCircle:
    def setup_method(self, method):
        # 这里的 method 参数是必要的，因为它是 setup_method 的一部分
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    
    def teardown_method(self, method):
        # 如果你需要在测试后清理，也可以定义 teardown_method
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2


    def test_perimeter(self):
        result = self.circle.perimeter()
        expectec = 2 * math.pi * self.circle.radius
        assert result ==expectec
    
    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() !=  my_rectangle.area()
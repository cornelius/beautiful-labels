import pytest

from color_range import ColorRange, hex_to_rgb, rgb_to_hex

def test_to_rgb():
    assert hex_to_rgb("000000") == [0,0,0]
    assert hex_to_rgb("ffffff") == [255,255,255]
    assert hex_to_rgb("0700ab") == [7,0,171]

def test_rgb_to_hex():
    assert rgb_to_hex([0,0,0]) == "000000"
    assert rgb_to_hex([255,255,255]) == "ffffff"
    assert rgb_to_hex([17,0,120]) == "110078"
    with pytest.raises(RuntimeError) as e:
        rgb_to_hex([256,0,0])
        assert "illegal" in e.value

def test_range_test():
    cr = ColorRange("test")
    assert cr.color_range(0, 3) == "1/3"
    assert cr.color_range(3, 4) == "4/4"

def test_range_unknown():
    with pytest.raises(RuntimeError) as e:
        ColorRange("xxx")
        assert e.value == "Unkown range 'xxx'"

def test_range_blue():
    cr = ColorRange("blue")
    assert cr.color_range(0, 3) == "3382fe"
    assert cr.color_range(3, 5) == "84b3fe"

def test_valid_ranges():
    for r in ("blue", "green", "rainbow"):
      assert ColorRange(r)

from function_app import kategori_pm25


def test_kategori():
    assert kategori_pm25(10) == "baik"
    assert kategori_pm25(40) == "sedang"
    assert kategori_pm25(100) == "tidak sehat"
    assert kategori_pm25(200) == "sangat tidak sehat"

from city_functions import city_country


def test_city_country():
    """Unit test for city_country function"""
    message = city_country("Santiago", "Chile")
    assert message == "Santiago, Chile"


def test_city_country_population():
    """Unit test for city_country function with optional population"""
    message = city_country("Santiago", "Chile", 5000000)
    assert message == "Santiago, Chile - population 5000000"

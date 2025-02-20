def city_country(city, country, population=""):
    """Generate formatted City, Country with optional population"""
    if population:
        message = f"{city}, {country} - population {population}"
    else:
        message = f"{city}, {country}"
    return message

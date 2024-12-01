def city_country(city, country,population =None, language=None):
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"


print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France", 6000000))
print(city_country("Tokyo", "Japan", 5000000, "Japanese"))

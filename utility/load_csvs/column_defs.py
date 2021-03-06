def col_dtype_dict():
    """
    return a dict that maps col names to correct data type 
    """
    dtype_dict = {
        
        "age": "int4range",
        "ageRange": "VARCHAR(255)",
        "count": "INTEGER",
        "disabilityType": "VARCHAR(255)",
        "ethnicity": "VARCHAR(255)",
        "geographicLocation": "VARCHAR(255) NOT NULL",
        "gender": "VARCHAR(255) NOT NULL",
        "householdType": "VARCHAR(255) NOT NULL",
        "page": "INTEGER",
        "shelterType": "VARCHAR(255) NOT NULL",
        "veteran": "VARCHAR(255)",
        "year": "INTEGER",        
        
    }

    return dtype_dict

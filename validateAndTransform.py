def validate_and_transform(document):
    # Example: Convert MongoDB boolean to SQL integer
    if 'is_active' in document:
        document['is_active'] = 1 if document['is_active'] else 0

    # Example: Validate and truncate string length
    if 'name' in document:
        max_length = 50  # Example maximum length in SQL
        if len(document['name']) > max_length:
            document['name'] = document['name'][:max_length]

    # Example: Convert date format
    if 'created_at' in document:
        # Convert from MongoDB date format to SQL date format
        document['created_at'] = document['created_at'].strftime('%Y-%m-%d %H:%M:%S')

    # Example: Numeric range validation
    if 'age' in document:
        min_age = 18  # Example minimum age in SQL
        max_age = 100  # Example maximum age in SQL
        if not min_age <= document['age'] <= max_age:
            raise ValueError('Age out of range')

    # Additional validations and transformations as needed

# Iterate over MongoDB data
#----------------------------------------------------------------------
# for document in mongo_collection.find():
#     validate_and_transform(document)
#----------------------------------------------------------------------
    # Insert or update document in SQL database
    # (implementation depends on your SQL library)


type_mapping = {
    'int': 'INT',
    'str': 'NVARCHAR(MAX)',
    'float': 'FLOAT',
    # Add more mappings as needed
}


def validate_data(document):
    for key, value in document.items():
        # Get MSSQL data type for the field from mapping
        mssql_data_type = type_mapping.get(type(value).__name__)
        if mssql_data_type:
            # Check if the field complies with MSSQL data type and constraints
            # Perform appropriate validation or transformation here
            pass
        else:
            # Log or handle cases where the data type is not mapped
            pass

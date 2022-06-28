GET_ANIMAL_ID_SHORT_QUERY = """
    SELECT * FROM new_animals
    WHERE animal_id = :1;
"""
GET_ANIMAL_ID_FULL_QUERY = """
    SELECT
        new_animals.id,
        age_upon_outcome,
        animal_id,
        new_animals.name,
        date_of_birth,
        outcome_month,
        outcome_year,
        animal_type.name as 'type',
        animal_breed.name as 'breed',
        animal.color.name as 'color',
        outcome_subtype.name as 'outcome_subtype',
        outcome_type.name as 'outcome_type',
    FROM new_animals
    LEFT JOIN animal_type
        ON animal_type.id = new_animals.type_id
    LEFT JOIN animal_breed
        ON animal_breed.id = new_animals.breed_id
    LEFT JOIN animal_color as animal.color1
        ON animal_color.id = new_animals.color_id
    LEFT JOIN outcome_subtype
        ON outcome_subtype.id = new_animals.outcome_subtype_id
    LEFT JOIN outcome_type
        ON outcome_type.id = new_animals.outcome_type_id
    WHERE new_animals.animal_id = :1
"""

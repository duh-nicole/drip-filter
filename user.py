class User:
    """
    A class to represent a user with multiple attributes
    """

    def __init__(self, user_id, first_name, last_name, age, city, phone_number):
        """
        Creates new User object
        """
        self._id = user_id
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._city = city
        self._phone_number = phone_number

    # --- OOP Matching Methods ---
    def matches_range(self, attribute_key, min_val, max_val):
        """Checks if a numerical attribute falls within a specific range."""
        value = getattr(self, attribute_key)
        return min_val <= value <= max_val

    def matches_string(self, attribute_key, search_term, partial=False):
        """Checks if a string attribute matches or contains a search term."""
        value = str(getattr(self, attribute_key)).lower()
        search_term = search_term.lower()
        
        if partial:
            return search_term in value
        return value == search_term

    # --- Data Handling ---
    def to_dict(self):
        """Converts object back to dictionary for JSON saving."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'city': self.city,
            'phone_number': self.phone_number
        }

    # --- Getters (Properties) ---
    @property
    def id(self): 
        return self._id

    @property
    def first_name(self): 
        return self._first_name

    @property
    def last_name(self): 
        return self._last_name

    @property
    def age(self): 
        return self._age

    @property
    def city(self): 
        return self._city

    @property
    def phone_number(self): 
        return self._phone_number

    def __str__(self):
        return (f"User ID: {self.id}\n"
                f"{self.first_name} {self.last_name}\n"
                f"{self.city}\n"
                f"Age: {self.age}\n"
                f"Phone: {self.phone_number}")

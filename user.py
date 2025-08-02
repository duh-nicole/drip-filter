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

    # Getters
    @property
    def id(self):
        """Gets the user's ID."""
        return self._id

    @property
    def first_name(self):
        """Gets the user's first name."""
        return self._first_name

    @property
    def last_name(self):
        """Gets the user's last name."""
        return self._last_name

    @property
    def age(self):
        """Gets the user's age."""
        return self._age

    @property
    def city(self):
        """Gets the user's city."""
        return self._city

    @property
    def phone_number(self):
        """Gets the user's phone number."""
        return self._phone_number

    # Setters
    @id.setter
    def id(self, value):
        """Sets the user's ID."""
        self._id = value

    @first_name.setter
    def first_name(self, value):
        """Sets the user's first name."""
        self._first_name = value

    @last_name.setter
    def last_name(self, value):
        """Sets the user's last name."""
        self._last_name = value

    @age.setter
    def age(self, value):
        """Sets the user's age."""
        self._age = value

    @city.setter
    def city(self, value):
        """Sets the user's city."""
        self._city = value

    @phone_number.setter
    def phone_number(self, value):
        """Sets the user's phone number."""
        self._phone_number = value

    def __str__(self):
        """
        Overrides the default string to prettier display
        """
        return (f"User ID: {self.id}\n"
                f"{self.first_name} {self.last_name}\n"
                f"{self.city}\n"
                f"{self.age}\n"
                f"{self.phone_number}")

    def in_range(self, min_val, max_val):
        """
        Verifies age is in specified range
        """
        return min_val <= self.age <= max_val

    def to_dict(self):
        """
        Converts object into dictionary
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'city': self.city,
            'phone_number': self.phone_number
        }

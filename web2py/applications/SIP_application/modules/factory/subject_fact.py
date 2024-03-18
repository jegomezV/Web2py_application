class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SubjectFactory(metaclass=Singleton):
    """
    A factory class for creating materias.

    Attributes:
        db: A database connection object.
    """
    _cache = {}

    def create_subject(self, name: str, description: str) -> Dict[str, str]:
        """
        The function to create a materia.

        Parameters:
            name (str): The name of the materia.
            description (str): The description of the materia.

        Returns:
            dict: A dictionary containing the name and description of the materia.
        """
        # Here you can add any additional logic you need for creating a materia
        if name not in self._cache:
            self._cache[name] = {"name": name, "description": description}
        return self._cache[name]

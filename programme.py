class Programme:
    """Represents a university programme with its cut-off point."""
    
    def __init__(self, name, cutoff_point):
        """Initializes a new Programme object.
        
        Args:
            name (str): The name of the programme.
            cutoff_point (int/float): The minimum aggregate score required for admission.
        """
        self.name = name
        self.cutoff_point = cutoff_point
    
    def to_dict(self):
        """Converts the Programme object to a dictionary for JSON serialization.
        
        Returns:
            dict: A dictionary representation of the programme.
        """
        return {
            "name": self.name,
            "cutoff_point": self.cutoff_point
        }
    
    @classmethod
    def from_dict(cls, data):
        """Creates a Programme object from a dictionary.
        
        Args:
            data (dict): A dictionary containing 'name' and 'cutoff_point' keys.
            
        Returns:
            Programme: A Programme object created from the dictionary.
        """
        return cls(data["name"], data["cutoff_point"])
    
    def __str__(self):
        """Returns a string representation of the programme."""
        return f"{self.name} (Cut-off: {self.cutoff_point})"
    
    def __repr__(self):
        """Returns a developer-friendly string representation."""
        return f"Programme(name='{self.name}', cutoff_point={self.cutoff_point})"

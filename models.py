from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str

@dataclass
class Location:
    id: int
    state: str
    wp_term_id: int

@dataclass
class CategoryAge:
    id: int
    category: str
    wp_term_id: int

@dataclass
class PhysicalSize:
    id: int
    size: str
    wp_term_id: int

@dataclass
class Pet:
    id: int
    name: str
    age: int
    adopted: bool
    specie: str
    user: User
    location: Location
    category_age: CategoryAge
    physical_size: PhysicalSize

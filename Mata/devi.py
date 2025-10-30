import json
from datetime import datetime

class PersonalizedDasaraWishes:
    def __init__(self):
        self.templates = [
            "Dear {name}, {wish} May this Dasara bring you {blessing}.",
            "Hello {name}! {wish} Wishing you {blessing} on this auspicious occasion.",
            "To {name} and family, {wish} May Goddess Durga bless you with {blessing}.",
            "Happy Dasara {name}! {wish} May you be blessed with {blessing}."
        ]
        
        self.blessings = [
            "prosperity, happiness, and good health",
            "success in all your endeavors",
            "peace, joy, and spiritual growth",
            "strength to overcome all challenges",
            "abundance and fulfillment in life",
            "divine protection and guidance"
        ]
    
    def generate_personalized_wish(self, name, language='english', region=None):
        """Generate personalized Dasara wish"""
        base_wishes = DasaraWishes()
        wish_text = base_wishes.get_wish(language)
        template = random.choice(self.templates)
        blessing = random.choice(self.blessings)
        
        personalized_wish = template.format(
            name=name,
            wish=wish_text,
            blessing=blessing
        )
        
        return personalized_wish
    
    def generate_bulk_wishes(self, contacts):
        """Generate wishes for multiple contacts"""
        wishes_list = []
        for contact in contacts:
            wish = self.generate_personalized_wish(
                contact['name'],
                contact.get('language', 'english'),
                contact.get('region')
            )
            wishes_list.append({
                'to': contact['name'],
                'wish': wish,
                'language': contact.get('language', 'english')
            })
        return wishes_list

# Usage examples
personalized = PersonalizedDasaraWishes()

# Single personalized wish
print(personalized.generate_personalized_wish("Rahul", "hindi"))

# Bulk wishes for contacts
contacts = [
    {'name': 'Priya', 'language': 'tamil'},
    {'name': 'Amit', 'language': 'hindi'},
    {'name': 'Sneha', 'language': 'kannada'},
    {'name': 'Raj', 'language': 'english'}
]

print("\nBulk Dasara Wishes:")
for wish in personalized.generate_bulk_wishes(contacts):
    print(f"\nTo: {wish['to']}")
    print(f"Language: {wish['language'].capitalize()}")
    print(f"Wish: {wish['wish']}")
class DasaraGreetingSystem:
    def __init__(self):
        self.wish_generator = DasaraWishes()
        self.cultural_generator = CulturalDasaraWishes()
        self.personalized_generator = PersonalizedDasaraWishes()
        
    def create_complete_greeting(self, name=None, preferred_language='english', region='all'):
        """Create a complete Dasara greeting with multiple elements"""
        greeting = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'festival': 'Dasara/Vijayadashami',
            'significance': 'Celebration of victory of good over evil',
        }
        
        # Add personalized wish if name is provided
        if name:
            greeting['personalized_wish'] = self.personalized_generator.generate_personalized_wish(
                name, preferred_language, region
            )
        else:
            greeting['general_wish'] = self.wish_generator.get_wish(preferred_language)
        
        # Add cultural context
        greeting['cultural_note'] = self.cultural_generator.get_regional_wish(region)
        
        # Add multilingual greeting
        greeting['multilingual_greetings'] = self.wish_generator.get_multilingual_wishes(2)
        
        return greeting
    
    def print_greeting_card(self, name=None, language='english', region='all'):
        """Print a formatted greeting card"""
        greeting = self.create_complete_greeting(name, language, region)
        
        print("🎊" * 50)
        print("✨" + " DASARA FESTIVAL GREETINGS ".center(48) + "✨")
        print("🎊" * 50)
        print()
        
        if name:
            print(f"Dear {name},")
            print()
        
        if 'personalized_wish' in greeting:
            print(greeting['personalized_wish'])
        else:
            print(greeting['general_wish'])
        
        print()
        print("Cultural Context:")
        print(f"📖 {greeting['cultural_note']}")
        print()
        
        print("Multilingual Greetings:")
        for lang_wish in greeting['multilingual_greetings']:
            print(f"🌍 {lang_wish['language']}: {lang_wish['wish']}")
        
        print()
        print("🎯 Significance:", greeting['significance'])
        print("📅 Generated on:", greeting['timestamp'])
        print()
        print("🎉" + " MAY GOOD ALWAYS TRIUMPH OVER EVIL ".center(48) + "🎉")
        print("🎊" * 50)

# Final Usage
greeting_system = DasaraGreetingSystem()

# Generate greeting card
greeting_system.print_greeting_card("Family", "english", "all")

# Generate for specific person
print("\n" + "="*60 + "\n")
greeting_system.print_greeting_card("Sunita", "hindi", "north_india")
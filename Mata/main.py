import time
import random
import sys

def animated_dasara_greeting():
    """Animated Dasara greeting in terminal"""
    messages = [
        "जय माँ दुर्गा",
        "Happy Dasara",
        "शुभ दशहरा",
        "Victory of Good over Evil",
        "जय जय माँ दुर्गा"
    ]
    
    symbols = "✨🪷🙏🕉️🌟💫🔥🎇🦁⚔️🛡️👑"
    
    print("\n" * 2)
    print(" " * 10 + "🚀 Starting Dasara Celebration...")
    time.sleep(1)
    
    for i in range(20):
        sys.stdout.write('\r' + ' ' * 50)
        sys.stdout.flush()
        
        # Create random pattern
        pattern = ''.join(random.choice(symbols + " ") for _ in range(40))
        message = random.choice(messages)
        
        sys.stdout.write(f'\r{pattern} {message} {pattern}')
        sys.stdout.flush()
        time.sleep(0.3)
    
    print("\n" * 2)
    final_message = "🎊 DASARA FESTIVAL GREETINGS 🎊"
    print(" " * ((80 - len(final_message)) // 2) + final_message)
    
    blessings = [
        "May Maa Durga bless you with:",
        "• Strength and Courage",
        "• Prosperity and Wealth", 
        "• Health and Happiness",
        "• Spiritual Growth",
        "• Victory over Evil"
    ]
    
    for blessing in blessings:
        print(" " * 20 + blessing)
        time.sleep(0.5)

# Run animated greeting
animated_dasara_greeting()
import random
from datetime import datetime

class DasaraWishes:
    def __init__(self):
        self.wishes = {
            'hindi': [
                "आप सभी को दशहरे की हार्दिक शुभकामनाएं! माँ दुर्गा आप पर अपनी कृपा बनाए रखें।",
                "विजयादशमी के पावन अवसर पर आपको और आपके परिवार को ढेरों शुभकामनाएं।",
                "बुराई पर अच्छाई की जीत के इस पवित्र त्योहार पर आप सभी को दशहरे की बधाई।"
            ],
            'english': [
                "Wishing you and your family a very Happy Dasara! May Goddess Durga bless you with strength and prosperity.",
                "Happy Vijayadashami! May this festival bring joy, peace, and success to your life.",
                "Warm greetings on the auspicious occasion of Dasara. May good always triumph over evil in your life."
            ],
            'kannada': [
                "ನಿಮ್ಮೆಲ್ಲರಿಗೂ ದಸರಾ ಹಬ್ಬದ ಹಾರ್ದಿಕ ಶುಭಾಷಯಗಳು! ದೇವಿ ದುರ್ಗೆಯವರು ನಿಮ್ಮ ಮೇಲೆ ತಮ್ಮ ಕೃಪೆ ಇರಿಸಲಿ.",
                "ವಿಜಯದಶಮಿ ಶುಭಾಷಯಗಳು! ಈ ಹಬ್ಬ ನಿಮ್ಮ ಜೀವನಕ್ಕೆ ಸಂತೋಷ, ಶಾಂತಿ ಮತ್ತು ಯಶಸ್ಸನ್ನು ತರಲಿ.",
                "ದಸರಾ ಹಬ್ಬದ ಶುಭಾಷಯಗಳು. ನಿಮ್ಮ ಜೀವನದಲ್ಲಿ ಯಾವಾಗಲೂ ಒಳ್ಳೆಯತನ ಕೆಟ್ಟತನದ ಮೇಲೆ ವಿಜಯಿ ಹೊಂದಲಿ."
            ],
            'tamil': [
                "தசரா திருநாள் நல்வாழ்த்துக்கள்! தேவி துர்க்கா உங்கள் மீது தனது அருளைப் பொழியட்டும்.",
                "விஜயதசமி நல்வாழ்த்துக்கள்! இந்த திருவிழா உங்கள் வாழ்வில் மகிழ்ச்சி, சமாதானம் மற்றும் வெற்றியைக் கொண்டு வரட்டும்.",
                "தசரா திருநாளின் மங்கல வாழ்த்துக்கள். உங்கள் வாழ்க்கையில் நல்லது எப்போதும் தீமையை வெல்லட்டும்."
            ],
            'telugu': [
                "మీ అందరికీ దసరా శుభాకాంక్షలు! దేవి దుర్గా మీపై తన కృపను కొనసాగించాలి.",
                "విజయదశమి శుభాకాంక్షలు! ఈ పండుగ మీ జీవితానికి సంతోషం, శాంతి మరియు విజయాన్ని తెస్తుంది.",
                "దసరా పండుగ శుభాకాంక్షలు. మీ జీవితంలో మంచి ఎప్పుడూ చెడుపై విజయం సాధించాలి."
            ],
            'marathi': [
                "तुम्हा सर्वांना दसर्याच्या हार्दिक शुभेच्छा! देवी दुर्गा तुमच्यावर त्यांची कृपा कायम ठेवो.",
                "विजयादशमीच्या हार्दिक शुभेच्छा! हा सण तुमच्या आयुष्यात आनंद, शांती आणि यश आणो.",
                "दसर्याच्या पवित्र दिवसाच्या शुभेच्छा. तुमच्या आयुष्यात चांगल्यावर नेहमी विजय मिळो."
            ],
            'bengali': [
                "আপনাকে ও আপনার পরিবারকে শুভ বিজয়া দশমীর প্রীতি ও শুভেচ্ছা! মা দুর্গা আপনার উপর তাঁর কৃপা বর্ষণ করুন।",
                "শুভ বিজয়া! এই উৎসব আপনার জীবনে সুখ, শান্তি ও সাফল্য বয়ে আনুক।",
                "বিজয়া দশমীর শুভেচ্ছা। আপনার জীবনে সদা সত্যের জয় হোক।"
            ]
        }
    
    def get_wish(self, language='english'):
        """Get a random wish in specified language"""
        if language.lower() in self.wishes:
            return random.choice(self.wishes[language.lower()])
        else:
            return random.choice(self.wishes['english'])
    
    def get_multilingual_wishes(self, num_wishes=3):
        """Get wishes in multiple languages"""
        selected_languages = random.sample(list(self.wishes.keys()), min(num_wishes, len(self.wishes)))
        multilingual_wishes = []
        for lang in selected_languages:
            multilingual_wishes.append({
                'language': lang.capitalize(),
                'wish': random.choice(self.wishes[lang])
            })
        return multilingual_wishes

# Usage examples
wishes = DasaraWishes()

# Single wish in specific language
print("Hindi Wish:", wishes.get_wish('hindi'))
print("English Wish:", wishes.get_wish('english'))

# Multiple languages
print("\nMultilingual Wishes:")
for wish in wishes.get_multilingual_wishes(4):
    print(f"{wish['language']}: {wish['wish']}")
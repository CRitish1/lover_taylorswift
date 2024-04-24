!pip install gtts

from gtts import gTTS
from IPython.display import Audio

# Define the love letter content as a string
love_letter = """
Ladies and gentlemen, will you please stand?
With every guitar string scar on my hand
I take this magnetic force of a man to be my lover
My heart's been borrowed and yours has been blue
All's well that ends well to end up with you
Swear to be overdramatic and true to my lover
And you'll save all your dirtiest jokes for me
And at every table, I'll save you a seat, lover

"""

# Convert the love letter to speech
tts = gTTS(love_letter)
tts.save('love_letter.mp3')

# Play the love letter sound
Audio('love_letter.mp3', autoplay=True)

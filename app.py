import streamlit as st
import random  # For random poem variations

# Hardcoded phoneme to chakra map based on chat data (English primary; simplified for others)
phoneme_to_chakra = {
    # English (from chat)
    '/s/': 'Muladhara',
    '/z/': 'Muladhara',
    '/ʃ/': 'Muladhara',
    '/ʒ/': 'Muladhara',
    '/m/': 'Svadhisthana',
    '/n/': 'Svadhisthana',
    '/w/': 'Svadhisthana',
    '/j/': 'Svadhisthana',
    '/l/': 'Svadhisthana',
    '/r/': 'Svadhisthana',
    '/p/': 'Manipura',
    '/b/': 'Manipura',
    '/t/': 'Manipura',
    '/d/': 'Manipura',
    '/k/': 'Manipura',
    '/ɡ/': 'Manipura',
    '/f/': 'Manipura',
    '/v/': 'Manipura',
    '/θ/': 'Manipura',
    '/ð/': 'Manipura',
    '/tʃ/': 'Ajna',  # Reassigned from Anahata as per reasoning
    '/dʒ/': 'Ajna',  # Reassigned
    '/h/': 'Anahata',
    '/ŋ/': 'Vishuddha',  # Reassigned
    '/æ/': 'Vishuddha',  # Reassigned
    '/ɛ/': 'Vishuddha',  # Reassigned
    '/ɪ/': 'Vishuddha',  # Reassigned
    '/ʌ/': 'Vishuddha',  # Reassigned
    '/ɒ/': 'Vishuddha',  # Reassigned
    '/ʊ/': 'Vishuddha',  # Reassigned
    '/ə/': 'Vishuddha',  # Reassigned
    '/ɔː/': 'Vishuddha',  # Reassigned
    '/iː/': 'Vishuddha',
    '/uː/': 'Vishuddha',
    '/eɪ/': 'Vishuddha',
    '/aɪ/': 'Vishuddha',
    '/aʊ/': 'Vishuddha',
    '/ɔɪ/': 'Vishuddha',
    '/ɑː/': 'Vishuddha',
    # Simplified for other languages (from chat mappings)
    '/ʋ/': 'Muladhara',  # Shared in Sanskrit/Hindi/Kannada
    '/ʃ/': 'Muladhara',
    '/s/': 'Muladhara',
    '/h/': 'Muladhara',
    '/b/': 'Svadhisthana',
    '/bʰ/': 'Svadhisthana',
    '/y/': 'Svadhisthana',  # /j/
    '/ɖ/': 'Manipura',
    '/ɖʰ/': 'Manipura',
    '/ɳ/': 'Ajna',  # Reassigned
    '/k/': 'Anahata',
    '/kʰ/': 'Anahata',
    '/a/': 'Vishuddha',
    '/aː/': 'Vishuddha',
    '/i/': 'Vishuddha',
    '/iː/': 'Vishuddha',
    '/u/': 'Vishuddha',
    '/uː/': 'Vishuddha',
    '/e/': 'Vishuddha',
    '/ai/': 'Vishuddha',
    '/o/': 'Vishuddha',
    '/au/': 'Vishuddha',
    '/ã/': 'Vishuddha',
    '/aḥ/': 'Vishuddha',
    '/ɽ/': 'Vishuddha',  # Hindi-specific
    '/ɽʰ/': 'Vishuddha',  # Hindi
    '/ɭ/': 'Vishuddha',  # Kannada
    '/kʃ/': 'Ajna',
    # Om for Sahasrara
    '/ɑː/': 'Sahasrara',
    '/uː/': 'Sahasrara',
    '/m/': 'Sahasrara'
}

# Chakra vivid descriptions with imagery and emojis (from research)
chakra_descriptions = {
    'Muladhara': 'The Root Chakra, a crimson lotus rooted in the earth's core at the base of your spine, grounding you like an ancient mountain amidst stormy winds, symbolizing stability and survival. 🌍 🔴 🌱 🧘 🏔️',
    'Svadhisthana': 'The Sacral Chakra, an orange river flowing below the navel, a vermillion lotus with a crescent moon, unleashing creativity and passion like a dancing flame in the ocean's embrace. 🟠 🌊 🌸 💃 🎨',
    'Manipura': 'The Solar Plexus Chakra, a golden fire blazing near the navel, a 10-petaled lotus of willpower, radiating like the sun's core, fueling metabolism and inner strength in a cosmic furnace. 🟡 🔥 🌞 💪 🌟',
    'Anahata': 'The Heart Chakra, a verdant hexagram lotus blooming in the chest, breathing air of compassion, flowing love like emerald rivers through the universe, bending karma with forgiveness's gentle breeze. 💚 🌬️ 🌸 ❤️ 🌌',
    'Vishuddha': 'The Throat Chakra, a sapphire full-moon lotus in the throat, echoing aether's purity, purifying organs with immortal nectar, inspiring artistic truth like a starry night's symphony. 🔵 🌕 🗣️ 🎤 🎨',
    'Ajna': 'The Third Eye Chakra, an indigo gateway between the brows, a two-petaled lotus of intuition, linking to transcendent realms, unveiling insights like a cosmic eye piercing the veil of illusion. 🟣 👁️ 🌌 🧠 ✨',
    'Sahasrara': 'The Crown Chakra, a violet thousand-petaled lotus at the head's summit, merging energies into pure consciousness, achieving enlightenment like a blooming galaxy in eternal samadhi. ⚪ 🌟 🧘 🌌 🌺'
}

# Simple letter to phoneme approximation (expanded for languages)
letter_to_phoneme = {
    'english': {
        'a': '/æ/',
        'b': '/b/',
        'c': '/k/',
        'd': '/d/',
        'e': '/ɛ/',
        'f': '/f/',
        'g': '/ɡ/',
        'h': '/h/',
        'i': '/ɪ/',
        'j': '/dʒ/',
        'k': '/k/',
        'l': '/l/',
        'm': '/m/',
        'n': '/n/',
        'o': '/ɒ/',
        'p': '/p/',
        'q': '/k/',
        'r': '/r/',
        's': '/s/',
        't': '/t/',
        'u': '/ʌ/',
        'v': '/v/',
        'w': '/w/',
        'x': '/ks/',
        'y': '/j/',
        'z': '/z/'
    },
    'sanskrit': letter_to_phoneme['english'],  # Simplified placeholder; use English approx
    'hindi': letter_to_phoneme['english'],  # Simplified
    'kannada': letter_to_phoneme['english']  # Simplified
}

def approximate_phonemes(name, language='english'):
    name = name.lower()
    phonemes = []
    i = 0
    while i < len(name):
        letter = name[i]
        if letter in letter_to_phoneme[language.lower()]:
            phonemes.append(letter_to_phoneme[language.lower()][letter])
        i += 1
    return list(set(phonemes))  # Unique

st.title("Enhanced Fun Name Chakra App 🌟✨")

st.markdown("Dive into the mystical world of chakras inspired by Maheshwara Sutras! Enter your name to activate vibrant energies with artistic imagery and emojis! 🎨🌈")

language = st.selectbox("Choose Language:", ["English", "Sanskrit", "Hindi", "Kannada"])

name = st.text_input("Enter your name:", placeholder="Type your name here...")

if name:
    st.success(f"Namaste, {name}! 👋 Your essence vibrates through the cosmos! 🌌")

    # Approximate phonemes
    phonemes = approximate_phonemes(name, language)
    st.info(f"Approximated phonemes in {language}: {', '.join(phonemes)} 🔊 – Echoes of ancient sounds!")

    # Map to chakras
    activated_chakras = set()
    for p in phonemes:
        if p in phoneme_to_chakra:
            activated_chakras.add(phoneme_to_chakra[p])

    if activated_chakras:
        st.warning(f"Your name awakens these chakras: {', '.join(activated_chakras)} – A symphony of energy! 🎶✨")
    else:
        st.warning("Your name's vibrations are uniquely cosmic – beyond mapped chakras! 🌟")

    # Vivid Chakra Imagery
    st.header("Artistic Chakra Visions 🖼️")
    for chakra in activated_chakras:
        st.subheader(f"{chakra} Awakens!")
        st.markdown(chakra_descriptions.get(chakra, 'Mysterious energy flows...'))
        # Emoji art example
        if chakra == 'Muladhara':
            st.text("🔴\n🌍 🌱\n🏔️ 🧘")
        # Add more for other chakras if desired
        st.markdown("---")

    # Fun Chakra Poem
    st.header("Your Personalized Chakra Poem 📜🌹")
    poem_lines = [f"In realms where {name} dances free,"]
    for chakra in activated_chakras:
        poem_lines.append(f"{chakra} glows with vivid glee – {random.choice(chakra_descriptions[chakra].split(',')[0].split(' ')[-3:])}! ✨")
    poem_lines.append(f"Embrace the light, let your spirit be! 🚀🌈")
    poem = '\n'.join(poem_lines)
    st.text_area("Poem", poem, height=150)

    # Reversed name fun
    reversed_name = name[::-1]
    st.error(f"Whisper your name backwards: **{reversed_name}** 🔄 – A hidden mantra unlocking secrets! 🗝️")

    # Length fun with imagery
    length = len(name)
    if length < 5:
        msg = "Compact like a seed bursting into a majestic tree in Muladhara's earth! 🌱🏔️"
    elif length < 8:
        msg = "Flowing gracefully like Svadhisthana's creative waves under a sunset sky! 🌅🌊"
    else:
        msg = "Expansive as Sahasrara's thousand petals blooming in cosmic violet light! 🌌🌺"
    st.success(f"Name length {length}: {msg}")

    # Activation button
    if st.button("Activate Your Chakras! ⚡"):
        st.confetti()
        st.balloons()
        st.write("Chakras ignited with artistic brilliance – feel the vivid energy surge! 🎉🔥")
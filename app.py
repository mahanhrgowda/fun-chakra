# -*- coding: utf-8 -*-
import streamlit as st
import random

# Hardcoded phoneme to chakra map based on chat data
phoneme_to_chakra = {
    # English
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
    '/tʃ/': 'Ajna',
    '/dʒ/': 'Ajna',
    '/h/': 'Anahata',
    '/ŋ/': 'Vishuddha',
    '/æ/': 'Vishuddha',
    '/ɛ/': 'Vishuddha',
    '/ɪ/': 'Vishuddha',
    '/ʌ/': 'Vishuddha',
    '/ɒ/': 'Vishuddha',
    '/ʊ/': 'Vishuddha',
    '/ə/': 'Vishuddha',
    '/ɔː/': 'Vishuddha',
    '/iː/': 'Vishuddha',
    '/uː/': 'Vishuddha',
    '/eɪ/': 'Vishuddha',
    '/aɪ/': 'Vishuddha',
    '/aʊ/': 'Vishuddha',
    '/ɔɪ/': 'Vishuddha',
    '/ɑː/': 'Vishuddha',
    # Sanskrit, Hindi, Kannada (simplified, based on chat mappings)
    '/ʋ/': 'Muladhara',
    '/ʃ/': 'Muladhara',
    '/s/': 'Muladhara',
    '/h/': 'Muladhara',
    '/b/': 'Svadhisthana',
    '/bʰ/': 'Svadhisthana',
    '/m/': 'Svadhisthana',
    '/j/': 'Svadhisthana',
    '/r/': 'Svadhisthana',
    '/l/': 'Svadhisthana',
    '/ɖ/': 'Manipura',
    '/ɖʰ/': 'Manipura',
    '/ɳ/': 'Ajna',
    '/t/': 'Manipura',
    '/tʰ/': 'Manipura',
    '/d/': 'Manipura',
    '/dʰ/': 'Manipura',
    '/n/': 'Manipura',
    '/p/': 'Manipura',
    '/pʰ/': 'Manipura',
    '/k/': 'Anahata',
    '/kʰ/': 'Anahata',
    '/ɡ/': 'Anahata',
    '/ɡʰ/': 'Anahata',
    '/ŋ/': 'Anahata',
    '/c/': 'Anahata',
    '/cʰ/': 'Anahata',
    '/ɟ/': 'Anahata',
    '/ɟʰ/': 'Anahata',
    '/ɲ/': 'Vishuddha',  # Reassigned for Hindi, Kannada
    '/ʈ/': 'Anahata',
    '/ʈʰ/': 'Anahata',
    '/a/': 'Vishuddha',
    '/aː/': 'Vishuddha',
    '/i/': 'Vishuddha',
    '/iː/': 'Vishuddha',
    '/u/': 'Vishuddha',
    '/uː/': 'Vishuddha',
    '/e/': 'Vishuddha',
    '/eː/': 'Vishuddha',
    '/o/': 'Vishuddha',
    '/oː/': 'Vishuddha',
    '/ai/': 'Vishuddha',
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

# Vivid chakra descriptions with artistic imagery and emojis
chakra_descriptions = {
    'Muladhara': 'The Root Chakra, a crimson lotus rooted deep in the earth’s molten core at the base of your spine, grounding you like an ancient mountain standing firm against stormy winds, embodying unyielding stability and primal survival. 🌍 🔴 🌱 🧘 🏔️',
    'Svadhisthana': 'The Sacral Chakra, an orange river cascading below your navel, a vermillion lotus cradling a crescent moon, igniting creativity and passion like a dancer’s flame swirling in the ocean’s mystic embrace. 🟠 🌊 🌸 💃 🎨',
    'Manipura': 'The Solar Plexus Chakra, a golden inferno blazing near your navel, a ten-petaled lotus radiating willpower, its fiery core pulsing like the sun, fueling strength and transformation in a cosmic furnace. 🟡 🔥 🌞 💪 🌟',
    'Anahata': 'The Heart Chakra, a verdant hexagram lotus blooming in your chest, breathing emerald air of compassion, flowing love like rivers through a starlit universe, bending karma with forgiveness’s gentle breeze. 💚 🌬️ 🌸 ❤️ 🌌',
    'Vishuddha': 'The Throat Chakra, a sapphire full-moon lotus glowing in your throat, echoing the pure aether, purifying with immortal nectar, inspiring truth like a starry night’s symphony sung by celestial muses. 🔵 🌕 🗣️ 🎤 🎨',
    'Ajna': 'The Third Eye Chakra, an indigo gateway between your brows, a two-petaled lotus of intuition, piercing the veil of illusion to reveal cosmic insights, like a radiant eye in a nebula’s heart. 🟣 👁️ 🌌 🧠 ✨',
    'Sahasrara': 'The Crown Chakra, a violet thousand-petaled lotus crowning your head, merging energies into pure consciousness, blooming like a galaxy in eternal samadhi, where enlightenment dances in divine light. ⚪ 🌟 🧘 🌌 🌺'
}

# Simple letter-to-phoneme approximation
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
    'sanskrit': {
        'a': '/a/',
        'ā': '/aː/',
        'i': '/i/',
        'ī': '/iː/',
        'u': '/u/',
        'ū': '/uː/',
        'b': '/b/',
        'bh': '/bʰ/',
        'm': '/m/',
        'y': '/j/',
        'r': '/r/',
        'l': '/l/',
        'v': '/ʋ/',
        'ś': '/ʃ/',
        's': '/s/',
        'h': '/h/',
        'k': '/k/',
        'kh': '/kʰ/',
        'g': '/ɡ/',
        'gh': '/ɡʰ/',
        'ṅ': '/ŋ/',
        'c': '/c/',
        'ch': '/cʰ/',
        'j': '/ɟ/',
        'jh': '/ɟʰ/',
        'ñ': '/ɲ/',
        'ṭ': '/ʈ/',
        'ṭh': '/ʈʰ/',
        'ḍ': '/ɖ/',
        'ḍh': '/ɖʰ/',
        'ṇ': '/ɳ/',
        't': '/t/',
        'th': '/tʰ/',
        'd': '/d/',
        'dh': '/dʰ/',
        'n': '/n/',
        'p': '/p/',
        'ph': '/pʰ/',
        'kṣ': '/kʃ/'
    },
    'hindi': {
        'a': '/ə/',
        'ā': '/aː/',
        'i': '/i/',
        'ī': '/iː/',
        'u': '/u/',
        'ū': '/uː/',
        'e': '/eː/',
        'ai': '/ɛː/',
        'o': '/oː/',
        'au': '/ɔː/',
        'b': '/b/',
        'bh': '/bʰ/',
        'm': '/m/',
        'y': '/j/',
        'r': '/r/',
        'l': '/l/',
        'v': '/ʋ/',
        'ś': '/ʃ/',
        's': '/s/',
        'h': '/h/',
        'k': '/k/',
        'kh': '/kʰ/',
        'g': '/ɡ/',
        'gh': '/ɡʰ/',
        'ṅ': '/ŋ/',
        'c': '/c/',
        'ch': '/cʰ/',
        'j': '/ɟ/',
        'jh': '/ɟʰ/',
        'ñ': '/ɲ/',
        'ṭ': '/ʈ/',
        'ṭh': '/ʈʰ/',
        'ḍ': '/ɖ/',
        'ḍh': '/ɖʰ/',
        'ṛ': '/ɽ/',
        'ṛh': '/ɽʰ/',
        'ṇ': '/ɳ/',
        't': '/t/',
        'th': '/tʰ/',
        'd': '/d/',
        'dh': '/dʰ/',
        'n': '/n/',
        'p': '/p/',
        'ph': '/pʰ/',
        'kṣ': '/kʃ/'
    },
    'kannada': {
        'a': '/a/',
        'ā': '/aː/',
        'i': '/i/',
        'ī': '/iː/',
        'u': '/u/',
        'ū': '/uː/',
        'e': '/e/',
        'ē': '/eː/',
        'o': '/o/',
        'ō': '/oː/',
        'ai': '/ai/',
        'au': '/au/',
        'b': '/b/',
        'bh': '/bʰ/',
        'm': '/m/',
        'y': '/j/',
        'r': '/r/',
        'l': '/l/',
        'ḷ': '/ɭ/',
        'v': '/ʋ/',
        'ś': '/ʃ/',
        's': '/s/',
        'h': '/h/',
        'k': '/k/',
        'kh': '/kʰ/',
        'g': '/ɡ/',
        'gh': '/ɡʰ/',
        'ṅ': '/ŋ/',
        'c': '/c/',
        'ch': '/cʰ/',
        'j': '/ɟ/',
        'jh': '/ɟʰ/',
        'ñ': '/ɲ/',
        'ṭ': '/ʈ/',
        'ṭh': '/ʈʰ/',
        'ḍ': '/ɖ/',
        'ḍh': '/ɖʰ/',
        'ṇ': '/ɳ/',
        't': '/t/',
        'th': '/tʰ/',
        'd': '/d/',
        'dh': '/dʰ/',
        'n': '/n/',
        'p': '/p/',
        'ph': '/pʰ/',
        'kṣ': '/kʃ/'
    }
}

def approximate_phonemes(name, language='english'):
    name = name.lower()
    phonemes = []
    i = 0
    while i < len(name):
        if language.lower() != 'english' and i < len(name) - 1:
            # Check for digraphs like 'bh', 'kh', etc.
            digraph = name[i:i+2]
            if digraph in letter_to_phoneme[language.lower()]:
                phonemes.append(letter_to_phoneme[language.lower()][digraph])
                i += 2
                continue
        letter = name[i]
        if letter in letter_to_phoneme[language.lower()]:
            phonemes.append(letter_to_phoneme[language.lower()][letter])
        i += 1
    return list(set(phonemes))

# Streamlit UI
st.title("🌟 Cosmic Name Chakra Journey 🌌")

st.markdown("""
Embark on a mystical voyage inspired by the ancient Maheshwara Sutras! Enter your name to awaken vibrant chakras, painted with vivid cosmic imagery and sparkling emojis. Discover how your name resonates with the universe's energy! 🎨🌈
""")

# Input form
with st.form("name_form"):
    language = st.selectbox("Choose Language:", ["English", "Sanskrit", "Hindi", "Kannada"])
    name = st.text_input("Enter your name:", placeholder="Type your name here...")
    submitted = st.form_submit_button("Unleash the Chakras! ⚡")

if submitted and name:
    st.success(f"Namaste, {name}! 🌺 Your essence dances through the cosmic tapestry! ✨")

    # Approximate phonemes
    phonemes = approximate_phonemes(name, language)
    st.info(f"Phonemes in {language}: {', '.join(phonemes)} 🔊 – Echoes of ancient vibrations!")

    # Map to chakras
    activated_chakras = set()
    for p in phonemes:
        if p in phoneme_to_chakra:
            activated_chakras.add(phoneme_to_chakra[p])
    
    if activated_chakras:
        st.warning(f"Your name ignites: {', '.join(activated_chakras)} – A celestial symphony! 🎶🌟")
    else:
        st.warning("Your name’s vibrations are uniquely cosmic, transcending mapped chakras! 🌌")

    # Vivid Chakra Imagery
    st.header("🌸 Chakra Visions in Celestial Art 🖼️")
    for chakra in activated_chakras:
        st.subheader(f"{chakra} Awakens! 🌟")
        st.markdown(chakra_descriptions[chakra])
        # Emoji art for each chakra
        if chakra == 'Muladhara':
            st.text("🔴\n🌍 🌱\n🏔️ 🧘")
        elif chakra == 'Svadhisthana':
            st.text("🟠\n🌊 🌸\n💃 🎨")
        elif chakra == 'Manipura':
            st.text("🟡\n🔥 🌞\n💪 🌟")
        elif chakra == 'Anahata':
            st.text("💚\n🌬️ 🌸\n❤️ 🌌")
        elif chakra == 'Vishuddha':
            st.text("🔵\n🌕 🗣️\n🎤 🎨")
        elif chakra == 'Ajna':
            st.text("🟣\n👁️ 🌌\n🧠 ✨")
        elif chakra == 'Sahasrara':
            st.text("⚪\n🌟 🧘\n🌌 🌺")
        st.markdown("---")

    # Chakra Poem
    st.header("📜 Your Cosmic Chakra Poem 🌹")
    poem_lines = [f"In the cosmos, {name} shines bright,"]
    for chakra in activated_chakras:
        words = random.choice(chakra_descriptions[chakra].split(',')[0].split(' ')[-5:-2])
        poem_lines.append(f"{chakra} glows, {''.join(words).strip()} in starlight! ✨")
    poem_lines.append(f"Your essence soars, a radiant cosmic flight! 🚀🌈")
    poem = '\n'.join(poem_lines)
    st.text_area("Poem", poem, height=150)

    # Fun Outputs
    st.header("🌌 Playful Cosmic Insights 🎉")
    # Reversed name
    reversed_name = name[::-1]
    st.error(f"Whispered backwards: **{reversed_name}** 🔄 – A secret mantra woven in stardust! 🗝️🌌")

    # Name length with vivid imagery
    length = len(name)
    if length < 5:
        msg = "Compact as a seed bursting into Muladhara’s ancient earth, sprouting cosmic roots! 🌱🏔️"
    elif length < 8:
        msg = "Flowing like Svadhisthana’s radiant waves under a sunset sky, alive with passion! 🌅🌊"
    else:
        msg = "Expansive as Sahasrara’s thousand petals, blooming in violet galaxies of enlightenment! 🌌🌺"
    st.success(f"Name length {length}: {msg}")

    # Chakra Energy Level
    energy_level = len(activated_chakras)
    if energy_level == 0:
        energy_msg = "A mysterious spark, flickering beyond the cosmos, ready to ignite! ⚡️🌌"
    elif energy_level <= 3:
        energy_msg = "A glowing ember, warming the universe with gentle chakra light! 🔥🌟"
    else:
        energy_msg = "A supernova of energy, blazing through chakras like a celestial storm! 🌠🚀"
    st.info(f"Your Chakra Energy: {energy_msg}")

    # Activation button
    if st.button("Activate Your Chakras! ⚡"):
        st.confetti()
        st.balloons()
        st.write("Chakras ablaze with cosmic brilliance – your energy surges through the universe! 🎉🔥")

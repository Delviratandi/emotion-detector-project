def emotion_detector(text_to_analyze):
    # Penanganan kesalahan jika input kosong atau hanya spasi
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    
    # Mengubah teks ke huruf kecil untuk pencocokan kata kunci
    text_lower = text_to_analyze.lower()
    
    # Standar nilai tiruan (Mock Response)
    anger, disgust, fear, joy, sadness = 0.0, 0.0, 0.0, 0.0, 0.0
    
    if "glad" in text_lower or "happy" in text_lower or "love" in text_lower:
        joy = 0.95
        dominant = 'joy'
    elif "mad" in text_lower or "angry" in text_lower:
        anger = 0.95
        dominant = 'anger'
    elif "disgusted" in text_lower:
        disgust = 0.95
        dominant = 'disgust'
    elif "sad" in text_lower:
        sadness = 0.95
        dominant = 'sadness'
    elif "scared" in text_lower or "fear" in text_lower:
        fear = 0.95
        dominant = 'fear'
    else:
        joy = 0.5
        dominant = 'joy'

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant
    }

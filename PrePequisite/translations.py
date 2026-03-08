# UI Elements Dictionary
ui_translations = {
    "English": {
        "title": "Efficient-YOLO Multi-Crop Disease Detection",
        "subtitle": "Upload a leaf image to detect diseases and get treatment recommendations.",
        "language_select": "Select Language",
        "upload_image": "Upload Plant Image",
        "predict_btn": "Predict Disease",
        "raw_predictions": "Raw Model Predictions",
        "final_analysis": "Final Analysis",
        "scientific_name": "Scientific Name",
        "common_name": "Common Name",
        "show_disease_details": "Show Disease Details",
        "show_treatment": "Show Treatment Recommendations",
        "crop_name_fallback": "Crop Name (If prediction failed)",
        "symptoms_fallback": "Describe Symptoms",
        "search_fallback_btn": "Search Symptoms",
        "healthy_message": "This plant appears healthy. No treatment needed!"
    },
    "Hindi": {
        "title": "मल्टी-क्रॉप रोग पहचान",
        "subtitle": "रोगों का पता लगाने और उपचार के सुझाव के लिए पत्ती की छवि अपलोड करें।",
        "language_select": "भाषा चुनें",
        "upload_image": "पौधे की छवि अपलोड करें",
        "predict_btn": "रोग की भविष्यवाणी करें",
        "raw_predictions": "प्रारंभिक मॉडल भविष्यवाणियां",
        "final_analysis": "अंतिम विश्लेषण",
        "scientific_name": "वैज्ञानिक नाम",
        "common_name": "सामान्य नाम",
        "show_disease_details": "रोग का विवरण दिखाएं",
        "show_treatment": "उपचार की सिफारिशें दिखाएं",
        "crop_name_fallback": "फसल का नाम (यदि भविष्यवाणी विफल रही)",
        "symptoms_fallback": "लक्षणों का वर्णन करें",
        "search_fallback_btn": "लक्षण खोजें",
        "healthy_message": "यह पौधा स्वस्थ प्रतीत होता है। किसी उपचार की आवश्यकता नहीं है!"
    },
    "Urdu": {
        "title": "کثیر فصلی بیماری کی تشخیص",
        "subtitle": "بیماریوں کا پتہ لگانے اور علاج کی سفارشات کے لیے پتے کی تصویر اپ لوڈ کریں۔",
        "language_select": "زبان منتخب کریں",
        "upload_image": "پودے کی تصویر اپ لوڈ کریں",
        "predict_btn": "بیماری کی پیشن گوئی کریں",
        "raw_predictions": "ابتدائی ماڈل کی پیشن گوئیاں",
        "final_analysis": "حتمی تجزیہ",
        "scientific_name": "سائنسی نام",
        "common_name": "عام نام",
        "show_disease_details": "بیماری کی تفصیلات دکھائیں",
        "show_treatment": "علاج کی سفارشات دکھائیں",
        "crop_name_fallback": "فصل کا نام (اگر پیشن گوئی ناکام ہو گئی)",
        "symptoms_fallback": "علامات بیان کریں",
        "search_fallback_btn": "علامات تلاش کریں",
        "healthy_message": "یہ پودا صحت مند معلوم ہوتا ہے۔ کسی علاج کی ضرورت نہیں!"
    },
    "Telugu": {
        "title": "బహుళ-పంటల వ్యాధి గుర్తింపు",
        "subtitle": "వ్యాధులను గుర్తించడానికి మరియు చికిత్స సిఫార్సుల కోసం ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి.",
        "language_select": "భాషను ఎంచుకోండి",
        "upload_image": "మొక్క చిత్రాన్ని అప్‌లోడ్ చేయండి",
        "predict_btn": "వ్యాధిని అంచనా వేయండి",
        "raw_predictions": "ప్రాథమిక మోడల్ అంచనాలు",
        "final_analysis": "తుది విశ్లేషణ",
        "scientific_name": "శాస్త్రీయ నామం",
        "common_name": "సాధారణ నామం",
        "show_disease_details": "వ్యాధి వివరాలను చూపించు",
        "show_treatment": "చికిత్స సిఫార్సులను చూపించు",
        "crop_name_fallback": "పంట పేరు (అంచనా విఫలమైతే)",
        "symptoms_fallback": "లక్షణాలను వివరించండి",
        "search_fallback_btn": "లక్షణాలను శోధించండి",
        "healthy_message": "ఈ మొక్క ఆరోగ్యంగా ఉన్నట్లు కనిపిస్తోంది. ఎలాంటి చికిత్స అవసరం లేదు!"
    }
}

# Disease Information Dictionary (Mapped to your exactly 28 YOLO classes)
disease_info = {
    "Apple__BlackRot": {
        "scientific_name": "Botryosphaeria obtusa",
        "is_healthy": False,
        "English": "Apple Black Rot", "Hindi": "सेब का काला सड़ांध", "Urdu": "سیب کا کالا سڑنا", "Telugu": "ఆపిల్ నల్ల కుళ్ళు"
    },
    "Apple__CedarRust": {
        "scientific_name": "Gymnosporangium juniperi-virginianae",
        "is_healthy": False,
        "English": "Apple Cedar Rust", "Hindi": "सेब का देवदार रस्ट", "Urdu": "سیب کا سیڈر رسٹ", "Telugu": "ఆపిల్ సెడార్ రస్ట్"
    },
    "Apple__Healthy": {
        "scientific_name": "Malus domestica (Healthy)",
        "is_healthy": True,
        "English": "Healthy Apple Leaf", "Hindi": "स्वस्थ सेब का पत्ता", "Urdu": "صحت مند سیب کا پتہ", "Telugu": "ఆరోగ్యకరమైన ఆపిల్ ఆకు"
    },
    "Apple__Scab": {
        "scientific_name": "Venturia inaequalis",
        "is_healthy": False,
        "English": "Apple Scab", "Hindi": "सेब की पपड़ी (स्कैब)", "Urdu": "سیب کی خارش (سکیب)", "Telugu": "ఆపిల్ స్కాబ్"
    },
    "Corn__CommonRust": {
        "scientific_name": "Puccinia sorghi",
        "is_healthy": False,
        "English": "Corn Common Rust", "Hindi": "मक्का का सामान्य रस्ट", "Urdu": "مکئی کا عام رسٹ", "Telugu": "మొక్కజొన్న సాధారణ రస్ట్"
    },
    "Corn__GrayLeafSpot": {
        "scientific_name": "Cercospora zeae-maydis",
        "is_healthy": False,
        "English": "Corn Gray Leaf Spot", "Hindi": "मक्का का ग्रे लीफ स्पॉट", "Urdu": "مکئی کا گرے لیف سپاٹ", "Telugu": "మొక్కజొన్న గ్రే లీఫ్ స్పాట్"
    },
    "Corn__Healthy": {
        "scientific_name": "Zea mays (Healthy)",
        "is_healthy": True,
        "English": "Healthy Corn Leaf", "Hindi": "स्वस्थ मक्का का पत्ता", "Urdu": "صحت مند مکئی کا پتہ", "Telugu": "ఆరోగ్యకరమైన మొక్కజొన్న ఆకు"
    },
    "Corn__LeafBlight": {
        "scientific_name": "Bipolaris maydis",
        "is_healthy": False,
        "English": "Corn Leaf Blight", "Hindi": "मक्का का झुलसा रोग", "Urdu": "مکئی کا لیف بلائٹ", "Telugu": "మొక్కజొన్న ఆకు ఎండు తెగులు"
    },
    "Corn__NorthernLeafBlight": {
        "scientific_name": "Setosphaeria turcica",
        "is_healthy": False,
        "English": "Corn Northern Leaf Blight", "Hindi": "मक्का का उत्तरी पत्ती झुलसा", "Urdu": "مکئی کا ناردرن لیف بلائٹ", "Telugu": "మొక్కజొన్న నార్తర్న్ లీఫ్ బ్లైట్"
    },
    "Grape__BlackRot": {
        "scientific_name": "Guignardia bidwellii",
        "is_healthy": False,
        "English": "Grape Black Rot", "Hindi": "अंगूर का काला सड़ांध", "Urdu": "انگور کا کالا سڑنا", "Telugu": "ద్రాక్ష నల్ల కుళ్ళు"
    },
    "Grape__Esca": {
        "scientific_name": "Phaeoacremonium aleophilum",
        "is_healthy": False,
        "English": "Grape Esca (Black Measles)", "Hindi": "अंगूर का एस्का (काला खसरा)", "Urdu": "انگور کا ایسکا", "Telugu": "ద్రాక్ష ఎస్కా (నల్ల మీజిల్స్)"
    },
    "Grape__Healthy": {
        "scientific_name": "Vitis vinifera (Healthy)",
        "is_healthy": True,
        "English": "Healthy Grape Leaf", "Hindi": "स्वस्थ अंगूर का पत्ता", "Urdu": "صحت مند انگور کا پتہ", "Telugu": "ఆరోగ్యకరమైన ద్రాక్ష ఆకు"
    },
    "Grape__LeafBlight": {
        "scientific_name": "Pseudocercospora vitis",
        "is_healthy": False,
        "English": "Grape Leaf Blight", "Hindi": "अंगूर का पत्ती झुलसा", "Urdu": "انگور کا لیف بلائٹ", "Telugu": "ద్రాక్ష ఆకు ఎండు తెగులు"
    },
    "Potato__EarlyBlight": {
        "scientific_name": "Alternaria solani",
        "is_healthy": False,
        "English": "Potato Early Blight", "Hindi": "आलू का अगेती झुलसा", "Urdu": "آلو کا ارلی بلائٹ", "Telugu": "బంగాళదుంప ఎర్లీ బ్లైట్"
    },
    "Potato__Healthy": {
        "scientific_name": "Solanum tuberosum (Healthy)",
        "is_healthy": True,
        "English": "Healthy Potato Leaf", "Hindi": "स्वस्थ आलू का पत्ता", "Urdu": "صحت مند آلو کا پتہ", "Telugu": "ఆరోగ్యకరమైన బంగాళదుంప ఆకు"
    },
    "Potato__LateBlight": {
        "scientific_name": "Phytophthora infestans",
        "is_healthy": False,
        "English": "Potato Late Blight", "Hindi": "आलू का पछेती झुलसा", "Urdu": "آلو کا لیٹ بلائٹ", "Telugu": "బంగాళదుంప లేట్ బ్లైట్"
    },
    "Tomato__BacterialSpot": {
        "scientific_name": "Xanthomonas campestris pv. vesicatoria",
        "is_healthy": False,
        "English": "Tomato Bacterial Spot", "Hindi": "टमाटर का बैक्टीरियल स्पॉट", "Urdu": "ٹماٹر کا بیکٹیریل سپاٹ", "Telugu": "టొమాటో బ్యాక్టీరియల్ స్పాట్"
    },
    "Tomato__BacterialWilt": {
        "scientific_name": "Ralstonia solanacearum",
        "is_healthy": False,
        "English": "Tomato Bacterial Wilt", "Hindi": "टमाटर का बैक्टीरियल विल्ट", "Urdu": "ٹماٹر کا بیکٹیریل ولٹ", "Telugu": "టొమాటో బ్యాక్టీరియల్ విల్ట్"
    },
    "Tomato__BrownSpots": {
        "scientific_name": "Stemphylium solani", 
        "is_healthy": False,
        "English": "Tomato Brown Spots", "Hindi": "टमाटर पर भूरे धब्बे", "Urdu": "ٹماٹر کے بھورے دھبے", "Telugu": "టొమాటో గోధుమ మచ్చలు"
    },
    "Tomato__EarlyBlight": {
        "scientific_name": "Alternaria solani",
        "is_healthy": False,
        "English": "Tomato Early Blight", "Hindi": "टमाटर का अगेती झुलसा", "Urdu": "ٹماٹر کا ارلی بلائٹ", "Telugu": "టొమాటో ఎర్లీ బ్లైట్"
    },
    "Tomato__Healthy": {
        "scientific_name": "Solanum lycopersicum (Healthy)",
        "is_healthy": True,
        "English": "Healthy Tomato Leaf", "Hindi": "स्वस्थ टमाटर का पत्ता", "Urdu": "صحت مند ٹماٹر کا پتہ", "Telugu": "ఆరోగ్యకరమైన టొమాటో ఆకు"
    },
    "Tomato__LateBlight": {
        "scientific_name": "Phytophthora infestans",
        "is_healthy": False,
        "English": "Tomato Late Blight", "Hindi": "टमाटर का पछेती झुलसा", "Urdu": "ٹماٹر کا لیٹ بلائٹ", "Telugu": "టొమాటో లేట్ బ్లైట్"
    },
    "Tomato__LeafMold": {
        "scientific_name": "Passalora fulva",
        "is_healthy": False,
        "English": "Tomato Leaf Mold", "Hindi": "टमाटर का लीफ मोल्ड", "Urdu": "ٹماٹر کا لیف مولڈ", "Telugu": "టొమాటో లీఫ్ మోల్డ్"
    },
    "Tomato__MosaicVirus": {
        "scientific_name": "Tomato mosaic tobamovirus",
        "is_healthy": False,
        "English": "Tomato Mosaic Virus", "Hindi": "टमाटर मोज़ेक वायरस", "Urdu": "ٹماٹر موزیک وائرس", "Telugu": "టొమాటో మొజాయిక్ వైరస్"
    },
    "Tomato__SeptoriaLeafSpot": {
        "scientific_name": "Septoria lycopersici",
        "is_healthy": False,
        "English": "Tomato Septoria Leaf Spot", "Hindi": "टमाटर का सेप्टोरिया लीफ स्पॉट", "Urdu": "ٹماٹر کا سیپٹوریا لیف سپاٹ", "Telugu": "టొమాటో సెప్టోరియా లీఫ్ స్పాట్"
    },
    "Tomato__SpiderMites": {
        "scientific_name": "Tetranychus urticae (Pest)",
        "is_healthy": False,
        "English": "Spider Mites", "Hindi": "मकड़ी के जाले (स्पाइडर माइट्स)", "Urdu": "مکڑی کے کیڑے (سپائیڈر مائٹس)", "Telugu": "సాలీడు పురుగులు"
    },
    "Tomato__TargetSpot": {
        "scientific_name": "Corynespora cassiicola",
        "is_healthy": False,
        "English": "Tomato Target Spot", "Hindi": "टमाटर का टारगेट स्पॉट", "Urdu": "ٹماٹر کا ٹارگٹ سپاٹ", "Telugu": "టొమాటో టార్గెట్ స్పాట్"
    },
    "Tomato__YellowLeafCurlVirus": {
        "scientific_name": "Tomato yellow leaf curl begomovirus",
        "is_healthy": False,
        "English": "Tomato Yellow Leaf Curl Virus", "Hindi": "टमाटर का पीला पत्ता कर्ल वायरस", "Urdu": "ٹماٹر کا یلو لیف کرل وائرس", "Telugu": "టొమాటో పసుపు ఆకు కర్ల్ వైరస్"
    }
}
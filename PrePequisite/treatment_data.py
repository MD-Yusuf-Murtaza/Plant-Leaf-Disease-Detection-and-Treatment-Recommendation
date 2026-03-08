# =============================================================================
# treatment_data.py
# Comprehensive inline treatment database for all 28 plant disease classes.
# Keyed by disease_id_mapping values (e.g., "tomato_early_blight").
# =============================================================================

TREATMENT_DB = {
    # ─────────────────────── APPLE ───────────────────────────────────────────
    "apple_black_rot": {
        "disease": {"common_name": "Apple Black Rot", "scientific_name": "Botryosphaeria obtusa"},
        "crop":    {"common_name": "Apple"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Circular brown lesions with purple margins on leaves (frog-eye leaf spot). "
            "Fruit shows brown-to-black mummified rot, often with concentric rings. "
            "Cankers with reddish-brown discolouration on bark and branches."
        ),
        "management": {
            "chemical": [
                "Apply captan (Captan 50 WP @ 2.0 g/L) at petal-fall and repeat every 10–14 days during wet weather.",
                "Mancozeb (Dithane M-45 @ 2.5 g/L) is effective as a protectant spray.",
                "Thiophanate-methyl (Topsin-M 70 WP @ 1.0 g/L) for curative action post-infection.",
                "Copper-based fungicides (Bordeaux mixture 1%) for early-season applications.",
            ],
            "preventive": [
                "Prune and destroy all mummified fruits, cankered wood, and dead branches during dormancy.",
                "Maintain good canopy airflow by annual pruning; avoid overcrowding.",
                "Sanitise pruning tools with 70% isopropyl alcohol between cuts.",
                "Remove fallen leaves and debris from the orchard floor each season.",
                "Avoid overhead irrigation; use drip irrigation to keep foliage dry.",
            ],
        },
    },

    "apple_cedar_rust": {
        "disease": {"common_name": "Apple Cedar Rust", "scientific_name": "Gymnosporangium juniperi-virginianae"},
        "crop":    {"common_name": "Apple"},
        "pathogen_type": "Fungal (Rust)",
        "symptoms": (
            "Bright orange-yellow spots on upper leaf surface in spring. "
            "Later, tube-like aecia (spore horns) erupt from the lower leaf surface. "
            "Infected fruit shows distortion and premature drop."
        ),
        "management": {
            "chemical": [
                "Myclobutanil (Rally 40 WP @ 0.4 g/L) applied at pink bud stage, petal-fall, and 7–10 days later.",
                "Propiconazole (Tilt 25 EC @ 1 mL/L) as an effective DMI fungicide against rust.",
                "Fenarimol (Rubigan) also provides good control during primary infection period.",
                "Lime sulfur sprays during dormancy reduce overwintering inoculum on cedar galls.",
            ],
            "preventive": [
                "Plant rust-resistant apple varieties (e.g., Redfree, Liberty, Enterprise).",
                "Remove or relocate Eastern red cedar (Juniperus virginiana) within 1 km of the orchard.",
                "Monitor cedar trees for orange gelatinous galls in spring and remove them.",
                "Begin protective sprays before wet weather when cedar galls are active.",
            ],
        },
    },

    "apple_scab": {
        "disease": {"common_name": "Apple Scab", "scientific_name": "Venturia inaequalis"},
        "crop":    {"common_name": "Apple"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Olive-green to brown velvety lesions on leaves, often causing leaf curl and early drop. "
            "Fruit shows dark, corky, scabby lesions that crack open in wet conditions. "
            "Severe infections lead to defoliation and unmarketable fruit."
        ),
        "management": {
            "chemical": [
                "Captan (Captan 50 WP @ 2.5 g/L) applied starting at green-tip stage every 7–10 days.",
                "Dodine (Cyprex 65 W @ 0.65 g/L) for early-season protectant coverage.",
                "Difenoconazole (Score 250 EC @ 0.5 mL/L) for curative action within 72 hours of infection.",
                "Kresoxim-methyl (Stroby WG @ 0.15 g/L) offers both curative and protectant activity.",
            ],
            "preventive": [
                "Rake and compost or bury fallen leaves in autumn to destroy overwintering spores (pseudothecia).",
                "Use disease-forecasting models (e.g., RIMpro) to time sprays to infection events.",
                "Plant scab-resistant cultivars like Florina, Jonafree, or Pristine.",
                "Avoid late-evening irrigation that prolongs leaf wetness periods.",
            ],
        },
    },

    # ─────────────────────── CORN / MAIZE ────────────────────────────────────
    "maize_common_rust": {
        "disease": {"common_name": "Maize Common Rust", "scientific_name": "Puccinia sorghi"},
        "crop":    {"common_name": "Maize / Corn"},
        "pathogen_type": "Fungal (Rust)",
        "symptoms": (
            "Small, oval to elongated brick-red pustules (uredinia) scattered on both leaf surfaces. "
            "Later pustules turn black (telia). Severe infection causes leaf yellowing and reduces photosynthesis."
        ),
        "management": {
            "chemical": [
                "Propiconazole (Tilt 25 EC @ 1 mL/L) at first appearance of pustules, repeat after 14 days.",
                "Azoxystrobin + Propiconazole (Quilt Xcel @ 1 L/ha) for both preventive and curative control.",
                "Mancozeb (Dithane M-45 @ 2.5 g/L) as a protectant spray when conditions favour rust.",
                "Tebuconazole (Folicur EW 250 @ 1 mL/L) provides reliable control of cereal rusts.",
            ],
            "preventive": [
                "Grow resistant or tolerant hybrid varieties recommended by ICAR / CIMMYT.",
                "Avoid late planting that exposes the crop to peak rust pressure during grain fill.",
                "Scout fields every 5–7 days from V6 stage onwards; act at trace levels in susceptible hybrids.",
                "Maintain balanced nutrition — avoid excess nitrogen fertiliser, which increases susceptibility.",
            ],
        },
    },

    "maize_gray_leaf_spot": {
        "disease": {"common_name": "Maize Gray Leaf Spot", "scientific_name": "Cercospora zeae-maydis"},
        "crop":    {"common_name": "Maize / Corn"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Rectangular, tan to gray lesions with sharp parallel margins between leaf veins. "
            "Lesions may coalesce to blight entire leaves. Survives in corn debris."
        ),
        "management": {
            "chemical": [
                "Pyraclostrobin (Headline @ 1 L/ha) at VT/R1 (tasselling/silking) for best economic return.",
                "Azoxystrobin + Propiconazole (Quilt Xcel @ 1 L/ha) — the most widely used combination.",
                "Trifloxystrobin + Prothioconazole (Stratego YLD @ 0.75 L/ha) for broad-spectrum control.",
            ],
            "preventive": [
                "Use resistant hybrid varieties; check ICAR regional variety trial data.",
                "Practise crop rotation — avoid growing maize on the same land consecutively.",
                "Till or incorporate corn residue to speed decomposition of infected stover.",
                "Maintain adequate plant spacing to improve air circulation.",
            ],
        },
    },

    "maize_maydis_leaf_blight": {
        "disease": {"common_name": "Southern Corn Leaf Blight", "scientific_name": "Bipolaris maydis"},
        "crop":    {"common_name": "Maize / Corn"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Tan, elongated lesions with distinct wavy margins, often 6–12 cm long. "
            "Lesions have a yellow halo and progress from lower leaves upward. "
            "Severe infection causes premature death of the canopy."
        ),
        "management": {
            "chemical": [
                "Mancozeb (Dithane M-45 @ 2.5 g/L) applied at early symptom appearance.",
                "Propiconazole (Tilt 25 EC @ 1 mL/L) at silking for maximum grain protection.",
                "Carbendazim (Bavistin 50 WP @ 1 g/L) provides curative activity.",
            ],
            "preventive": [
                "Grow T (Texas)-cytoplasm-free or resistant hybrid seed.",
                "Avoid planting in fields with heavy corn residue from the previous season.",
                "Rotate with non-host crops such as soybean, groundnut, or sorghum.",
            ],
        },
    },

    "maize_turcicum_leaf_blight": {
        "disease": {"common_name": "Northern Corn Leaf Blight", "scientific_name": "Setosphaeria turcica"},
        "crop":    {"common_name": "Maize / Corn"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Large, cigar-shaped gray-green to tan lesions (5–15 cm long) on leaves. "
            "Lesions have no distinct border (unlike southern blight). "
            "Dark green sporulation visible on lesion surface under humid conditions."
        ),
        "management": {
            "chemical": [
                "Propiconazole (Tilt 25 EC @ 1 mL/L) applied 4–6 weeks after sowing and at tasselling.",
                "Azoxystrobin (Amistar 25 SC @ 1 mL/L) as a protectant from V6 onwards in heavy disease years.",
                "Mancozeb + Carbendazim (Saaf @ 2 g/L) — widely available and cost-effective.",
            ],
            "preventive": [
                "Grow Ht-gene resistant hybrids; note that new races can overcome Ht1 resistance.",
                "Scout from V6 to tasselling; spray if >50% of plants show symptoms below the ear leaf.",
                "Plough in or remove crop debris promptly after harvest.",
                "Optimise nitrogen levels — over-fertilised crops are more severely affected.",
            ],
        },
    },

    # ─────────────────────── GRAPE ───────────────────────────────────────────
    "grapes_black_rot": {
        "disease": {"common_name": "Grape Black Rot", "scientific_name": "Guignardia bidwellii"},
        "crop":    {"common_name": "Grape"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Circular, reddish-brown leaf lesions with a black border and tiny black fruiting bodies (pycnidia). "
            "Infected berries turn brown, shrivel, and mummify into hard, black 'raisins' (mummies)."
        ),
        "management": {
            "chemical": [
                "Myclobutanil (Nova 40 WP @ 0.4 g/L) from 2 weeks before bloom to 4 weeks after; highly effective.",
                "Captan (Captan 50 WP @ 2.5 g/L) as a protectant spray every 7–10 days during wet periods.",
                "Mancozeb (Dithane M-45 @ 2.5 g/L) applied before and immediately after rainfall events.",
                "Tebuconazole (Folicur EW 250 @ 1 mL/L) provides curative control up to 5 days after infection.",
            ],
            "preventive": [
                "Remove and destroy all mummified berries and infected canes during dormant pruning.",
                "Maintain open canopy through shoot positioning, hedging, and leaf removal around clusters.",
                "Avoid deep mulching around the vine base that retains moisture.",
                "Monitor weather daily; use the Black Rot infection model to time sprays.",
            ],
        },
    },

    "grape_esca": {
        "disease": {"common_name": "Grape Esca (Black Measles)", "scientific_name": "Phaeoacremonium aleophilum / Phaeomoniella chlamydospora"},
        "crop":    {"common_name": "Grape"},
        "pathogen_type": "Fungal (Wood pathogen complex)",
        "symptoms": (
            "Tiger-stripe pattern of yellow/red interveinal chlorosis on leaves. "
            "Black spots on berry surface (hence 'Black Measles'). "
            "Internal wood shows dark brown streaking. Apoplexy (sudden vine death) in hot seasons."
        ),
        "management": {
            "chemical": [
                "No fully curative chemical treatment exists. Sodium arsenite (now banned in most countries) was historically used.",
                "Fosetyl-Al (Aliette 80 WG @ 2.5 g/L) applied to trunk wounds shows some suppression.",
                "Trichoderma-based biological agents (e.g., T. harzianum) applied as a wound protectant after pruning.",
            ],
            "preventive": [
                "CRITICAL: Protect pruning wounds immediately with wound sealant or Bordeaux paste.",
                "Prune during dry weather to minimise wood moisture and spore germination.",
                "Remove symptomatic cordons by cutting below the diseased wood; seal cut.",
                "Avoid mechanical wounding of vines during field operations.",
                "Delay pruning until early spring to allow natural wound healing.",
            ],
        },
    },

    "grape_leaf_blight": {
        "disease": {"common_name": "Grape Leaf Blight (Isariopsis Leaf Spot)", "scientific_name": "Pseudocercospora vitis"},
        "crop":    {"common_name": "Grape"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Irregular, dark reddish-brown spots on upper leaf surface with olive-gray sporulation below. "
            "Lesions coalesce causing large dead areas. Severe defoliation weakens vines."
        ),
        "management": {
            "chemical": [
                "Copper oxychloride (COC @ 3.0 g/L) applied at first sign of spots.",
                "Mancozeb (Dithane M-45 @ 2.5 g/L) every 10–14 days during the growing season.",
                "Carbendazim (Bavistin 50 WP @ 1.0 g/L) for curative activity.",
                "Hexaconazole (Contaf 5 EC @ 2 mL/L) for effective post-infection control.",
            ],
            "preventive": [
                "Maintain good airflow through canopy training and leaf management.",
                "Avoid overhead irrigation; drip or furrow irrigation keeps foliage dry.",
                "Collect and destroy fallen leaves to reduce overwintering inoculum.",
                "Apply Bordeaux mixture (1%) before the monsoon season as a prophylactic measure.",
            ],
        },
    },

    # ─────────────────────── POTATO ──────────────────────────────────────────
    "potato_early_blight": {
        "disease": {"common_name": "Potato Early Blight", "scientific_name": "Alternaria solani"},
        "crop":    {"common_name": "Potato"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Dark brown, circular lesions with concentric rings (target-board pattern) on older leaves. "
            "Lesions surrounded by yellow halo. Foliage blighting from bottom of plant upward. "
            "Tubers may show dark, sunken lesions with corky tissue underneath."
        ),
        "management": {
            "chemical": [
                "Mancozeb (Dithane M-45 @ 2.5 g/L) — first-choice protectant; apply every 7–10 days.",
                "Chlorothalonil (Kavach @ 2.0 g/L) protects well in wet conditions.",
                "Azoxystrobin (Amistar 25 SC @ 1.0 mL/L) gives excellent control; limit to 2 applications.",
                "Difenoconazole (Score 250 EC @ 0.5 mL/L) as a curative DMI when lesions appear.",
            ],
            "preventive": [
                "Use certified, disease-free seed tubers; inspect before planting.",
                "Optimise nitrogen supply — over or under-fertilisation increases susceptibility.",
                "Maintain adequate plant spacing (45 × 15 cm) for airflow.",
                "Rotate with cereals or legumes for at least 2 years.",
                "Scout weekly from 2 weeks after emergence; spray when lesions first appear.",
            ],
        },
    },

    "potato_late_blight": {
        "disease": {"common_name": "Potato Late Blight", "scientific_name": "Phytophthora infestans"},
        "crop":    {"common_name": "Potato"},
        "pathogen_type": "Oomycete (Water Mould)",
        "symptoms": (
            "Water-soaked, pale green lesions on leaf tips and margins, rapidly enlarging and turning brown. "
            "White cottony sporulation visible on leaf underside in humid conditions. "
            "Stems show dark brown lesions. Tubers rot internally with reddish-brown granular rot extending inward."
        ),
        "management": {
            "chemical": [
                "Metalaxyl-M + Mancozeb (Ridomil Gold MZ @ 2.5 g/L) — gold standard for late blight; curative + protectant.",
                "Cymoxanil + Mancozeb (Curzate @ 2.5 g/L) applied within 3 days of infection for curative effect.",
                "Fluopicolide + Propamocarb (Infinito @ 1.6 mL/L) — systemic, excellent for advanced-stage control.",
                "Copper hydroxide (Kocide 2000 @ 3.0 g/L) as a protectant spray early in season.",
                "Mandipropamid (Revus @ 0.6 mL/L) for very high-risk periods; no cross-resistance to metalaxyl.",
            ],
            "preventive": [
                "Plant resistant varieties: Kufri Jyoti, Kufri Badshah (ICAR recommended) or tolerant varieties.",
                "Use blight forecasting (BlightPro, CARAH model) to time first spray accurately.",
                "Destroy volunteer potato plants and infected haulms immediately.",
                "Avoid waterlogged fields; ensure good drainage and hill up soil around stems.",
                "Desiccate haulms 2–3 weeks before harvest to prevent tuber infection.",
            ],
        },
    },

    # ─────────────────────── TOMATO ──────────────────────────────────────────
    "tomato_bacterial_spot": {
        "disease": {"common_name": "Tomato Bacterial Spot", "scientific_name": "Xanthomonas campestris pv. vesicatoria"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Bacterial",
        "symptoms": (
            "Small, water-soaked lesions on leaves that become dark brown with a yellow halo. "
            "Lesions on fruit are raised, scab-like, dark brown spots up to 3 mm across. "
            "Infected seedlings show blighting of leaves and stem tip necrosis."
        ),
        "management": {
            "chemical": [
                "Copper hydroxide (Kocide 2000 @ 3.0 g/L) + Mancozeb (2.5 g/L) combination — most effective standard.",
                "Streptomycin sulphate (Agrimycin 100 @ 0.2 g/L) — antibiotic; use judiciously to prevent resistance.",
                "Copper oxychloride (Blitox 50 @ 3.0 g/L) as an economical alternative.",
                "Bactericides containing Kasugamycin (Kasu-B @ 2 mL/L) show promise against Xanthomonas strains.",
            ],
            "preventive": [
                "Use certified disease-free, hot-water-treated seed (50°C for 25 minutes).",
                "Avoid overhead irrigation and working in wet fields to minimise spread.",
                "Remove and destroy infected plant debris promptly.",
                "Rotate away from tomato, pepper, and eggplant for 2+ years.",
                "Plant in raised beds with plastic mulch to prevent rain-splash of soil.",
            ],
        },
    },

    "tomato_bacterial_wilt": {
        "disease": {"common_name": "Tomato Bacterial Wilt", "scientific_name": "Ralstonia solanacearum"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Bacterial (Soilborne)",
        "symptoms": (
            "Rapid wilting of the entire plant while leaves remain green (green wilt). "
            "Cross-section of infected stem shows brown discolouration of vascular ring. "
            "Milky white bacterial streaming observed when cut stem is held in water."
        ),
        "management": {
            "chemical": [
                "No effective chemical control once the plant is infected. Focus on prevention.",
                "Soil drenching with Copper oxychloride (3 g/L) around the root zone as a prophylactic measure.",
                "Biocontrol agent Bacillus subtilis (Serenade ASO @ 4 mL/L) applied as soil drench and foliar spray.",
                "Pseudomonas fluorescens (Pf-1 @ 10 g/kg seed as seed treatment + 2.5 kg/ha as soil application).",
            ],
            "preventive": [
                "CRITICAL: Solarise soil for 4–6 weeks using transparent polythene under full sun.",
                "Graft susceptible varieties onto resistant rootstocks (e.g., Solanum torvum, AVTO1331).",
                "Remove and bag infected plants immediately; never compost them.",
                "Avoid waterlogging — the bacterium thrives in saturated soils.",
                "Rotate with non-solanaceous crops (cereals, legumes) for minimum 3 years.",
                "Sterilise all farm equipment and stakes with formaldehyde (2%) before reuse.",
            ],
        },
    },

    "tomato_brown_spots": {
        "disease": {"common_name": "Tomato Brown Spots (Stemphylium Leaf Spot)", "scientific_name": "Stemphylium solani"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Small, water-soaked spots on leaves turning brown with a yellow to olive-green halo. "
            "Lesions are circular to elongated (2–5 mm) with a papery texture at maturity. "
            "Severe infection causes significant defoliation."
        ),
        "management": {
            "chemical": [
                "Mancozeb (Dithane M-45 @ 2.5 g/L) as a protectant spray every 10 days.",
                "Iprodione (Rovral 50 WP @ 2.0 g/L) is highly effective against Stemphylium.",
                "Chlorothalonil (Kavach @ 2.0 g/L) applied preventively in humid conditions.",
                "Azoxystrobin (Amistar 25 SC @ 1.0 mL/L) for integrated management.",
            ],
            "preventive": [
                "Avoid prolonged leaf wetness through efficient irrigation management.",
                "Improve plant spacing to 45 × 60 cm for adequate airflow.",
                "Remove and destroy lower affected leaves to reduce inoculum load.",
                "Apply Trichoderma viride (4 g/kg seed) as seed treatment.",
            ],
        },
    },

    "tomato_early_blight": {
        "disease": {"common_name": "Tomato Early Blight", "scientific_name": "Alternaria solani"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Dark brown, circular lesions with target-board concentric rings on older leaves. "
            "Yellow halo surrounds each lesion. Lesions coalesce causing leaf yellowing and drop. "
            "Dark, sunken, concentric lesions may appear on stem (collar rot) and fruit."
        ),
        "management": {
            "chemical": [
                "Mancozeb (Dithane M-45 @ 2.5 g/L) — best first-choice protectant; spray every 7 days.",
                "Chlorothalonil (Bravo 720 SC @ 2.0 mL/L) for wet-season protection.",
                "Difenoconazole (Score 250 EC @ 0.5 mL/L) for curative control at symptom onset.",
                "Azoxystrobin + Difenoconazole (Amistar Top @ 0.75 mL/L) for both protection and cure.",
            ],
            "preventive": [
                "Use disease-free seedlings; apply Mancozeb seed treatment.",
                "Stake plants for improved airflow and reduced foliage contact with soil.",
                "Avoid wetting foliage; use drip irrigation.",
                "Rotate tomatoes with non-solanaceous crops for 2+ years.",
                "Apply mulch to prevent soil-splash transmission.",
            ],
        },
    },

    "tomato_late_blight": {
        "disease": {"common_name": "Tomato Late Blight", "scientific_name": "Phytophthora infestans"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Oomycete (Water Mould)",
        "symptoms": (
            "Large, irregular, water-soaked, greasy lesions on leaves that rapidly turn brown. "
            "White cottony sporulation on lower leaf surface in humid weather. "
            "Fruit shows greasy, olive-green to brown patches that rot rapidly. "
            "Stem lesions can kill entire plant branches quickly."
        ),
        "management": {
            "chemical": [
                "Metalaxyl-M + Mancozeb (Ridomil Gold MZ @ 2.5 g/L) — first choice for confirmed late blight.",
                "Cymoxanil + Mancozeb (Curzate @ 2.5 g/L) — curative within 72 hours of infection.",
                "Fluopicolide + Propamocarb (Infinito @ 1.6 mL/L) — highly systemic; use at high disease pressure.",
                "Mandipropamid (Revus @ 0.6 mL/L) — different mode of action; valuable in rotation.",
            ],
            "preventive": [
                "Monitor weather closely; spray before expected rain and cool, foggy nights.",
                "Remove and destroy infected leaves and fruit immediately; do not compost.",
                "Maintain 60 × 45 cm spacing and stake plants to improve airflow.",
                "Do not irrigate in the evenings — extended leaf wetness accelerates spread.",
                "Use tolerant varieties (IIHR-55, Arka Rakshak) where available.",
            ],
        },
    },

    "tomato_leaf_mold": {
        "disease": {"common_name": "Tomato Leaf Mold", "scientific_name": "Passalora fulva (syn. Cladosporium fulvum)"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Pale green to yellow spots on upper leaf surface. "
            "Olive-green to grayish-purple velvety mold on the corresponding lower surface. "
            "Infected leaves turn yellow, wither, and drop. Common in greenhouses and tunnels."
        ),
        "management": {
            "chemical": [
                "Mancozeb (Dithane M-45 @ 2.5 g/L) as a protectant; spray every 7–10 days.",
                "Iprodione (Rovral 50 WP @ 2.0 g/L) — very effective against this pathogen.",
                "Chlorothalonil (Kavach @ 2.0 g/L) for wet-season or greenhouse conditions.",
                "Hexaconazole (Contaf 5 EC @ 2 mL/L) for curative management.",
            ],
            "preventive": [
                "Maintain relative humidity below 85% in greenhouses using ventilation fans.",
                "Avoid overcrowding; provide 60 × 45 cm plant spacing.",
                "Remove and destroy infected leaves promptly; never leave them on the floor.",
                "Grow Cf-gene resistant varieties when available (check seed companies).",
                "Sanitise greenhouse structures and stakes with Copper sulfate solution between crops.",
            ],
        },
    },

    "tomato_tomato_mosaic": {
        "disease": {"common_name": "Tomato Mosaic Virus (ToMV)", "scientific_name": "Tomato mosaic tobamovirus"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Viral",
        "symptoms": (
            "Mosaic pattern of light and dark green on leaves (mottling). "
            "Leaves may show distortion, blistering, or fernleaf (narrow, distorted leaves). "
            "Fruit shows uneven ripening, internal browning, and necrotic streaking."
        ),
        "management": {
            "chemical": [
                "No chemical cure for virus. Focus entirely on prevention and rogueing.",
                "Spray insecticide (Imidacloprid 17.8 SL @ 0.5 mL/L) to control aphids that may carry viruses.",
            ],
            "preventive": [
                "Use ToMV-resistant varieties (Tm2/2 gene) — critically important.",
                "Treat seed with 10% trisodium phosphate (TSP) for 15 minutes before washing and drying.",
                "Wash hands thoroughly with soap before handling plants; the virus spreads by contact.",
                "Roguing: remove and destroy infected plants immediately using gloves.",
                "Do not smoke or use tobacco near plants — tobacco mosaic is closely related and can spread.",
                "Sterilise tools with 10% bleach or 70% alcohol solution between uses.",
            ],
        },
    },

    "tomato_septoria_leaf_spot": {
        "disease": {"common_name": "Tomato Septoria Leaf Spot", "scientific_name": "Septoria lycopersici"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Numerous small (1–4 mm), circular spots with dark brown margins and gray-white centres on lower leaves. "
            "Tiny black pycnidia (spore bodies) visible inside lesions with a hand lens. "
            "Lesions begin on lower leaves and move upward; severe defoliation weakens plants."
        ),
        "management": {
            "chemical": [
                "Mancozeb (Dithane M-45 @ 2.5 g/L) applied every 7 days from first symptom appearance.",
                "Chlorothalonil (Bravo 720 SC @ 2.0 mL/L) — excellent broad-spectrum protectant.",
                "Copper-based fungicides (Copper oxychloride @ 3 g/L) as an organically approved option.",
                "Azoxystrobin (Amistar 25 SC @ 1.0 mL/L) provides systemic and protective control.",
            ],
            "preventive": [
                "Remove infected lower leaves promptly and dispose of — do not compost.",
                "Apply mulch to reduce soil-splash transmission of spores to lower leaves.",
                "Stake plants for adequate airflow and to keep foliage off wet soil.",
                "Avoid overhead irrigation; water at base of plants in the morning.",
                "Rotate with non-solanaceous crops for 2+ years.",
            ],
        },
    },

    "tomato_spider_mites": {
        "disease": {"common_name": "Tomato Spider Mite Damage (Two-Spotted Spider Mite)", "scientific_name": "Tetranychus urticae"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Arachnid Pest",
        "symptoms": (
            "Fine, bronze or yellow stippling on upper leaf surface. "
            "Webbing on the underside of leaves and between leaves. "
            "Severely infested leaves turn yellow, dry up, and drop. Hot dry weather favours rapid population buildup."
        ),
        "management": {
            "chemical": [
                "Abamectin (Vertimec 1.8 EC @ 0.5 mL/L) — highly effective; target undersides of leaves.",
                "Spiromesifen (Oberon 22.9 SC @ 1 mL/L) — disrupts mite development and egg hatch.",
                "Fenpyroximate (Sedan 5 EC @ 1.5 mL/L) provides rapid knockdown.",
                "Hexythiazox (Nissorun 10 EC @ 1 mL/L) for ovicidal (egg-killing) activity.",
                "Rotate between modes of action to prevent resistance development.",
            ],
            "preventive": [
                "Maintain adequate soil moisture; drought-stressed plants are more susceptible.",
                "Introduce predatory mites (Phytoseiulus persimilis) for biological control.",
                "Avoid dusty field conditions that promote mite outbreaks.",
                "Remove heavily infested leaves and bag them before disposal.",
                "Monitor closely in hot, dry periods by inspecting leaf undersides with a hand lens.",
            ],
        },
    },

    "tomato_target_spot": {
        "disease": {"common_name": "Tomato Target Spot", "scientific_name": "Corynespora cassiicola"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Fungal",
        "symptoms": (
            "Circular lesions on leaves with concentric dark and light rings (resembling a target). "
            "Lesions have a yellow halo; centres may fall out creating a 'shot-hole' effect. "
            "Spots on fruit are dark, sunken, and corky. More common in tropical and subtropical climates."
        ),
        "management": {
            "chemical": [
                "Difenoconazole (Score 250 EC @ 0.5 mL/L) provides excellent control.",
                "Pyraclostrobin (Cabrio EG @ 1.5 g/L) for protectant and curative activity.",
                "Azoxystrobin + Propiconazole (Quilt Xcel @ 0.75 mL/L) for broad-spectrum control.",
                "Mancozeb (Dithane M-45 @ 2.5 g/L) as first-line protectant spray.",
            ],
            "preventive": [
                "Stake and prune plants for maximum airflow and reduced humidity.",
                "Remove and destroy infected crop debris promptly after harvest.",
                "Avoid excessive nitrogen fertilisation; well-balanced nutrition reduces susceptibility.",
                "Rotate with cereal or legume crops for 2+ years.",
            ],
        },
    },

    "tomato_tomato_leaf_curl": {
        "disease": {"common_name": "Tomato Yellow Leaf Curl Virus (TYLCV)", "scientific_name": "Tomato yellow leaf curl virus"},
        "crop":    {"common_name": "Tomato"},
        "pathogen_type": "Viral (Whitefly-transmitted)",
        "symptoms": (
            "Upward curling and yellowing of leaves, especially young leaves at the growing tip. "
            "Severe stunting of the plant; inter-veinal chlorosis and leaf margin yellowing. "
            "Flowers may drop and fruit set is severely reduced. Transmitted by silverleaf whitefly (Bemisia tabaci)."
        ),
        "management": {
            "chemical": [
                "Target the whitefly vector: Imidacloprid (Confidor 200 SL @ 0.5 mL/L) as soil drench at transplanting.",
                "Thiamethoxam (Actara 25 WG @ 0.3 g/L) as foliar spray for adult whitefly control.",
                "Dinotefuran (Oshin 20 SG @ 0.5 g/L) for systemic whitefly management.",
                "Buprofezin (Applaud 25 SC @ 1.5 mL/L) for nymph suppression.",
            ],
            "preventive": [
                "CRITICAL: Plant virus-resistant varieties (Ty-gene, e.g., Syngenta TY series, Arka Samrat).",
                "Use insect-proof nurseries with 50-mesh nets for seedling production.",
                "Install yellow sticky traps in the field to monitor and mass-trap whiteflies.",
                "Apply reflective silver mulch to repel whiteflies from landing on young plants.",
                "Remove and destroy infected plants immediately to prevent further spread.",
                "Maintain a 2-week whitefly-free period in nurseries using neonicotinoid seed treatment.",
            ],
        },
    },
}

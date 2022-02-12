"""
createPokémon.team - web application that helps you build your own
Pokémon team in any core series game
Copyright © 2019  Mirek Długosz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
any later version.
"""


# Pokemon that were added in second game in generation
# This omits gen 3, where deoxys situation is little more complicated
# It also omits many Pokemon which we don't care about anyway, such as
# Spiky-eared Pichu, forces of nature Therian formes etc.
GEN4_ADDITIONS = ["rotomheat", "rotomwash", "rotomfrost", "rotomfan", "rotommow",
                  "giratinaorigin", "shayminsky"]

GEN5_ADDITIONS = ["kyuremblack", "kyuremwhite"]

GEN6_ADDITIONS = ["beedrillmega", "pidgeotmega", "slowbromega", "steelixmega",
                  "sceptilemega", "swampertmega", "sableyemega", "sharpedomega",
                  "cameruptmega", "altariamega", "glaliemega", "salamencemega",
                  "metagrossmega", "rayquazamega", "lopunnymega", "gallademega",
                  "audinomega", "dianciemega", "kyogreprimal", "groudonprimal"]

GEN7_ADDITIONS = ["lycanrocdusk", "necrozmaduskmane", "necrozmadawnwings",
                  "necrozmaultra", "poipole", "naganadel", "stakataka",
                  "blacephalon", "zeraora"]

# List of Pokemon available in each game. This is required, since Game Freak
# broke the assumption that all Pokemon available in previous game/generation
# are available in new game/generation as well
# It's part of constants, but sheer size caused it to be moved to separate file
GEN1_DEX = ["bulbasaur", "ivysaur", "venusaur", "charmander",
            "charmeleon", "charizard", "squirtle", "wartortle", "blastoise",
            "caterpie", "metapod", "butterfree", "weedle", "kakuna",
            "beedrill", "pidgey", "pidgeotto", "pidgeot", "rattata",
            "raticate", "spearow", "fearow", "ekans", "arbok", "pikachu",
            "raichu", "sandshrew", "sandslash", "nidoranf", "nidorina",
            "nidoqueen", "nidoranm", "nidorino", "nidoking", "clefairy",
            "clefable", "vulpix", "ninetales", "jigglypuff", "wigglytuff",
            "zubat", "golbat", "oddish", "gloom", "vileplume", "paras",
            "parasect", "venonat", "venomoth", "diglett", "dugtrio",
            "meowth", "persian", "psyduck", "golduck", "mankey", "primeape",
            "growlithe", "arcanine", "poliwag", "poliwhirl", "poliwrath",
            "abra", "kadabra", "alakazam", "machop", "machoke", "machamp",
            "bellsprout", "weepinbell", "victreebel", "tentacool",
            "tentacruel", "geodude", "graveler", "golem", "ponyta",
            "rapidash", "slowpoke", "slowbro", "magnemite", "magneton",
            "farfetchd", "doduo", "dodrio", "seel", "dewgong", "grimer",
            "muk", "shellder", "cloyster", "gastly", "haunter", "gengar",
            "onix", "drowzee", "hypno", "krabby", "kingler", "voltorb",
            "electrode", "exeggcute", "exeggutor", "cubone", "marowak",
            "hitmonlee", "hitmonchan", "lickitung", "koffing", "weezing",
            "rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan", "horsea",
            "seadra", "goldeen", "seaking", "staryu", "starmie", "mrmime",
            "scyther", "jynx", "electabuzz", "magmar", "pinsir", "tauros",
            "magikarp", "gyarados", "lapras", "ditto", "eevee", "vaporeon",
            "jolteon", "flareon", "porygon", "omanyte", "omastar", "kabuto",
            "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos",
            "moltres", "dratini", "dragonair", "dragonite", "mewtwo", "mew"]
GEN2_DEX = GEN1_DEX + ["chikorita", "bayleef", "meganium", "cyndaquil", "quilava",
            "typhlosion", "totodile", "croconaw", "feraligatr", "sentret",
            "furret", "hoothoot", "noctowl", "ledyba", "ledian", "spinarak",
            "ariados", "crobat", "chinchou", "lanturn", "pichu", "cleffa",
            "igglybuff", "togepi", "togetic", "natu", "xatu", "mareep",
            "flaaffy", "ampharos", "bellossom", "marill", "azumarill",
            "sudowoodo", "politoed", "hoppip", "skiploom", "jumpluff",
            "aipom", "sunkern", "sunflora", "yanma", "wooper", "quagsire",
            "espeon", "umbreon", "murkrow", "slowking", "misdreavus", "unown",
            "wobbuffet", "girafarig", "pineco", "forretress", "dunsparce",
            "gligar", "steelix", "snubbull", "granbull", "qwilfish", "scizor",
            "shuckle", "heracross", "sneasel", "teddiursa", "ursaring",
            "slugma", "magcargo", "swinub", "piloswine", "corsola", "remoraid",
            "octillery", "delibird", "mantine", "skarmory", "houndour",
            "houndoom", "kingdra", "phanpy", "donphan", "porygon2", "stantler",
            "smeargle", "tyrogue", "hitmontop", "smoochum", "elekid", "magby",
            "miltank", "blissey", "raikou", "entei", "suicune", "larvitar",
            "pupitar", "tyranitar", "lugia", "hooh", "celebi"]
GEN3_DEX = GEN2_DEX + ["treecko", "grovyle", "sceptile", "torchic", "combusken",
            "blaziken", "mudkip", "marshtomp", "swampert", "poochyena",
            "mightyena", "zigzagoon", "linoone", "wurmple", "silcoon",
            "beautifly", "cascoon", "dustox", "lotad", "lombre", "ludicolo",
            "seedot", "nuzleaf", "shiftry", "taillow", "swellow", "wingull",
            "pelipper", "ralts", "kirlia", "gardevoir", "surskit",
            "masquerain", "shroomish", "breloom", "slakoth", "vigoroth",
            "slaking", "nincada", "ninjask", "shedinja", "whismur", "loudred",
            "exploud", "makuhita", "hariyama", "azurill", "nosepass",
            "skitty", "delcatty", "sableye", "mawile", "aron", "lairon",
            "aggron", "meditite", "medicham", "electrike", "manectric",
            "plusle", "minun", "volbeat", "illumise", "roselia", "gulpin",
            "swalot", "carvanha", "sharpedo", "wailmer", "wailord", "numel",
            "camerupt", "torkoal", "spoink", "grumpig", "spinda", "trapinch",
            "vibrava", "flygon", "cacnea", "cacturne", "swablu", "altaria",
            "zangoose", "seviper", "lunatone", "solrock", "barboach",
            "whiscash", "corphish", "crawdaunt", "baltoy", "claydol",
            "lileep", "cradily", "anorith", "armaldo", "feebas", "milotic",
            "castform", "kecleon", "shuppet", "banette", "duskull", "dusclops",
            "tropius", "chimecho", "absol", "wynaut", "snorunt", "glalie",
            "spheal", "sealeo", "walrein", "clamperl", "huntail", "gorebyss",
            "relicanth", "luvdisc", "bagon", "shelgon", "salamence", "beldum",
            "metang", "metagross", "regirock", "regice", "registeel",
            "latias", "latios", "kyogre", "groudon", "rayquaza", "jirachi"]
GEN4_DEX = GEN3_DEX + ["deoxys", "deoxysattack", "deoxysdefense",
            "deoxysspeed"] + ["turtwig", "grotle", "torterra", "chimchar",
            "monferno", "infernape", "piplup", "prinplup", "empoleon",
            "starly", "staravia", "staraptor", "bidoof", "bibarel",
            "kricketot", "kricketune", "shinx", "luxio", "luxray", "budew",
            "roserade", "cranidos", "rampardos", "shieldon", "bastiodon",
            "burmy", "wormadam", "wormadamsandy", "wormadamtrash",
            "mothim", "combee", "vespiquen", "pachirisu", "buizel",
            "floatzel", "cherubi", "cherrim", "shellos", "gastrodon",
            "ambipom", "drifloon", "drifblim", "buneary", "lopunny",
            "mismagius", "honchkrow", "glameow", "purugly", "chingling",
            "stunky", "skuntank", "bronzor", "bronzong", "bonsly", "mimejr",
            "happiny", "chatot", "spiritomb", "gible", "gabite", "garchomp",
            "munchlax", "riolu", "lucario", "hippopotas", "hippowdon",
            "skorupi", "drapion", "croagunk", "toxicroak", "carnivine",
            "finneon", "lumineon", "mantyke", "snover", "abomasnow",
            "weavile", "magnezone", "lickilicky", "rhyperior", "tangrowth",
            "electivire", "magmortar", "togekiss", "yanmega", "leafeon",
            "glaceon", "gliscor", "mamoswine", "porygonz", "gallade",
            "probopass", "dusknoir", "froslass", "rotom", "uxie",
            "mesprit", "azelf", "dialga", "palkia", "heatran", "regigigas",
            "giratina", "cresselia", "phione", "manaphy", "darkrai",
            "shaymin", "arceus", "arceusbug", "arceusdark", "arceusdragon",
            "arceuselectric", "arceusfighting", "arceusfire", "arceusflying",
            "arceusghost", "arceusgrass", "arceusground", "arceusice",
            "arceuspoison", "arceuspsychic", "arceusrock", "arceussteel",
            "arceuswater"]
GEN5_DEX = GEN4_DEX + GEN4_ADDITIONS + ["victini", "snivy", "servine",
            "serperior", "tepig", "pignite", "emboar", "oshawott",
            "dewott", "samurott", "patrat", "watchog", "lillipup",
            "herdier", "stoutland", "purrloin", "liepard", "pansage",
            "simisage", "pansear", "simisear", "panpour", "simipour",
            "munna", "musharna", "pidove", "tranquill", "unfezant",
            "blitzle", "zebstrika", "roggenrola", "boldore", "gigalith",
            "woobat", "swoobat", "drilbur", "excadrill", "audino", "timburr",
            "gurdurr", "conkeldurr", "tympole", "palpitoad", "seismitoad",
            "throh", "sawk", "sewaddle", "swadloon", "leavanny", "venipede",
            "whirlipede", "scolipede", "cottonee", "whimsicott", "petilil",
            "lilligant", "basculin", "sandile", "krokorok", "krookodile",
            "darumaka", "darmanitan", "darmanitanzen", "maractus",
            "dwebble", "crustle", "scraggy", "scrafty", "sigilyph", "yamask",
            "cofagrigus", "tirtouga", "carracosta", "archen", "archeops",
            "trubbish", "garbodor", "zorua", "zoroark", "minccino", "cinccino",
            "gothita", "gothorita", "gothitelle", "solosis", "duosion",
            "reuniclus", "ducklett", "swanna", "vanillite", "vanillish",
            "vanilluxe", "deerling", "sawsbuck", "emolga", "karrablast",
            "escavalier", "foongus", "amoonguss", "frillish", "jellicent",
            "alomomola", "joltik", "galvantula", "ferroseed", "ferrothorn",
            "klink", "klang", "klinklang", "tynamo", "eelektrik", "eelektross",
            "elgyem", "beheeyem", "litwick", "lampent", "chandelure", "axew",
            "fraxure", "haxorus", "cubchoo", "beartic", "cryogonal", "shelmet",
            "accelgor", "stunfisk", "mienfoo", "mienshao", "druddigon",
            "golett", "golurk", "pawniard", "bisharp", "bouffalant", "rufflet",
            "braviary", "vullaby", "mandibuzz", "heatmor", "durant", "deino",
            "zweilous", "hydreigon", "larvesta", "volcarona", "cobalion",
            "terrakion", "virizion", "tornadus", "thundurus", "reshiram",
            "zekrom", "landorus", "kyurem",
            "keldeo", "meloetta", "meloettapirouette", "genesect",
            "genesectdouse", "genesectshock", "genesectburn", "genesectchill"]
GEN6_DEX = GEN5_DEX + GEN5_ADDITIONS + ["chespin", "quilladin", "chesnaught",
            "fennekin", "braixen", "delphox", "froakie", "frogadier",
            "greninja", "bunnelby", "diggersby", "fletchling", "fletchinder",
            "talonflame", "scatterbug", "spewpa", "vivillon", "litleo",
            "pyroar", "flabebe", "floette", "florges", "skiddo", "gogoat",
            "pancham", "pangoro", "furfrou", "espurr", "meowstic", "meowsticf",
            "honedge", "doublade", "aegislash", "spritzee", "aromatisse",
            "swirlix", "slurpuff", "inkay", "malamar", "binacle", "barbaracle",
            "skrelp", "dragalge", "clauncher", "clawitzer", "helioptile",
            "heliolisk", "tyrunt", "tyrantrum", "amaura", "aurorus", "sylveon",
            "hawlucha", "dedenne", "carbink", "goomy", "sliggoo", "goodra",
            "klefki", "phantump", "trevenant", "pumpkaboo", "gourgeist",
            "bergmite", "avalugg", "noibat", "noivern", "xerneas", "yveltal",
            "zygarde", "diancie", "hoopa", "hoopaunbound", "volcanion",
            "arceusfairy", "venusaurmega", "charizardmegax", "charizardmegay",
            "blastoisemega", "alakazammega", "gengarmega", "kangaskhanmega",
            "pinsirmega", "gyaradosmega", "aerodactylmega", "mewtwomegax",
            "mewtwomegay", "ampharosmega", "scizormega", "heracrossmega",
            "houndoommega", "tyranitarmega", "blazikenmega", "gardevoirmega",
            "mawilemega", "aggronmega", "medichammega", "manectricmega",
            "banettemega", "absolmega", "latiasmega", "latiosmega",
            "garchompmega", "lucariomega", "abomasnowmega"]
GEN7_DEX = GEN6_DEX + GEN6_ADDITIONS + ["rowlet", "dartrix", "decidueye",
            "litten", "torracat", "incineroar", "popplio", "brionne",
            "primarina", "pikipek", "trumbeak", "toucannon", "yungoos",
            "gumshoos", "grubbin", "charjabug", "vikavolt", "crabrawler",
            "crabominable", "oricorio", "oricoriopompom", "oricoriopau",
            "oricoriosensu", "cutiefly", "ribombee", "rockruff", "lycanroc",
            "lycanrocmidnight", "wishiwashi", "mareanie", "toxapex", "mudbray",
            "mudsdale", "dewpider", "araquanid", "fomantis", "lurantis",
            "morelull", "shiinotic", "salandit", "salazzle", "stufful",
            "bewear", "bounsweet", "steenee", "tsareena", "comfey", "oranguru",
            "passimian", "wimpod", "golisopod", "sandygast", "palossand",
            "pyukumuku", "typenull", "silvally", "silvallybug", "silvallydark",
            "silvallydragon", "silvallyelectric", "silvallyfairy",
            "silvallyfighting", "silvallyfire", "silvallyflying",
            "silvallyghost", "silvallygrass", "silvallyground", "silvallyice",
            "silvallypoison", "silvallypsychic", "silvallyrock",
            "silvallysteel", "silvallywater", "minior", "komala",
            "turtonator", "togedemaru", "mimikyu", "bruxish", "drampa",
            "dhelmise", "jangmoo", "hakamoo", "kommoo", "tapukoko", "tapulele",
            "tapubulu", "tapufini", "cosmog", "cosmoem", "solgaleo", "lunala",
            "nihilego", "buzzwole", "pheromosa", "xurkitree", "celesteela",
            "kartana", "guzzlord", "necrozma", "magearna", "marshadow",
            "rattataalola", "raticatealola", "raichualola", "sandshrewalola",
            "sandslashalola", "vulpixalola", "ninetalesalola", "diglettalola",
            "dugtrioalola", "meowthalola", "persianalola", "geodudealola",
            "graveleralola", "golemalola", "grimeralola", "mukalola",
            "exeggutoralola", "marowakalola"]
GEN8_DEX = ["grookey", "thwackey", "rillaboom", "scorbunny", "raboot",
            "cinderace", "sobble", "drizzile", "inteleon", "blipbug",
            "dottler", "orbeetle", "caterpie", "metapod", "butterfree",
            "grubbin", "charjabug", "vikavolt", "hoothoot", "noctowl",
            "rookidee", "corvisquire", "corviknight", "skwovet", "greedent",
            "pidove", "tranquill", "unfezant", "nickit", "thievul",
            "zigzagoon", "zigzagoongalar", "linoone", "linoonegalar",
            "obstagoon", "wooloo", "dubwool", "lotad", "lombre", "ludicolo",
            "seedot", "nuzleaf", "shiftry", "chewtle", "drednaw", "purrloin",
            "liepard", "yamper", "boltund", "bunnelby", "diggersby",
            "minccino", "cinccino", "bounsweet", "steenee", "tsareena",
            "oddish", "gloom", "vileplume", "bellossom", "budew", "roselia",
            "roserade", "wingull", "pelipper", "joltik", "galvantula",
            "electrike", "manectric", "vulpix", "ninetales", "vulpixalola",
            "ninetalesalola", "growlithe", "arcanine", "vanillite",
            "vanillish", "vanilluxe", "swinub", "piloswine", "mamoswine",
            "delibird", "snorunt", "glalie", "froslass", "baltoy", "claydol",
            "mudbray", "mudsdale", "dwebble", "crustle", "golett", "golurk",
            "munna", "musharna", "natu", "xatu", "stufful", "bewear", "snover",
            "abomasnow", "krabby", "kingler", "wooper", "quagsire", "corphish",
            "crawdaunt", "nincada", "ninjask", "shedinja", "tyrogue",
            "hitmonlee", "hitmonchan", "hitmontop", "pancham", "pangoro",
            "klink", "klang", "klinklang", "combee", "vespiquen", "bronzor",
            "bronzong", "ralts", "kirlia", "gardevoir", "gallade", "drifloon",
            "drifblim", "gossifleur", "eldegoss", "cherubi", "cherrim",
            "stunky", "skuntank", "tympole", "palpitoad", "seismitoad",
            "duskull", "dusclops", "dusknoir", "machop", "machoke", "machamp",
            "gastly", "haunter", "gengar", "magikarp", "gyarados", "goldeen",
            "seaking", "remoraid", "octillery", "shellder", "cloyster",
            "feebas", "milotic", "basculin", "wishiwashi", "pyukumuku",
            "trubbish", "garbodor", "sizzlipede", "centiskorch", "rolycoly",
            "carkol", "coalossal", "diglett", "dugtrio", "diglettalola",
            "dugtrioalola", "drilbur", "excadrill", "roggenrola",
            "boldore", "gigalith", "timburr", "gurdurr", "conkeldurr",
            "woobat", "swoobat", "noibat", "noivern", "onix", "steelix",
            "arrokuda", "barraskewda", "meowth", "meowthgalar", "meowthalola",
            "perrserker", "persian", "persianalola", "milcery", "alcremie",
            "cutiefly", "ribombee", "ferroseed", "ferrothorn", "pumpkaboo",
            "gourgeist", "pichu", "pikachu", "raichu", "raichualola", "eevee",
            "vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon",
            "glaceon", "sylveon", "applin", "flapple", "appletun", "espurr",
            "meowstic", "meowsticf", "swirlix", "slurpuff", "spritzee",
            "aromatisse", "dewpider", "araquanid", "wynaut", "wobbuffet",
            "farfetchd", "farfetchdgalar", "sirfetchd", "chinchou", "lanturn",
            "croagunk", "toxicroak", "scraggy", "scrafty", "stunfisk",
            "stunfiskgalar", "shuckle", "barboach", "whiscash", "shellos",
            "gastrodon", "wimpod", "golisopod", "binacle", "barbaracle",
            "corsola", "corsolagalar", "cursola", "impidimp", "morgrem",
            "grimmsnarl", "hatenna", "hattrem", "hatterene", "salandit",
            "salazzle", "pawniard", "bisharp", "throh", "sawk", "koffing",
            "weezinggalar", "weezing", "bonsly", "sudowoodo", "cleffa",
            "clefairy", "clefable", "togepi", "togetic", "togekiss",
            "munchlax", "snorlax", "cottonee", "whimsicott", "rhyhorn",
            "rhydon", "rhyperior", "gothita", "gothorita", "gothitelle",
            "solosis", "duosion", "reuniclus", "karrablast", "escavalier",
            "shelmet", "accelgor", "elgyem", "beheeyem", "cubchoo",
            "beartic", "rufflet", "braviary", "vullaby", "mandibuzz",
            "skorupi", "drapion", "litwick", "lampent", "chandelure", "inkay",
            "malamar", "sneasel", "weavile", "sableye", "mawile", "maractus",
            "sigilyph", "riolu", "lucario", "torkoal", "mimikyu", "cufant",
            "copperajah", "qwilfish", "frillish", "jellicent", "mareanie",
            "toxapex", "cramorant", "toxel", "toxtricity", "toxtricitylowkey",
            "silicobra", "sandaconda", "hippopotas", "hippowdon", "durant",
            "heatmor", "helioptile", "heliolisk", "hawlucha", "trapinch",
            "vibrava", "flygon", "axew", "fraxure", "haxorus", "yamask",
            "yamaskgalar", "runerigus", "cofagrigus", "honedge", "doublade",
            "aegislash", "ponyta", "ponytagalar", "rapidash", "rapidashgalar",
            "sinistea", "polteageist", "indeedee", "indeedeef", "phantump",
            "trevenant", "morelull", "shiinotic", "oranguru", "passimian",
            "morpeko", "falinks", "drampa", "turtonator", "togedemaru", "snom",
            "frosmoth", "clobbopus", "grapploct", "pincurchin", "mantyke",
            "mantine", "wailmer", "wailord", "bergmite", "avalugg", "dhelmise",
            "lapras", "lunatone", "solrock", "mimejr", "mrmimegalar", "mrrime",
            "darumaka", "darumakagalar", "darmanitan", "darmanitanzen",
            "darmanitangalar", "darmanitangalarzen", "stonjourner", "eiscue",
            "duraludon", "rotom", "rotomheat", "rotomwash", "rotomfrost",
            "rotomfan", "rotommow", "ditto", "dracozolt", "arctozolt",
            "dracovish", "arctovish", "charmander", "charmeleon", "charizard",
            "typenull", "silvally", "silvallybug", "silvallydark",
            "silvallydragon", "silvallyelectric", "silvallyfairy",
            "silvallyfighting", "silvallyfire", "silvallyflying",
            "silvallyghost", "silvallygrass", "silvallyground", "silvallyice",
            "silvallypoison", "silvallypsychic", "silvallyrock",
            "silvallysteel", "silvallywater", "larvitar", "pupitar",
            "tyranitar", "deino", "zweilous", "hydreigon", "goomy",
            "sliggoo", "goodra", "jangmoo", "hakamoo", "kommoo", "dreepy",
            "drakloak", "dragapult", "zacian", "zaciancrowned", "zamazenta",
            "zamazentacrowned", "eternatus", "slowpoke", "slowpokegalar",
            "slowbro", "slowbrogalar", "slowking", "slowkinggalar",
            "bulbasaur", "ivysaur", "venusaur", "squirtle", "wartortle",
            "blastoise", "mew", "mewtwo", "celebi", "jirachi", "cobalion",
            "terrakion", "virizion", "reshiram", "zekrom", "kyurem",
            "kyuremblack", "kyuremwhite", "keldeo", "rowlet", "dartrix",
            "decidueye", "litten", "torracat", "incineroar", "popplio",
            "brionne", "primarina", "cosmog", "cosmoem", "solgaleo",
            "lunala", "necrozma", "necrozmaduskmane", "necrozmadawnwings",
            "marshadow", "zeraora", "meltan", "melmetal", "buneary",
            "lopunny", "happiny", "chansey", "blissey", "igglybuff",
            "jigglypuff", "wigglytuff", "fomantis", "lurantis",
            "fletchling", "fletchinder", "talonflame", "shinx", "luxio",
            "luxray", "klefki", "abra", "kadabra", "alakazam", "tentacool",
            "tentacruel", "dunsparce", "bouffalant", "lickitung", "lickilicky",
            "druddigon", "venipede", "whirlipede", "scolipede", "foongus",
            "amoonguss", "comfey", "tangela", "tangrowth", "zorua",
            "zoroark", "staryu", "starmie", "emolga", "dedenne", "magnemite",
            "magneton", "magnezone", "carvanha", "sharpedo", "lillipup",
            "herdier", "stoutland", "tauros", "miltank", "scyther",
            "scizor", "pinsir", "heracross", "sandygast", "palossand",
            "azurill", "marill", "azumarill", "poliwag", "poliwhirl",
            "poliwrath", "politoed", "psyduck", "golduck", "whismur",
            "loudred", "exploud", "skarmory", "rockruff", "lycanroc",
            "lycanrocmidnight", "lycanrocdusk", "mienfoo", "mienshao",
            "sandshrew", "sandshrewalola", "sandslash", "sandslashalola",
            "cubone", "marowak", "marowakalola", "kangaskhan", "sandile",
            "krokorok", "krookodile", "larvesta", "volcarona", "skrelp",
            "dragalge", "clauncher", "clawitzer", "horsea", "seadra",
            "kingdra", "petilil", "lilligant", "exeggcute", "exeggutor",
            "exeggutoralola", "porygon", "porygon2", "porygonz", "magearna",
            "kubfu", "urshifu", "urshifurapidstrike", "zarude", "nidoranf",
            "nidorina", "nidoqueen", "nidoranm", "nidorino", "nidoking",
            "zubat", "golbat", "crobat", "jynx", "smoochum", "electabuzz",
            "magmar", "elekid", "magby", "electivire", "magmortar",
            "omanyte", "omastar", "kabuto", "kabutops", "aerodactyl",
            "articuno", "articunogalar", "zapdos", "zapdosgalar", "moltres",
            "moltresgalar", "dratini", "dragonair", "dragonite", "raikou",
            "entei", "suicune", "lugia", "hooh", "treecko", "grovyle",
            "sceptile", "torchic", "combusken", "blaziken", "mudkip",
            "marshtomp", "swampert", "aron", "lairon", "aggron", "swablu",
            "altaria", "lileep", "cradily", "anorith", "armaldo", "absol",
            "spheal", "sealeo", "walrein", "relicanth", "bagon", "shelgon",
            "salamence", "beldum", "metang", "metagross", "regirock",
            "regice", "registeel", "regieleki", "regidrago", "latias",
            "latios", "kyogre", "groudon", "rayquaza", "spiritomb", "gible",
            "gabite", "garchomp", "uxie", "mesprit", "azelf", "dialga",
            "palkia", "heatran", "regigigas", "giratina", "giratinaorigin",
            "cresselia", "victini", "audino", "tirtouga", "carracosta",
            "archen", "archeops", "cryogonal", "tornadus", "thundurus",
            "landorus", "genesect", "genesectdouse", "genesectshock",
            "genesectburn", "genesectchill", "tyrunt", "tyrantrum", "amaura",
            "aurorus", "carbink", "xerneas", "yveltal", "zygarde", "diancie",
            "volcanion", "tapukoko", "tapulele", "tapubulu", "tapufini",
            "nihilego", "buzzwole", "pheromosa", "xurkitree", "celesteela",
            "kartana", "guzzlord", "poipole", "naganadel", "stakataka",
            "blacephalon", "glastrier", "spectrier", "calyrex", "calyrexice",
            "calyrexshadow",
            ]


available_pokemon = {
    "red-blue": GEN1_DEX,
    "yellow": GEN1_DEX,
    "gold-silver": GEN2_DEX,
    "crystal": GEN2_DEX,
    "ruby-sapphire": GEN3_DEX + ["deoxys"],
    "emerald": GEN3_DEX + ["deoxysspeed"],
    "firered-leafgreen": GEN3_DEX + ["deoxysattack", "deoxysdefense"],
    "diamond-pearl": GEN4_DEX,
    "platinum": GEN4_DEX + GEN4_ADDITIONS,
    "heartgold-soulsilver": GEN4_DEX + GEN4_ADDITIONS,
    "black-white": GEN5_DEX,
    "black-2-white-2": GEN5_DEX + GEN5_ADDITIONS,
    "x-y": GEN6_DEX,
    "omega-ruby-alpha-sapphire": GEN6_DEX + GEN6_ADDITIONS,
    "sun-moon": GEN7_DEX,
    "ultra-sun-ultra-moon": GEN7_DEX + GEN7_ADDITIONS,
    "sword-shield": GEN8_DEX,
    "brilliant-diamond-shining-pearl": GEN4_DEX + GEN4_ADDITIONS,
}

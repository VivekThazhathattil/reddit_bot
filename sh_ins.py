import random
class Shakespearean_insult:
    def __init__(self) -> None:
        self.adj_1 = [
            "artless",
            "bawdy",
            "beslubbering",
            "bootless",
            "churlish",
            "cockered",
            "clouted",
            "craven",
            "currish",
            "dankish",
            "dissembling",
            "droning",
            "errant",
            "fawning",
            "fobbing",
            "froward",
            "forthy",
            "gleeking",
            "goatish",
            "gorbellied",
            "impertinent",
            "infectious",
            "jarring",
            "loggerheaded",
            "lumpish",
            "mammering",
            "mangled",
            "mewling",
            "paunchy",
            "pribbling",
            "puking",
            "puny",
            "qualling",
            "rank",
            "reeky",
            "roguish",
            "ruttish",
            "saucy",
            "spleeny",
            "spongy",
            "surly",
            "tottering",
            "unmuzzeled",
            "vain",
            "venomed",
            "villainous",
            "warped",
            "wayward",
            "weedy",
            "yeasty",
        ]
        self.adj_2 = [
            "base-court",
            "bat-fowling",
            "beef-witted",
            "beetle-headed",
            "boil-brained",
            "clapper-clawed",
            "clay-brained",
            "common-kissing",
            "crook-pated",
            "dismal-dreaming",
            "dizzy-eyed",
            "doghearted",
            "dread-bolted",
            "earth-vexing",
            "elf-skinned",
            "fat-kidneyed",
            "fen-sucked",
            "flap-mouthed",
            "fly-bitten",
            "folly-fallen",
            "fool-born",
            "full-gorged",
            "guts-gripped",
            "half-faced",
            "hasty-witted",
            "hedge-born",
            "hell-hated",
            "idle-headed",
            "ill-breading",
            "ill-nurtured",
            "knotty-pated",
            "milk-livered",
            "motley-minded",
            "onion-eyed",
            "plume-plucked",
            "pottle-deep",
            "pox-marked",
            "reeling-ripe",
            "rough-hewn",
            "rude-growing",
            "rump-fed",
            "shard-borne",
            "sheep-biting",
            "spur-galled",
            "swag-bellied",
            "tardy-gaited",
            "tickle-brained",
            "toad-spotted",
            "unchin-snouted",
            "weather-bitten",
        ]
        self.noun = [
            "apple-john",
            "baggage",
            "barnacle",
            "bladder",
            "boar-pig",
            "bugbear",
            "bum-bailey",
            "canker-blossom",
            "clack-dish",
            "clotpole",
            "coxcomb",
            "codpiece",
            "death-token",
            "deberry",
            "flap-dragon",
            "flax-wench",
            "flirt-gill",
            "foot-licker",
            "fusilarian",
            "giglet",
            "gudgeon",
            "haggard",
            "harpy",
            "hedge-pig",
            "horn-beast",
            "hugger-mugger",
            "joithead",
            "lewdster",
            "lout",
            "maggot-pie",
            "malt-worm",
            "mammet",
            "measle",
            "minnow",
            "mscreant",
            "moldwap",
            "mumble-news",
            "nut-hook",
            "pigeon-egg",
            "pignut",
            "puttock",
            "pumpion",
            "ratsbane",
            "scut",
            "skainsmate",
            "strumpet",
            "varlot",
            "vassal",
            "whey-face",
            "wagtail",
        ]

    def get_insult(self) -> None:
        mes_1 = "Thou " + random.choice(self.adj_1)
        mes_2 = random.choice(self.adj_2)
        mes_3 = random.choice(self.noun)
        return mes_1 + " " +  mes_2 + " " + mes_3

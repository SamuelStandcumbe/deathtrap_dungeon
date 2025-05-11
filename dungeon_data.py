import json

dungeon = {
    "1": {
        "text": (
            "The clamour of the excited spectators gradually fades behind you as you venture deep into "
            "the gloom of the cavern tunnel. Large crystals hang from the tunnel roof at twenty metres "
            "intervals, radiating light, just enough for you to see your way. As your eyes gradually begin "
            "to grow accustomed to the near darkness, you begin to see movement all around. Spiders and "
            "beetles crawling up and down the chiselled walls disappear quickly into cracks and crevices "
            "as they sense your approach; rats and mice scurry along the floor ahead of you. Droplets of "
            "water drips into small pools with an eerie plopping sound which echoes down the tunnel. The "
            "air is cold, moist and dank. After walking slowly along the tunnel for about five minutes, "
            "you arrive at a stone table standing against the wall to your left. On it, there are six boxes, "
            "one of which has your name painted on its lid."
        ),
        "choices": {
            "A": {
                "text": "Open the box",
                "next": "270"
            },
            "B": {
                "text": "Continue Wwalking North",
                "next": "66"
            }
        }
    },
    "2": {
        "text": (
            "The scorpion manages to hold you in its pincers long enough to flick its segmented tail "
            "forward over its head and sting you with its poisonous barbs. Its effect is fatal and you slump "
            "to the ground in the Arena of Death, wondering whether Throm will win through."
        ),
        "choices": {}
    },
    "3": {
        "text": (
            "The gnome shakes his head and says, 'I am afraid you have failed the Trial of Champions. "
            "Baron Sukumvit's Deathtrap Dungeon will keep its secrets for another year, as you will not be "
            "allowed to leave here. You are appointed my servant for the rest of your days, to prepare and "
            "modify the dungeon for future contestants. Perhaps in another life, you will succeed...'"
        ),
        "choices": {}
    },
    "4": {
        "text": (
            "In the total darkness, you do not see the pipe's downward turn. You slip and, unable to get a grip "
            "on the slimy pipe, slide over the edge. Your screams echo down the pipe as you fall the fifty "
            "metres to the bottom. You have failed the Trial of Champions."
        ),
        "choices": {}
    },
    "5": {
        "text": (
            "You crawl along the floor and find yourself in the lair of a tribe of TROGLODYTES. As you creep "
            "past them, your scabbard bangs across a rock on the floor. *Test your Luck*."
        ),
        "choices": {
            "A": {
                "text": "Lucky?",
                "next": "185"
            },
            "B": {
                "text": "Unlucky?",
                "next": "395"
            }
        }
    },
    "6": {
        "text": (
            "Knowing that the manticore will fire its spikes in its tail at you, you run for cover behind one "
            "of the pillars. Before you reach it, a volley of spikes flies through the air and one of them sinks "
            "into your arm. Lose 2 STAMINA points. If you are still alive, you waste no time and attack the "
            "manticore with your sword before it has time to unleash more of its deadly spikes."
        ),
        "enemies": {
            "Manticore": {
                "skill": 11,
                "stamina": 11
            }
        },
        "choices": {
            "A": {
                "text": "I won.",
                "next": "364"
            }
        }
    },
    "7": {
        "text": (
            "Before you have time to reach a doorway, the boulder is upon you. You cry out in pain and terror as it "
            "crushes you to the floor. Your adventure ends here."
        ),
        "choices": {}
    },
    "8": {
        "text": (
            "The Mirror Demon grabs you by the wrist. Immediately it begins to pull you towards the mirror. Its strength "
            "is incredible, and, despite all your efforts, you cannot prevent it from pulling you relentlessly towards "
            "the mirror. When it touches the mirror it seems to disappear straight through it. With horror, you see your "
            "own arm disappears, followed by the rest of your body. You are now in a mirror world of another dimension, "
            "from which you can never return."
        ),
        "choices": {}
    },
    "9": {
        "text": (
            "The Hobgoblins have nothing of any use to you on them, so you decide to open the bag on the floor. Inside "
            "you find a corked earthenware jug. You uncork it and sniff at the liquid inside. It smells sharp and acrid."
        ),
        "choices": {
            "A": {
                "text": "Drink some of it.",
                "next": "158"
            },
            "B": {
                "text": "Dip some cloth in it.",
                "next": "375"
            }
        }
    },
    "10": {
        "text": (
            "Still running as fast as you can, you reach into your backpack and pull out the wooden tube. You plan to lie "
            "under the surface of the water, breathing through the tube. With luck, the Troglodytes will assume that you "
            "will be swept to your death downriver as the torrent disappears into the depths of the mountain. You seize the "
            "tube between your teeth and lower yourself into the water. Holding onto one of the underwater bridge pillars, "
            "you keep perfectly still for ten minutes. When you finally think the Troglodytes have finally gone, you rise "
            "to the surface and look around. There is nobody to be seen, so you climb out of the river and cross the bridge "
            "to the northern bank. Any remaining Provisions you have are sodden and inedible. You continue to walk through the "
            "vast cavern until you at last see a tunnel in the far wall. You walk down it until you come to a heavy wooden "
            "door, which is locked."
        ),
        "choices": {
            "A": {
                "text": "I have an iron key to open the door",
                "next": "86"
            },
            "B": {
                "text": "I have no key.",
                "next": "276"
            }
        }
    },
    "11": {
        "text": (
            "You look down and see the crumpled bodies of the Flying Guardians lying motionless on the floor. You start to "
            "prise out the idol's emerald eye with the tip of your sword. At last, it comes free, and you are surprised by its "
            "weight. Hoping that it may be of use later, you put it in your backpack."
        ),
        "choices": {
            "A": {
                "text": "Prise out the right eye.",
                "next": "140"
            },
            "B": {
                "text": "Climb down the idol.",
                "next": "46"
            }
        }
    },
    "12": {
        "text": (
            "The door opens into a large, candle-lit room filled with the most extraordinarily lifelike statues of knights and "
            "warriors. A white-haired old man dressed in tattered rags suddenly jumps out from behind one of the statues and "
            "starts to giggle. Though he looks like a fool, the sparkle in his eyes makes you think there is more to him than "
            "is apparent. In a high-pitched voice he says, 'Oh good, another stone for my garden, I'm glad you have come to "
            "join your friends. Now, I'm a fair man, so I'll ask you a question. If you answer correctly, I'll let you go "
            "free - but if your answer is wrong, I'll turn you to stone!' He starts to chuckle again, obviously pleased with "
            "your arrival."
        ),
        "choices": {
            "A": {
                "text": "Wait for his question.",
                "next": "382"
            },
            "B": {
                "text": "Attack him.",
                "next": "195"
            },
            "C": {
                "text": "Make a run for the door.",
                "next": "250"
            }
        }
    },
    "13": {
        "text": (
            "The tunnel makes a sudden turn to the left and heads north for as far as you can see. The footprints that you are "
            "following start to peter out as the tunnel becomes gradually drier. Soon you are beyond the dripping roof and pools "
            "on the floor. You notice the air becoming hotter and you find yourself panting even though you are walking quite "
            "slowly. In a small recess on the left-hand wall, you see a section of bamboo standing on its end. Lifting it down "
            "you see it is filled with a clear liquid. Your throat is painfully dry and you feel a little dizzy from the heat."
        ),
        "choices": {
            "A": {
                "text": "Drink the liquid.",
                "next": "147"
            },
            "B": {
                "text": "Do not drink it and continue walking North. It's not worth the risk.",
                "next": "182"
            }
        }
    },
    "14": {
        "text": (
            "The tunnel led into a dark chamber covered in thick cobwebs. Clawing your way through them you trip over a wooden "
            "casket."
        ),
        "choices": {
            "A": {
                "text": "Try and open it",
                "next": "157"
            },
            "B": {
                "text": "Leave it alone and continue north",
                "next": "310"
            }
        }
    },
    "15": {
        "text": (
            "A tickling sensation runs down your spine as you crawl carefully out of the room. Back in the tunnel, you heave a sigh "
            "of relief, throw the skull back in the room and slam the door shut."
        ),
        "choices": {
            "A": {
                "text": "Pleased with your good fortune, you set off west again.",
                "next": "74"
            }
        }
    },
    "16": {
        "text": (
            "You just have time to hear the gnome say, 'Three skulls' before a white bolt of energy shoots out from the lock into your "
            "chest, knocking you unconscious. Roll one die, add 1 to the result and reduce your STAMINA by the total. If you are still "
            "alive, you come to and are told by the Gnome to try again. You chose the wrong gems last time, so you won't try that "
            "combination again.\n\n"
            "   A         B         C\n"
            "Emerald   Diamond   Sapphire\n"
            "Diamond   Sapphire  Emerald\n"
            "Sapphire  Emerald   Diamond\n"
            "Emerald   Sapphire  Diamond\n"
            "Diamond   Emerald   Sapphire\n"
            "Sapphire  Diamond   Emerald"
        ),
        "choices": {
            "A": {
                "text": "Enter 'Emerald', 'Diamond', then 'Sapphire'.",
                "next": "16"
            },
            "B": {
                "text": "Enter 'Diamond', 'Sapphire', then 'Emerald'.",
                "next": "392"
            },
            "C": {
                "text": "Enter 'Sapphire', 'Emerald', then 'Diamond'.",
                "next": "177"
            },
            "D": {
                "text": "Enter 'Emerald', 'Sapphire', then 'Diamond'.",
                "next": "287"
            },
            "E": {
                "text": "Enter 'Diamond', 'Emerald', then 'Sapphire'.",
                "next": "132"
            },
            "F": {
                "text": "Enter 'Sapphire', 'Diamond', then 'Emerald'.",
                "next": "249"
            }
        },
        "17": {
            "text": {
                "You are not strong enough to force open the heavy door. The water is now waist-high and you are exhaused from "
                "your efforts. The water level rises quickly and you find youself floating ever upwards until your face is pressed"
                "against the ceiling. You are soon completely immersed and unable to hold your breath any longer. Your adventure "
                "ends here."
            },
            "choices": {}
        }    
    }
}

# Convert dungeon dictionary to JSON format
json_data = json.dumps(dungeon, indent=4)
class Meaning:
    """By passing refactored input this class calculate the meaning of sentence
       Simple algorithm will predict what user want to know
    """

    from difflib import SequenceMatcher

    def __init__(self):
        self.classifier_words = {
            "Craft_question": ['how', 'do', 'does,', 'would', 'can', 'could',
                               'i', 'is', 'be', 'was', 'were', 'to', 'been',
                               'craft', 'crafted', 'make', 'made',
                               'solution', 'recipe',
                               'know', 'about'],
            "Item_question": ['what', 'can', 'could',
                              'i', 'is', 'be',
                              'do', 'did', 'done', 'like', 'for', 'used',
                              'with'],
            "Greeting": ['hi', 'hello', 'good', 'morning', 'afternoon', 'yo',
                         'hey'],
            "Feeling": ['how', 'do', 'you', 'feel', 'are', 'you', 'feeling',
                        'mood', 'what', 'is'],
            "Thanks": ['goodbot', 'good', 'bot', 'thanks', 'thank', 'you', 'nice']
        }

        self.normal_words = [
            'sven', 'how', 'do', 'does,', 'would', 'can', 'could',
            'i', 'is', 'be', 'was', 'were', 'to', 'been',
            'craft', 'crafted', 'make', 'made',
            'solution', 'recipe',
            'know', 'about', 'what', 'can', 'could',
            'i', 'is', 'be',
            'do', 'did', 'done', 'like', 'for', 'used',
            'with', 'hi', 'hello', 'good', 'morning', 'afternoon', 'yo',
            'hey'
        ]

        self.items_names = ["chest",
                            "crafting table",
                            "furnace",
                            "stick",
                            "torches",
                            "wood planks",
                            "axes",
                            "bucket",
                            "carrot on a stick",
                            "clock",
                            "compass",
                            "fishing rod",
                            "flint and steel",
                            "hoes",
                            "map",
                            "pickaxes",
                            "shears",
                            "shovels",
                            "arrow",
                            "bow",
                            "damaged shield",
                            "patterned shield",
                            "shield",
                            "spectral arrow",
                            "swords",
                            "tipped arrow",
                            "boots",
                            "chestplates",
                            "helmets",
                            "leggins",
                            "andesite",
                            "anvil",
                            "beacon",
                            "block of coal",
                            "block of quartz",
                            "block of redstone",
                            "bone block",
                            "bookshelf",
                            "brick block",
                            "chiseled quartz block",
                            "chiseled sandstone",
                            "chiseled stone brick",
                            "clay block",
                            "coarse dirt",
                            "dark prismarine",
                            "diorite",
                            "end stone bricks",
                            "glowstone",
                            "granite",
                            "hay bale",
                            "jack-o-lantern",
                            "magma block",
                            "moss stone",
                            "mossy stone brick",
                            "nether brick",
                            "nether wart block",
                            "pillar quartz block",
                            "polished andesite",
                            "polished diorite",
                            "polished granite",
                            "prismarine",
                            "prismarine bricks",
                            "purpur block",
                            "purpur pillar",
                            "purpur slab",
                            "purpur stairs",
                            "red nether brick",
                            "sandstone",
                            "sea lantern",
                            "slime block",
                            "smooth sandstone",
                            "snow block",
                            "stained clay",
                            "stone brick",
                            "stone slabs",
                            "stone stairs",
                            "tnt",
                            "wood slabs",
                            "wood stairs",
                            "activator rail",
                            "boat",
                            "detector rail",
                            "minecart",
                            "minecart with chest",
                            "minecart with hopper",
                            "minecart with tnt",
                            "powered minecart",
                            "powered rail",
                            "rails",
                            "daylight sensor",
                            "dispenser",
                            "doors",
                            "dropper",
                            "hopper",
                            "iron trapdoor",
                            "jukebox",
                            "lever",
                            "note block",
                            "piston",
                            "pressure plates",
                            "redstone comparator",
                            "redstone lamp",
                            "redstone repeater",
                            "redstone torch",
                            "sticky piston",
                            "stone button",
                            "trapdoor",
                            "trapped chest",
                            "tripwire hook",
                            "weighted pressure plates",
                            "wooden button",
                            "beetroot soup",
                            "bowl",
                            "bread",
                            "cake",
                            "cookie",
                            "enchanted golden apple",
                            "golden apple",
                            "golden carrot",
                            "melon seeds",
                            "mushroom stew",
                            "pumpkin pie",
                            "pumpkin seeds",
                            "rabbit stew",
                            "sugar",
                            "armor stand",
                            "banner",
                            "bed",
                            "book",
                            "book and quill",
                            "carpet",
                            "cobblestone wall",
                            "end crystal",
                            "end rod",
                            "ender chest",
                            "eye of ender",
                            "fence",
                            "fence gate",
                            "fire charge",
                            "firework rocket",
                            "firework star",
                            "flower pot",
                            "glass panes",
                            "gold ingot",
                            "iron bars",
                            "item frame",
                            "ladder",
                            "lead",
                            "leather",
                            "melon block",
                            "mineral block",
                            "minerals",
                            "nether brick fence",
                            "painting",
                            "paper",
                            "sign",
                            "stained glass",
                            "blaze powder",
                            "brewing stand",
                            "cauldron",
                            "enchantment table",
                            "fermented spider eye",
                            "glass bottle",
                            "glistering melon",
                            "gold nugget",
                            "magma cream",
                            "bone meal",
                            "cyan dye",
                            "dandelion yellow dye",
                            "gray dye",
                            "light blue dye",
                            "light gray dye",
                            "lime dye",
                            "magenta dye",
                            "orange dye",
                            "pink dye",
                            "purple dye",
                            "rose red dye",
                            "black wool",
                            "blue wool",
                            "brown wool",
                            "cyan wool",
                            "gray wool",
                            "green wool",
                            "light blue wool",
                            "light gray wool",
                            "lime wool",
                            "magenta wool",
                            "orange wool",
                            "pink wool",
                            "purple wool",
                            "red wool",
                            "wool",
                            "yellow wool"]

    def predict(self, refactored_sentence, unrefactored_sentence):
        """returns list of sentence type, Minecraft item name, and confidence of prediction (percentage)"""
        max_local = 0
        max_global = 0
        final_type = None
        confidence1 = 0
        confidence2 = 0
        for key in self.classifier_words:
            for word in refactored_sentence[0]:
                if word[0] in self.classifier_words.get(key):
                    max_local = max_local + 1 + word[1]
            if max_local > max_global:
                confidence2 = confidence1
                confidence1 = max_local - max_global
                max_global = max_local
                final_type = key
            max_local = 0

        item_name = None
        for item in self.items_names:
            if item in unrefactored_sentence:
                item_name = item
                break

        possible_items = list()
        if item_name is None:
            possible_item_words = list()
            for word in refactored_sentence[0]:
                if word[0] not in self.normal_words:
                    possible_item_words.append(word[0])

            for item in self.items_names:
                if len(possible_items) >= 10:
                    break;
                for word in possible_item_words:
                    if word in item:
                        possible_items.append(item)
                        continue
                    for item_part in item:
                        similarity = self.SequenceMatcher(None, item_part, word).ratio()
                        if similarity > 0.5:
                            possible_items.append(item)
                            break

        confidence_percentage = 100
        if confidence2 is not 0:
            confidence_percentage = confidence_percentage - confidence1 * 100 / confidence2
        return final_type, item_name, confidence_percentage, possible_items

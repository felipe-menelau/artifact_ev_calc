import urllib.request, json
hero_common = ['Ogre Magi', 'Lycan', 'Venomancer', 'Treant Protector', 'Dark Seer', 'Beastmaster', 'Lion', 'Crystal Maiden', 'Bloodseeker', 'Bristleback', 'Zeus', 'Bounty Hunter', 'Phantom Assassin', 'Magnus', 'Ursa', 'Enchantress', 'Sven', 'Skywrath Mage', 'Mazzie', 'Necrophos']
hero_uncommon = ['Rix', 'Viper', 'Timbersaw', 'Luna', 'Legion Commander', 'Sniper', 'Prellex', 'Sorla Khan', 'Winter Wyvern', 'Tidehunter', 'Abaddon', 'Outworld Devourer']
hero_rare = ['Storm Spirit', 'Omniknight', 'Centaur Warrunner', 'Lich', 'Meepo', 'Earthshaker', 'Chen', 'Axe', 'Pugna', 'Tinker', 'Drow Ranger', 'Kanna']
item_common = ['Blade of the Vigil', 'Stonehall Pike', 'Stonehall Plate', 'Barbed Mail', 'Rumusque Vestments', 'Ring of Tarrasque', 'Book of the Dead', 'Broadsword', 'Keenfolk Musket', 'Red Mist Maul', 'Stonehall Cloak', 'Fur-lined Mantle', 'Chainmail', 'Shield of Basilius']
item_uncommon = ['Helm of the Dominator', 'Claymore', "Hero's Cape", 'Platemail', 'Jasper Daggers', 'Claszureme Hourglass', 'Demagicking Maul', 'Keenfolk Plate', "Assassin's Veil", 'Revtel Signet Ring', 'Phase Boots', 'Blink Dagger', 'Obliterating Orb', 'Golden Ticket']
item_rare = ['Wingfall Hammer', 'Shop Deed', 'Apotheosis Blade', 'Bracers of Sacrifice', 'Vesture of the Tyrant', "Nyctasha's Guard", 'Cloak of Endless Carnage', 'Ristul Emblem', 'Poaching Knife', 'Seraphim Shield', 'Shield of Aquila', 'Horn of the Alpha', "Shiva's Guard"]
card_common = ['Clear the Deck', 'Combat Training', 'Bellow', 'Disciple of Nevermore', 'Thunderhide Pack', 'Selfish Cleric', 'Arcane Censure', 'Poised to Strike', "Selemene's Favor", 'Strafing Run', 'Lightning Strike', 'Ventriloquy', 'Cunning Plan', 'Relentless Zombie', 'Satyr Duelist', "Assassin's Apprentice", 'Hip Fire', 'Defensive Stance', 'Foresight', 'Better Late Than Never', 'Sucker Punch', 'Fight Through the Pain', 'Arcane Assault', 'Intimidation', 'Collateral Damage', 'Crippling Blow', 'Bronze Legionnaire', 'Hellbear Crippler', 'Trebuchets', 'Messenger Rookery', 'Rumusque Blessing', 'Arm the Rebellion', 'Payday', 'Pick a Fight', 'Dimensional Portal', 'Buying Time', 'Juke', 'New Orders', "Avernus' Blessing", 'Rebel Decoy', 'Oglodi Vandal', 'Grazing Shot', 'Vhoul Martyr', 'Tower Barrage', 'Slay', 'Ogre Conscript', 'Untested Grunt', 'Iron Fog Goldmine']
card_uncommon = ['Rend Armor', 'Temple of War', 'Rolling Storm', 'Lodestone Demolition', 'Dirty Deeds', 'Iron Branch Protection', 'Forward Charge', 'Howling Mind', 'Enough Magic!', 'Altar of the Mad Moon', 'The Tyler Estate', 'Lost in Time', 'Spot Weakness', 'Cleansing Rite', 'Burning Oil', 'Rebel Instigator', 'Restoration Effort', 'Smeevil Armsmaster', 'Homefield Advantage', 'Keenfolk Turret', '...And One For Me', 'Oglodi Catapult', 'Diabolic Revelation', 'Call the Reserves', 'Legion Standard Bearer', 'Unsupervised Artillery', "Aghanim's Sanctum", 'Defend the Weak', 'Sister of the Veil', 'Troll Soothsayer', 'The Omexe Arena', 'Self Sabotage', 'Thunderstorm', 'Pick Off', 'Stonehall Elite', 'Red Mist Pillager', 'Satyr Magician', 'Smash Their Defenses!', 'Gank', 'Murder Plot', 'Divine Intervention', 'Compel', 'Relentless Pursuit', 'Tyler Estate Censor', 'Smeevil Blacksmith', 'Cursed Satyr', 'Roseleaf Rejuvenator', 'Mist of Avernus', 'Stars Align', 'Defensive Bloom', 'Friendly Fire', 'Steal Strength']
card_rare = ['Fractured Timeline', 'Keenfolk Golem', 'Marrowfell Brawler', 'Path of the Dreamer', 'Path of the Wise', 'Revtel Investments', 'Escape Route', 'Ravenhook', 'Steam Cannon', "Assassin's Shadow", 'Watchtower', 'Revtel Convoy', 'Cheating Death', "Tresdin's Standards", 'Unearthed Secrets', 'Grand Melee', 'Soul of Spring', 'Champion of the Ancient', 'Routed', 'Bitter Enemies', 'The Cover of Night', 'The Oath', 'Caught Unprepared', 'Ravenous Mass', 'Glyph of Confusion', 'Mercenary Exiles', 'Emissary of the Quorum', 'Conflagration', 'Divine Purpose', 'Incarnation of Selemene', 'Path of the Cunning', 'Annihilation', 'Curse of Atrophy', 'Coordinated Assault', 'Spring the Trap', 'At Any Cost', 'Remote Detonation', 'Pit Fighter of Quoidge', 'Rampaging Hellbear', 'Assured Destruction', 'Corrosive Mist', 'Heroic Resolve', 'Wrath of Gold', 'Whispers of Madness', 'Ogre Corpse Tosser', 'Thunderhide Alpha', 'Path of the Bold', 'Raze', 'Rising Anger', 'Bolt of Damocles', 'Fog of War', 'Time of Triumph']
hero_list = ['Lycan', 'Luna', 'Storm Spirit', 'Tinker', 'Outworld Devourer', 'Pugna', 'Lion', 'Dark Seer', 'Omniknight', 'Bristleback', 'Phantom Assassin', 'Prellex', 'Sorla Khan', 'Centaur Warrunner', 'Timbersaw', 'Viper', 'Ursa', 'Drow Ranger', 'Lich', 'Abaddon', 'Zeus', 'Chen', 'Axe', 'Venomancer', 'Bloodseeker', 'Tidehunter', 'Rix', 'Enchantress', 'Ogre Magi', 'Mazzie', 'Sven', 'Crystal Maiden', 'Winter Wyvern', 'Bounty Hunter', 'Beastmaster', 'Sniper', 'Treant Protector', 'Skywrath Mage', 'Legion Commander', 'Necrophos', 'Magnus', 'Meepo', 'Kanna', 'Earthshaker']
price = {}

with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Rarity%5B%5D=tag_Rarity_Common&sort_dir=desc&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    price[entry['name']] = entry['sell_price']/100
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Rarity%5B%5D=tag_Rarity_Uncommon&sort_dir=desc&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    price[entry['name']] = entry['sell_price']/100
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Rarity%5B%5D=tag_Rarity_Rare&sort_dir=desc&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    price[entry['name']] = entry['sell_price']/100

"""
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B0%5D=tag_Hero&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    hero_list.append(entry['name'])
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B%5D=tag_Hero&category_583950_Rarity%5B%5D=tag_Rarity_Common&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    hero_common.append(entry['name'])
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B%5D=tag_Hero&category_583950_Rarity%5B%5D=tag_Rarity_Uncommon&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    hero_uncommon.append(entry['name'])
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B%5D=tag_Hero&category_583950_Rarity%5B%5D=tag_Rarity_Rare&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    hero_rare.append(entry['name'])

with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B%5D=tag_Item&category_583950_Rarity%5B%5D=tag_Rarity_Common&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    item_common.append(entry['name'])
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B%5D=tag_Item&category_583950_Rarity%5B%5D=tag_Rarity_Uncommon&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    item_uncommon.append(entry['name'])
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B%5D=tag_Item&category_583950_Rarity%5B%5D=tag_Rarity_Rare&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    item_rare.append(entry['name'])

with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B%5D=tag_Spell&category_583950_Card_Type%5B%5D=tag_Creep&category_583950_Card_Type%5B%5D=tag_Improvement&category_583950_Rarity%5B%5D=tag_Rarity_Common&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    card_common.append(entry['name'])
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B%5D=tag_Spell&category_583950_Card_Type%5B%5D=tag_Creep&category_583950_Card_Type%5B%5D=tag_Improvement&category_583950_Rarity%5B%5D=tag_Rarity_Uncommon&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    card_uncommon.append(entry['name'])
with urllib.request.urlopen("https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Card_Type%5B%5D=tag_Spell&category_583950_Card_Type%5B%5D=tag_Creep&category_583950_Card_Type%5B%5D=tag_Improvement&category_583950_Rarity%5B%5D=tag_Rarity_Rare&appid=583950&norender=1&count=500") as url:
    data = json.loads(url.read().decode())
for entry in data['results']:
    card_rare.append(entry['name'])
"""

total = 0
for cost in price:
    if cost in hero_list:
        total += price[cost]
    else:
        total += 3*price[cost]
print(total)

for cost in price:
  if price[cost] - price[cost]/1.15 < 0.02:
    price[cost] -= 0.02
  else:
    price[cost] = price[cost]/1.15

total_hero_rare = 0
total_hero_uncommon = 0 
total_hero_common = 0
total_item_rare = 0
total_item_uncommon = 0
total_item_common = 0
total_card_rare = 0
total_card_uncommon = 0
total_card_common = 0

for card in hero_rare:
    total_hero_rare += price[card]
avg_hero_rare = total_hero_rare/len(hero_rare)
for card in hero_uncommon:
    total_hero_uncommon += price[card]
avg_hero_uncommon = total_hero_uncommon/len(hero_uncommon)
for card in hero_common:
    total_hero_common += price[card]
avg_hero_common = total_hero_common/len(hero_common)

for card in item_rare:
    total_item_rare += price[card]
avg_item_rare = total_item_rare/len(item_rare)
for card in item_uncommon:
    total_item_uncommon += price[card]
avg_item_uncommon = total_item_uncommon/len(item_uncommon)
for card in item_common:
    total_item_common += price[card]
avg_item_common = total_item_common/len(item_common)

for card in card_rare:
    total_card_rare += price[card]
avg_card_rare = total_card_rare/len(card_rare)
for card in card_uncommon:
    total_card_uncommon += price[card]
avg_card_uncommon = total_card_uncommon/len(card_uncommon)
for card in card_common:
    total_card_common += price[card]
avg_card_common = total_card_common/len(card_common)

expected_value = 0.877*avg_card_rare+2.423*avg_card_uncommon+5.700*avg_card_common+0.195*avg_item_rare+0.538*avg_item_uncommon+1.267*avg_item_common+0.098*avg_hero_rare+0.269*avg_hero_uncommon+0.633*avg_hero_common
print(expected_value)



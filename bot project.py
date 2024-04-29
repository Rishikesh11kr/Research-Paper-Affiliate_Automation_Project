import telebot

# Replace with your actual Telegram bot token (avoid sharing publicly!)
TOKEN = '6921955802:AAHV4D1Rxbr8DUCGSojBrqXZXVJ2wxLAcyM'
bot = telebot.TeleBot(TOKEN)

# Category and subcategory data (replace placeholders with desired options)
categories = {
    'HOMEACCESSORIES': {
        'BATHROOM': ['Towels', 'Bathrobes', 'Bathroom Organizers'],
        'KITCHEN': ['Utensils', 'Cookware', 'Food Storage Containers'],
        'LIVINGROOM': ['Cushions', 'Throws', 'Decorative Items'],
        'BEDROOM': ['Bedding Sets', 'Pillows', 'Mattress Protectors']
    },
    'BEAUTYPRODUCTS': {
        'SKINCARE': ['Moisturizers', 'Sunscreen', 'Cleansers'],
        'MAKEUP': ['Foundations', 'Eye Shadow', 'Lipstick'],
        'HAIRCARE': ['Shampoo', 'Conditioner', 'Hair Styling Products'],
    },
    'CLOTHING': {
        'MENSWEAR': ['Shirts', 'T-shirts', 'Jeans'],
        'WOMENSWEAR': ['Dresses', 'Blouses', 'Skirts'],
        'SPORTSWEAR': ['Tracksuits', 'Leggings', 'Activewear']
    },
}

# Links and information for bath accessories
bedroom_links = """
BEDSHEETS :-

1. Percale Floral Bedsheet & Pillow Covers Set (Clared Red)
https://amzn.to/3W9WzKO

2. Krishnam Home 300TC Glace Printed Cotton Bedsheet for Double Bed purple
https://amzn.to/3W2DD0A

LAMPS:- 

1. G Gojeeva New Wooden LED Table Lamp With Creative Laser Cutting Design
https://amzn.to/4a0Nt6F

2. NYRWANA Table Lamp, LED Rechargeable Lamp, Lamps for Home Decoration, Night Lamp
https://amzn.to/3W7hJt3

SOME USEFULL THINGS:-

1. Mobile Phone Charging Stand
https://amzn.to/3w0iBF9
"""

bathroom_links ="""

TOWELS:- 

1. Amazon Brand - Solimo - Cotton Bath Towel dark grey 
https://amzn.to/3wb16C5

2. COMFORT WEAVE Cotton Bath Towels 250 GSM Multicolor(Set of 5, 31 X 62 Inch)
https://amzn.to/3w7wpO8

SOME USEFUL THINGS:- 

1. Plantex Aluminium Towel Rack/Towel Rod/Towel Hanger with Hooks/Bathroom Organizer
https://amzn.to/4aHXcQ6

2. HOUSE OF VIPA Plastic Bathroom Accessories, Bathroom Rack, Bathroom Shelf Organizer, Wall Mounted Shelf
https://amzn.to/3Jy807r

3. 20Pack Disposable Shower Drain Hair Catcher, Drain Hair Catcher Waterproof Mesh Stickers
https://amzn.to/3U9wIA0"""

kitchen_links = """
SOME USEFULL THINGS FOR KITCHEN:- 

1. Clazkit Large Stainless Steel Cutting Board Vegetable
https://amzn.to/49MMXJg

2. FEMINA FASHION HUB Portable Electronic Digital Food Weighting Scale Weight Machine With Back light LCD Display
https://amzn.to/49T5t2M

3. GANESH Stainless Steel Potato Crusher Vegetable Smasher
https://amzn.to/4aXQCVm

4. Maloren Tap Extension For Sink Kitchen Gadgets Adjustable Water Saving Faucet Home 360
https://amzn.to/4b4eEOA

5. wolpin Plastic Kitchen Dustbin Modern Lightweight Cabinet Door Hanging Garbage Bin
https://amzn.to/49Jz4eP

"""
livingroom_links = """
CARPETS:-

1. Export Quality Hand Tufted Woolen Rugs in Classical & Vintage Pattern for Living Room
https://amzn.to/3UnwXsG

3. MUEZZA CARPETS_Soft Fluffy Shag Area Rugs for Living Room, Shaggy Floor Carpet
https://amzn.to/3Upqf5p

CLOCKS:- 

1. Non Ticking Silent Quartz Clock for Living Room
https://amzn.to/44eWlUU

2. Kadio Analog 24.5 cm X 24.5 cm Wall Clock (Brown, with Glass, Standard)
https://amzn.to/3xO8R1y

WALL DECOR:- 

1. RIZIK STORE Metal Abstract Figures Wall Sculpture For Home Decor, Living Room & Bedroom(Multicolour)
https://amzn.to/3Upqj59

2. Gold Metal Wall Decor Leaf Wall Hanging Decoration, Set of 3 Metal Wall Art Home Decor
https://amzn.to/4b0GJ9r"""

skincare_links = """
FACE WASH:- 

1. Neutrogena Deep Clean Foaming Cleanser- Advanced Face Wash
https://amzn.to/3W4Lj2k

2. Lakme Blush & Glow Hydrating Strawberry Facewash, with Vitamin C Serum
https://amzn.to/3W89Jbs

MOISTURIZER:- 

1. Dot & Key Ceramides Moisturizer with Hyaluronic for Intense Moisturizing and Skin Strengthening
https://amzn.to/3U4VLV6

2. Neutrogena Hydro Boost Hyaluronic Acid Face Moisturizer 50ml
https://amzn.to/3W89QUq

FACE CREAM

1. Olay Total Effects Day Cream with SPF 15 | Fights 7 Signs of Ageing
https://amzn.to/3vR5d6p

2. Mamaearth Vitamin C Daily Glow Face Cream With Vitamin C & Turmeric For Skin Illumination
https://amzn.to/3Q9SS42"""

haircare_links = """
SHAMPOO:-

1.Plum Coconut Shampoo for Dull Hair with Coconut Milk and Peptides for Strong & Shiny Hair
https://amzn.to/49EUwl6

2.L'OREAL PROFESSIONNEL PARIS Absolut Repair Shampoo For Damaged & Weakend Hair
https://amzn.to/4b6PgId

CONDITIONER:- 

1. L'Oreal Paris Hyaluron Moisture 72H Moisture Sealing Conditioner, For Dry & Dehydrated Hair
https://amzn.to/49Gh7xz

2. Tresemme Keratin Smooth, Conditioner, 190ml, for Smoother, Shinier Hair
https://amzn.to/4b3kzn3

HAIR WAX:- 

1. Set Wet Hair Wax For Men - Hair Clay Wax 60g
https://amzn.to/4dgMzWq

2. Dapr. Advanced Hair Pomade (100g), Wet Or Matte Look
https://amzn.to/3UpuYnx"""

makeup_links= """
FOUNDATION:- 

1. Lakme 9 to 5 Primer + Matte Perfect Cover Liquid Foundation
https://amzn.to/4aHIJUn

2. Maybelline New York Liquid Foundation, Matte & Poreless, Full Coverage Blendable Normal to Oily Skin
https://amzn.to/3U5MoEs

LIPSTICKS:-

1. Maybelline Liquid Lipstick, High Shine Gloss
https://amzn.to/3JwLuMc

2. Maybelline New York Liquid Matte Lipstick, Long Lasting
https://amzn.to/446cb3Y

EYE MACKUP:-

1. Maybelline New York Volume Express Colossal Mascara
https://amzn.to/3Js8HiI

2. Just Herbs Eyeshadow Palette 9 in 1 Long Lasting Blendable Eye Makeup Palette
https://amzn.to/3JtXgac"""

menswear_links="""
SHIRTS:-

1. U.S. POLO ASSN. Men Solid Pattern BLUE
https://amzn.to/44f99KP

2. Leriya Fashion Shirt for Men | Tropical Leaf Printed Rayon Shirts for Men | Preppy Short Sleeves
https://amzn.to/3WpRNcv

T-SHIRTS:-

1. U.S. POLO ASSN. Men's Slim Fit T-Shirt
https://amzn.to/49EUHNi

2. Nora Nico Round Neck Half Sleeve 100% Cotton Tshirt
https://amzn.to/49Pu1tc

JEANS:-

1. The Indian Garage Co Men's Slim Fit Jeans
https://amzn.to/3vZ5KDi

2. Billford Men Relaxed Waist Standard Length Cotton Men's Tapered Fit Carrot Jeans
https://amzn.to/3JpGXeu
"""
womenswear_links= """
KURTA:-

1. LetsDressUp Rayon Kurti Upto 8XL | Printed Kurti Kurti | Plus Size
https://amzn.to/4b4eoz6

2. Yash Gallery Women's Cotton & Cotton Slub Ikat Printed Anarkali Kurta (Black)
https://amzn.to/4aGntyx

JEANS:- 

1.INKD Women's Stretchable Flare Jeans
https://amzn.to/3xKxFau

2. KOTTY Women High Rise Cotton Lycra Blend Ankle Length Jeans
https://amzn.to/446ewvS

TOP:- 

1. Van Heusen Women's Half Sleeve Solid V-Neck Formal Regular Fit Top
https://amzn.to/3U9xQDK

2. Leriya Fashion Rayon Vibrant Floral Printed Long Cuff Sleeves Button Closure Mandarin Collar Fancy Shirt
https://amzn.to/3JpMKB1
"""
sportswear_links= """
SHORTS:- 

1.COMFORTABLY DUMB Men's Polyester Quick Dry Lightweight
https://amzn.to/3Jo1iB8

2. CBlue Men's Outdoor Quick Dry Lightweight Sports Shorts Zipper Pockets
https://amzn.to/3Qc4V0y

YOGA & EXERCISE SET:- 

1. Women Running and Exercise GYM & Yoga Set
https://amzn.to/3JsN3ek

2. RiCREATION Women Sports Bra and Tights set
https://amzn.to/3Jqpanx

UPPER:- 

1. Glito Men's White Side Stripe Black Bomber Upper/Jacket With Side Pocket
https://amzn.to/3JnV6sV

2. forbro Polyester Lycra blend Regular Fit Upper Jacket for men branded
https://amzn.to/3JqpfaP
"""

help_message = """Welcome to the shopping bot!

Here are the available commands:
- /start: Start the bot and display the main menu.
- /help: Display this help message.

To navigate:
- Simply type the category name (e.g., BATH, KITCHEN) to see its subcategories.
- Type the subcategory name to view its items.
- Type 'Back to Categories' to return to the main menu.

Enjoy shopping!"""

@bot.message_handler(commands=['/start'])
def start(message):
    welcome_message = "Hi there! Welcome to AffiliateAutomationProject.\n"
    category_buttons = []
    for category, subcategories in categories.items():
        category_buttons.append(telebot.types.KeyboardButton(category))
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*category_buttons)
    bot.reply_to(message, welcome_message, reply_markup=markup)

@bot.message_handler(func=lambda message: True)  # Handle all other messages
def handle_selection(message):
    selected_category = message.text
    if selected_category in categories:  # Standard category selection
        subcategory_buttons = []
        for subcategory in categories[selected_category]:
            subcategory_buttons.append(telebot.types.KeyboardButton(subcategory))
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(*subcategory_buttons)
        markup.add("Back to Categories")
        bot.reply_to(message, "Here are the subcategories in " + selected_category, reply_markup=markup)
    elif selected_category == 'BATHROOM':
        bot.reply_to(message, "HERE ARE THE LINKS OF BATHING ACCESSORIES:\n"+ bathroom_links)
    elif selected_category == 'KITCHEN':
        bot.reply_to(message, "HERE ARE THE LINKS OF KITCHEN ACCESSORIES:\n"+ kitchen_links)
    elif selected_category == 'LIVINGROOM':
        bot.reply_to(message, "HERE ARE THE LINKS OF LIVINGROOM ACCESSORIES:\n"+ livingroom_links)
    elif selected_category == 'BEDROOM':
         bot.reply_to(message, "HERE ARE THE LINKS OF BEDROOM ACCESSORIES:\n" + bedroom_links)
    elif selected_category == 'SKINCARE':
        bot.reply_to(message, "HERE IS THE LINKS OF SKINCARE PRODUCT:\n"+ skincare_links)
    elif selected_category == 'MAKEUP':
        bot.reply_to(message, "HERE ARE LINKS OF MACKUP PRODUCTS:\n"+ makeup_links)
    elif selected_category == 'HAIRCARE':
        bot.reply_to(message, "HERE ARE THE LINKS OF HAIRCARE PRODUCTS:\n"+ haircare_links)
    elif selected_category == 'MENSWEAR':
        bot.reply_to(message, "HERE ARE THE LINKS OF MENSWEAR PRODUCTS:\n"+ menswear_links)
    elif selected_category == 'WOMENSWEAR':
        bot.reply_to(message, "HERE ARE THE LINKS OF MENSWEAR PRODUCTS:\n"+ womenswear_links)
    elif selected_category == 'SPORTSWEAR':
        bot.reply_to(message, "HERE ARE THE LINKS OF SPORTWEAR PRODUCTS:\n"+ sportswear_links)
    elif selected_category.lower() == '/help':
        bot.reply_to(message, help_message) 
    elif selected_category.lower() == 'back to categories':
        start(message)  # Go back to the main menu
    elif selected_category == '/start':
        # User pressed start again, repeat welcome message
        start(message)
    else:
        bot.reply_to(message, "Invalid selection. Please choose a category or subcategory.")

# Remove any existing webhook (optional to avoid conflicts)
bot.delete_webhook()

# Start polling
bot.polling() 

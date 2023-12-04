from flask import Flask, jsonify

app = Flask(__name__)

# Updated JSON data with ratings in the menu categories
restaurant_data = {
    "restaurant": {
        "name": "Epicurean Symphony",
        "location": {
            "address": "123 Gourmet Avenue, Culinary Metropolis",
            "latitude": 40.7128,
            "longitude": -74.0060
        },
        "chef": {
            "name": "Chef Isabella Culinary Maestro",
            "bio": "An internationally renowned chef with a flair for creating culinary masterpieces that transcend borders.",
            "signature_dish": "Mango Tango Fusion"
        },
        "awards": [
            {
                "year": 2023,
                "organization": "Michelin Guide",
                "award": "Three Michelin Stars"
            },
            {
                "year": 2022,
                "organization": "James Beard Foundation",
                "award": "Outstanding Chef of the Year"
            },
            {
                "year": 2021,
                "organization": "World's 50 Best Restaurants",
                "award": "Top 5 Restaurants Worldwide"
            }
        ],
        "ambiance": {
            "description": "Epicurean Symphony offers a sophisticated and cozy ambiance, with contemporary decor and soft lighting, creating the perfect setting for an unforgettable dining experience."
        },
        "sustainability": {
            "initiatives": [
                {
                    "name": "Farm-to-Table",
                    "description": "We source our ingredients locally to support farmers and ensure the freshest, seasonal produce in our dishes."
                },
                {
                    "name": "Waste Reduction",
                    "description": "We prioritize reducing food waste through careful portioning, composting, and recycling practices."
                },
                {
                    "name": "Ocean-Friendly Seafood",
                    "description": "We are committed to serving sustainably sourced seafood to promote the health of our oceans and marine life."
                }
            ]
        },
        "events": {
            "upcoming_events": [
                {
                    "name": "Culinary Artistry Showcase",
                    "date": "2023-12-15",
                    "description": "Join us for a night of culinary artistry as Chef Isabella presents her latest creations in an exclusive tasting event."
                },
                {
                    "name": "Wine and Dine Pairing Night",
                    "date": "2024-01-20",
                    "description": "Indulge in an evening of exquisite wine and food pairings, curated by our sommelier and Chef Isabella."
                }
            ]
        },
        "online_presence": {
            "website": "https://www.epicureansymphony.com",
            "social_media": {
                "facebook": "https://www.facebook.com/epicureansymphony",
                "instagram": "https://www.instagram.com/epicureansymphony",
                "twitter": "https://www.twitter.com/epicureansymph"
            }
        },
        "menu": {
            "categories": [
                {
                    "name": "Artisanal Appetizers",
                    "items": [
                        {
                            "name": "Mango Tango Ceviche",
                            "description": "Fresh ceviche with mango, avocado, and citrus-infused seafood medley.",
                            "price": 32.99,
                            "ingredients": ["Sea bass", "Shrimp", "Mango", "Avocado"],
                            "nutritional_info": {
                                "calories": 280,
                                "protein": 20,
                                "carbohydrates": 15,
                                "fat": 18
                            },
                            "seasonal_availability": ["Year-round"],
                            "rating": 4.8
                        },
                        {
                            "name": "Truffle Butter Escargot",
                            "description": "Escargot baked in truffle butter, served with garlic-infused baguette.",
                            "price": 28.99,
                            "ingredients": ["Escargot", "Truffle butter", "Baguette", "Garlic"],
                            "nutritional_info": {
                                "calories": 350,
                                "protein": 15,
                                "carbohydrates": 25,
                                "fat": 22
                            },
                            "seasonal_availability": ["Year-round"],
                            "rating": 4.5
                        }
                    ]
                },
                {
                    "name": "Global Fusion Entrees",
                    "items": [
                        {
                            "name": "Saffron-Spiced Chicken Tikka Masala",
                            "description": "Tender chicken tikka in a rich saffron-infused tomato curry, served with basmati rice.",
                            "price": 42.99,
                            "ingredients": ["Chicken tikka", "Saffron curry", "Basmati rice", "Naan bread"],
                            "nutritional_info": {
                                "calories": 480,
                                "protein": 25,
                                "carbohydrates": 40,
                                "fat": 28
                            },
                            "seasonal_availability": ["Year-round"],
                            "customizable_options": ["Spice level: Medium", "Add coconut milk"],
                            "rating": 4.9
                        },
                        {
                            "name": "Chimichurri-Infused Argentinian Ribeye",
                            "description": "Grilled ribeye steak marinated in zesty chimichurri sauce, served with sweet potato puree.",
                            "price": 56.99,
                            "ingredients": ["Ribeye steak", "Chimichurri sauce", "Sweet potato puree", "Grilled vegetables"],
                            "nutritional_info": {
                                "calories": 600,
                                "protein": 40,
                                "carbohydrates": 30,
                                "fat": 45
                            },
                            "seasonal_availability": ["Year-round"],
                            "rating": 4.7
                        }
                    ]
                },
                {
                    "name": "Epicurean Indulgences",
                    "items": [
                        {
                            "name": "Passion Fruit Cheesecake",
                            "description": "Creamy cheesecake with a tropical twist of passion fruit, topped with mango coulis.",
                            "price": 18.99,
                            "ingredients": ["Cream cheese", "Passion fruit", "Mango coulis", "Graham cracker crust"],
                            "nutritional_info": {
                                "calories": 380,
                                "protein": 8,
                                "carbohydrates": 35,
                                "fat": 25
                            },
                            "seasonal_availability": ["Year-round"],
                            "rating": 4.6
                        },
                        {
                            "name": "Chocolate Hazelnut Decadence",
                            "description": "Decadent chocolate hazelnut mousse layered with hazelnut praline, served with espresso gelato.",
                            "price": 24.99,
                            "ingredients": ["Chocolate hazelnut mousse", "Hazelnut praline", "Espresso gelato"],
                            "nutritional_info": {
                                "calories": 450,
                                "protein": 10,
                                "carbohydrates": 40,
                                "fat": 30
                            },
                            "seasonal_availability": ["Year-round"],
                            "rating": 4.8
                        }
                    ]
                }
            ],
            "seasonal_menu": {
                "name": "Seasonal Symphony",
                "items": [
                    {
                        "name": "Butternut Squash Sage Risotto",
                        "description": "Creamy risotto with roasted butternut squash, sage, and Parmesan cheese.",
                        "price": 36.99,
                        "ingredients": ["Arborio rice", "Butternut squash", "Sage", "Parmesan cheese"],
                        "nutritional_info": {
                            "calories": 420,
                            "protein": 10,
                            "carbohydrates": 60,
                            "fat": 18
                        },
                        "seasonal_availability": ["Fall"],
                        "rating": 4.5
                    },
                    {
                        "name": "Mango Coconut Basil Sorbet",
                        "description": "Refreshing sorbet with the tropical combination of mango, coconut, and fresh basil.",
                        "price": 14.99,
                        "ingredients": ["Mango", "Coconut milk", "Basil", "Simple syrup"],
                        "nutritional_info": {
                            "calories": 180,
                            "protein": 1,
                            "carbohydrates": 40,
                            "fat": 0
                        },
                        "seasonal_availability": ["Summer"],
                        "rating": 4.7
                    }
                ]
            }
        },
        "reviews": [
            {
                "customer_name": "CulinaryExplorer",
                "rating": 5,
                "comment": "Epicurean Symphony takes gastronomy to new heights. Chef Isabella's creations are a culinary masterpiece."
            },
            {
                "customer_name": "FoodieConnoisseur",
                "rating": 4.5,
                "comment": "An epicurean delight! The fusion of flavors in every dish is simply extraordinary."
            },
            {
                "customer_name": "GourmetGlobetrotter",
                "rating": 5,
                "comment": "Exceptional service, world-class cuisine, and a dining experience that lingers on the palate."
            }
        ]
    }
}


@app.route('/', methods=['GET'])
def home():
    # Extracting relevant information for the home page
    restaurant_name = restaurant_data['restaurant']['name']
    chef_name = restaurant_data['restaurant']['chef']
    awards = restaurant_data['restaurant']['awards']
    review = restaurant_data['restaurant']['reviews']
    upcoming_event = restaurant_data['restaurant']['events']
    sustainability_initiatives = restaurant_data['restaurant']['sustainability']['initiatives']
    ambiance_description = restaurant_data['restaurant']['ambiance']['description']

    # Extracting top three dishes by rating
    menu_categories = restaurant_data['restaurant']['menu']['categories']
    top_dishes_by_rating = get_top_dishes_by_rating(menu_categories, 3)

    # Constructing the response
    response = {
        "restaurant_name": restaurant_name,
        "chef_name": chef_name,
        "awards": awards,
        "review": review,
        "upcoming_event": upcoming_event,
        "sustainability_initiatives": sustainability_initiatives,
        "ambiance_description": ambiance_description,
        "top_dishes_by_rating": top_dishes_by_rating
    }

    return jsonify(response)



@app.route('/footer', methods=['GET'])
def footer():
    online_presence = restaurant_data['restaurant']['online_presence']
    location = restaurant_data['restaurant']['location']


    footer_response = {
        "online_presence": online_presence,
        "location": location
    }

    return jsonify(footer_response)

@app.route('/all_items', methods=['GET'])
def all_items():
    # Extracting all items in all categories
    menu_categories = restaurant_data['restaurant']['menu']['categories']
    all_items_list = []

    for category in menu_categories:
        for item in category['items']:
            all_items_list.append({
                "category": category['name'],
                "item_name": item['name']
            })

    return jsonify(all_items_list)


@app.route('/menu', methods=['GET'])
def formatted_menu():
    # Extracting menu data
    categories = restaurant_data['restaurant']['menu']['categories']
    seasonal_menu = restaurant_data['restaurant']['menu']['seasonal_menu']['items']

    # Constructing the formatted menu
    formatted_menu = {
        "category": [],
        "Seasonal": []
    }

    for category in categories:
        formatted_category = {
            "name": category["name"],
            "items": category["items"]
        }
        formatted_menu["category"].append(formatted_category)

    for seasonal_item in seasonal_menu:
        formatted_seasonal_item = {
            "seasonName": seasonal_item["seasonal_availability"][0],
            "items": [seasonal_item]
        }
        formatted_menu["Seasonal"].append(formatted_seasonal_item)

    return jsonify(formatted_menu)


def get_top_dishes_by_rating(menu_categories, top_n):
    top_dishes = []

    for category in menu_categories:
        for item in category['items']:
            top_dishes.append({
                "name": item['name'],
                "rating": item['rating']
            })

    top_dishes = sorted(top_dishes, key=lambda x: x['rating'], reverse=True)[:top_n]
    return top_dishes

if __name__ == '__main__':
    app.run(debug=True)

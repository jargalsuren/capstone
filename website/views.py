from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Ingredients, Recipe
from . import db
import json

views = Blueprint('views', __name__)


def insert():
    Recipes = [
        [1, "Caesar Salad Roast Chicken",  "Salad", "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Zm9vZHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60", 50,
         "Place a rack in lower third of oven preheat to 450¬∞F. Whisk anchovies, garlic, 3 Tbsp. mayonnaise, 1 Tbsp. mustard, 1 Tbsp. oil, and 1¬Ω tsp. pepper in a small bowl. Set aside 1 Tbsp. anchovy mayo in another small bowl.Pat chicken dry season outside and inside all over with salt. Arrange breast side up in a cast-iron skillet and tuck wings underneath. Arrange shallots around(if using legs, nestle under and around) season with salt and pepper. Brush remaining anchovy mayo all over chicken, making sure to get it into the nooks and crannies, then brush shallots with any leftover anchovy mayo.Place chicken in oven so legs are facing toward the back (this is the hottest part of the oven and will help the legs cook before the breast dries out) and roast until some anchovy mayo and fat begin to drip onto shallots, about 15 minutes. Remove from oven and , using tongs, turn shallots to coat in drippings. Return skillet to oven and continue to roast chicken, stirring shallots once or twice, until golden brown and an instant-read thermometer inserted into the thickest part of breast registers 155¬∞F, 45‚Äì55 minutes. If skin starts to get too dark on the top before chicken is done, tent area with foil, leaving the rest of the bird exposed. If using chicken legs, start checking at 40 minutes (a thermometer inserted right at the joint should register 160¬∞F). Transfer chicken and shallots to a cutting board, leaving behind any juices and fat in skillet. If shallots need more time to soften and darken, roast a bit longer without chicken before proceeding. Reserve skillet. Reduce oven temperature to 400¬∞F. Finely grate half of zest of 1 lemon into a large bowl cut lemon in half and squeeze in juice. Add reserved 1 Tbsp. anchovy mayo, remaining 3 Tbsp. mayo, and remaining 1 Tbsp. oil and whisk to combine, then stir in Parmesan. Season with salt and pepper. Set dressing aside. Add bread to reserved skillet with fat and turn to coat. Return skillet to oven and toast bread, tossing halfway through, until golden brown and crisp, 12‚Äì15 minutes. Transfer croutons to bowl with reserved dressing. Add romaine and gently toss until lettuce is well coated. Season salad with salt and pepper. Slice remaining lemon into wedges. Carve chicken and nestle back into skillet or transfer to a platter arrange shallots and lemon wedges around. Serve with salad and more mustard alongside."],
        [2, "Shrimp Creole", "Seafood", "https://images.unsplash.com/photo-1515443961218-a51367888e4b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fHNocmltcCUyMG1lYWx8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60", 40,
         "In a large heavy kettle cook garlic, onions, celery, and bell peppers in oil over moderately low heat, stirring occasionally, until softened. Add all remaining ingredients except shrimp and simmer, uncovered, 30 minutes, or until thickened. Stir in shrimp and cook, covered, over moderately high heat, stirring occasionally, until shrimp are cooked through, about 5 minutes. Serve shrimp and sauce over cooked rice."],
        [3, "Mango Curry", "Indian", "https://images.unsplash.com/photo-1600703090366-f68fd1d8df1b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8bWFuZ28lMjBjdXJyeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60", 40,
         "In a bowl, combine mangoes, shallots, green chiles, ginger, garlic, vinegar, and salt and mix well. Set aside for 2 hours. In a large saucepan, combine mango mixture and coconut milk and bring to a boil. Reduce heat and simmer for 5 minutes, or until mangoes are softened. Have a splash guard and measured spices nearby. Heat oil in a small frying pan over medium-high heat until nearly smoking. Immediately reduce heat to medium. (You can test the heat of the oil by dropping in a couple of seeds. The oil is at the correct temperature when the seeds crackle, but do not burn.) Add mustard seeds and temper for a few seconds, until they stop popping. (Cover with the splash guard, if needed.) Add red chiles and curry leaves and cook for 15‚Äì20 seconds. Add the tempered spice mixture to the saucepan and stir to combine. Garnish with fried onions(if using). Serve with rice. Tempering is a traditional method of extracting optimal flavor from Indian spices, and it is a skill learned with practice! Reducing the heat a little before adding the spices prevents the spices from burning and adding a bitterness to your dish. If they do burn, simply start again with fresh spices."]
    ]

    for recipe in Recipes:
        db.session.add(Recipe(id=recipe[0], name=recipe[1], category=recipe[2],
                              photo=recipe[3], duration=recipe[4], instruction=recipe[5]))

    db.session.commit()


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # insert()
    recipes = db.session.query(Recipe).all()
    return render_template("home.html", user=current_user, recipes=recipes)

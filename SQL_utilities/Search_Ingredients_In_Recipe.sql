SELECT ingredients.name, ingredients.buy_where
FROM ingredients
JOIN recipe_breakdown ON ingredients.id = recipe_breakdown.ingredient_id
JOIN recipes ON recipes.id = recipe_breakdown.recipe_id
WHERE recipes.name = "Salade Estivale"


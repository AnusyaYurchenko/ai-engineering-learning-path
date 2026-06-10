from openai import OpenAI
import json

client = OpenAI()


def get_completion(prompt, system_prompt="You are a helpful assistant.", json_mode=False):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"} if json_mode else None,
    )
    return response.choices[0].message.content


user_inputs = {
    "people": 2,
    "days": 7,
    "daily_calories": 2000,
    "allergens": ["peanuts", "shellfish"],
    "budget_usd": 110,
    "pantry": ["rice", "lentils", "frozen spinach"]
}


schema_string = """
{
  "menu": [
    {
      "day": "",
      "dish": "",
      "ingredients": [],
      "calories": 0,
      "est_cost_usd": 0
    }
  ],
  "total_cost": 0
}
"""


def draft_plan(params):
    system_prompt = """You are a registered dietician who writes weekly dinner plans."""

    user_prompt = f"""
    <instructions>
Your task is to create a {params["days"]}-day dinner plan for a family of {params["people"]} people.
- Create exactly one dinner dish for each day.
- Assign around {params["daily_calories"]} calories per person each day.
- Keep your estimated total cost less than or equal to ${params["budget_usd"]}.
- One or more family members have the following allergies: {", ".join(params["allergens"])}.
- Do not include any of these allergens in your plan.
- IMPORTANT: we already have these ingredients on hand: {", ".join(params["pantry"])}.
- Use as many pantry items as you reasonably can while still meeting the other constraints.
    </instructions>

    <schema>
Return your answer as pure JSON with no markdown and no comments.
The JSON must match exactly this schema:
{schema_string}
    </schema>
"""

    raw_json = get_completion(
        user_prompt,
        system_prompt,
        json_mode=True
    )

    return json.loads(raw_json)


def critique_plan(plan, params):
    system_prompt = """You are a stern dietary QA inspector."""

    user_prompt = f"""
    <instructions>
Here is the proposed plan as raw JSON:

{json.dumps(plan)}

Check for rule violations:

1. The total_cost must be less than or equal to {params["budget_usd"]}.
2. Each day's calories must be within ±15% of {params["daily_calories"]}.
3. NONE of these allergens may appear: {", ".join(params["allergens"])}.
4. Every pantry item ({", ".join(params["pantry"])}) must appear at least once in the week.
5. The plan must cover exactly {params["days"]} days.

Place any violation inside "fixes".

Then think of nice-to-have tweaks, such as better variety, seasonal vegetables, quicker prep, or clearer ingredients.
Put those ideas in "suggestions".
    </instructions>

    <schema>
Reply with JSON matching this schema:
{{"fixes": [], "suggestions": []}}
Output only the JSON. No markdown backticks, no comments, no extra text.
    </schema>
"""

    raw = get_completion(
        user_prompt,
        system_prompt,
        json_mode=True
    )

    return json.loads(raw)


def revise_plan(plan, fixes, suggestions, params):
    system_prompt = """You are a senior meal planner applying corrections."""

    user_prompt = f"""
    <instructions>
Your task is to apply corrections to this meal plan.

Current meal plan:
{json.dumps(plan)}

Mandatory fixes:
{json.dumps(fixes)}

Optional but welcome suggestions:
{json.dumps(suggestions)}

Apply every mandatory fix.
Use suggestions only if they do not break the rules.
The revised plan must still follow these constraints:
- It must serve {params["people"]} people.
- It must cover exactly {params["days"]} days.
- It should aim for around {params["daily_calories"]} calories per person per day.
- Its total cost must be less than or equal to ${params["budget_usd"]}.
- It must avoid these allergens: {", ".join(params["allergens"])}.
- It should use all pantry items at least once: {", ".join(params["pantry"])}.

Return the updated plan as plain JSON with the same schema and no extra text.
    </instructions>

    <schema>
Return your answer as pure JSON with no markdown and no comments.
The JSON must match exactly this schema:
{schema_string}
    </schema>
"""

    raw = get_completion(
        user_prompt,
        system_prompt,
        json_mode=True
    )

    return json.loads(raw)


def build_grocery_list(plan, pantry):
    system_prompt = """You are a helpful kitchen assistant."""

    user_prompt = f"""
    <instructions>
Using the dinner plan below, create a shopping list for one week.
Do not include anything already in the pantry: {", ".join(pantry)}.

Return JSON exactly like:
{{"shopping_list": [{{"item": "", "estimated_qty": ""}}]}}

Plan JSON:
{json.dumps(plan)}
    </instructions>
"""

    raw = get_completion(
        user_prompt,
        system_prompt,
        json_mode=True
    )

    return json.loads(raw)


MAX_PASSES = 3


def build_plan(params):
    plan = draft_plan(params)

    for _ in range(MAX_PASSES):
        critique = critique_plan(plan, params)

        if not critique["fixes"] and not critique["suggestions"]:
            break

        plan = revise_plan(
            plan,
            critique["fixes"],
            critique["suggestions"],
            params
        )

    return plan


if __name__ == "__main__":
    final_plan = build_plan(user_inputs)

    print("\nFINAL PLAN")
    print(json.dumps(final_plan, indent=2))

    groceries = build_grocery_list(final_plan, user_inputs["pantry"])

    print("\nGROCERY LIST")
    print(json.dumps(groceries, indent=2))

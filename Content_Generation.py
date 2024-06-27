import openai

# Set up the OpenAI API key
openai.api_key = 'openai-api-key'

def generate_product_description(attributes):
    prompt = f"Generate a product description based on the following attributes: {attributes}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    description = response.choices[0].text.strip()
    return description

# Example usage
product_attributes = {
    "name": "Smartphone",
    "brand": "TechBrand",
    "features": ["5G connectivity", "6.5-inch display", "128GB storage", "48MP camera"]
}
attributes_str = ', '.join([f"{key}: {value}" for key, value in product_attributes.items()])
description = generate_product_description(attributes_str)
print(description)

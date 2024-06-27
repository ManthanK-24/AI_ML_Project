from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_data(user_id):
    # Simulate user data retrieval
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "browsing_history": [1, 2, 3],
        "preferences": ["electronics", "books"]
    }
    return jsonify(user_data)

@app.route('/api/product/<int:product_id>', methods=['GET'])
def get_product_data(product_id):
    # Simulate product data retrieval
    product_data = {
        "product_id": product_id,
        "name": "Product Name",
        "attributes": ["feature1", "feature2"]
    }
    return jsonify(product_data)

if __name__ == '__main__':
    app.run(debug=True)

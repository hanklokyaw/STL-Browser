from flask import Flask, request, jsonify, render_template, send_from_directory
import pandas as pd

# Load the DataFrame with SKU information
df = pd.read_csv('SKU_Description.csv')

print(df)

# Choose "exact" or "wildcard" for search option
SEARCH_METHOD = "wildcard"

def search_sku_description(search_term, column, match_type="exact"):
    """
    Search the DataFrame based on the specified column and match type.

    Args:
        search_term (str): Term to search for.
        column (str): Column to search in ("SKU" or "Description").
        match_type (str): Match type, "exact" or "wildcard".

    Returns:
        DataFrame: Filtered DataFrame with matching rows.
    """
    search_term = search_term.strip().lower()
    if match_type == "exact":
        filtered_df = df[df[column].str.lower() == search_term]
    elif match_type == "wildcard":
        filtered_df = df[df[column].str.contains(search_term, case=False, na=False)]
    else:
        raise ValueError("Invalid match type. Use 'exact' or 'wildcard'.")
    return filtered_df

search_df = search_sku_description("tesla", "Description", match_type=SEARCH_METHOD)
print(search_df)


app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    term = request.args.get('term', '')
    column = request.args.get('column', 'SKU')
    match_type = request.args.get('match_type', 'exact')

    if column not in ['SKU', 'Description']:
        return jsonify({'error': "Invalid column. Use 'SKU' or 'Description'."}), 400

    try:
        result = search_sku_description(term, column, match_type)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    if result.empty:
        return jsonify({'error': 'No matches found'}), 404

    return jsonify(result.to_dict(orient='records'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5003)
from flask import Blueprint, request, jsonify

from models import Shoe, db

shoe_blueprint = Blueprint('shoe_api_routes', __name__, url_prefix='/api/shoe')


@shoe_blueprint.route('/all', methods=['GET'])
def get_all_shoes():
    all_shoes = Shoe.query.all()
    result = [shoe.serialize() for shoe in all_shoes]
    response = {"result":result}
    return jsonify(response)


@shoe_blueprint.route('/create', methods=['POST'])
def create_shoes():
    try:
        shoe = Shoe()
        shoe.name = request.form['name']
        shoe.slug = request.form['slug']
        shoe.image = request.form['image']
        shoe.price = request.form['price']

        db.session.add(shoe)
        db.session.commit()

        response = {'message': 'Shoe Create', 'result': shoe.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message': 'Shoe creation failed'}

    return jsonify(response)


@shoe_blueprint.route('/<slug>', methods=['GET'])
def shoe_details(slug):
    shoe = Shoe.query.filter_by(slug=slug).first()
    if shoe:
        response = {"result":shoe.serialize()}
    else:
        response = {"message":"No shoes found"}

    return jsonify(response)
import os
import csv
import ast
from flask import Blueprint,render_template, request, jsonify
from werkzeug.utils import secure_filename
from models import db, Movie
from datetime import datetime

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

# Utility function to check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    # Render the HTML template for the home page
    return render_template('index.html')


# POST route to upload CSV file
@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Process the CSV file and insert data into the database
        try:
            with open(filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        
                        # handling empty dates
                        release_date = None
                        if row['release_date']:
                            release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()

                        # Convert the 'languages' field from a list to a string for storage
                        languages = ast.literal_eval(row['languages']) if row['languages'] else []
                        languages_str = ",".join(languages) 

                        movie = Movie(
                            budget=float(row['budget']) if row['budget'] else None,
                            homepage=row['homepage'],
                            original_language=row['original_language'],
                            original_title=row['original_title'],
                            overview=row['overview'],
                            release_date=release_date, 
                            revenue=float(row['revenue']) if row['revenue'] else None,
                            runtime=float(row['runtime']) if row['runtime'] else None,
                            status=row['status'],
                            title=row['title'],
                            vote_average=float(row['vote_average']) if row['vote_average'] else None,
                            vote_count=float(row['vote_count']) if row['vote_count'] else None,
                            production_company_id=float(row['production_company_id']) if row['production_company_id'] else None,
                            genre_id=float(row['genre_id']) if row['genre_id'] else None,
                            languages=languages_str
                        )
                        db.session.add(movie)
                    except Exception as e:
                        print(f"Error processing row: {e}")
                        return jsonify({"error": f"Error processing row: {str(e)}"}), 400

                db.session.commit()

            return jsonify({"message": "File uploaded and data saved successfully"}), 201

        except Exception as e:
            print(f"Error opening or processing the file: {e}")
            return jsonify({"error": f"Error processing the file: {str(e)}"}), 500

    return jsonify({"error": "File not allowed"}), 400

# GET route to view movies with pagination, filtering, and sorting
@main.route('/movies', methods=['GET'])
def get_movies():
    # Get query parameters for pagination, filtering, and sorting
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    release_year = request.args.get('release_year', type=int) 
    language = request.args.get('language') 
    
    # Get sorting orders for release_date and vote_average
    sort_by_release_date = request.args.get('sort_by_release_date', 'asc')  # Default to ascending for release_date
    sort_by_vote_average = request.args.get('sort_by_vote_average', 'asc')  # Default to ascending for vote_average

    
    # Base query
    query = Movie.query

    # Apply filtering by release_year (extracting year from release_date)
    if release_year:
        query = query.filter(db.extract('year', Movie.release_date) == release_year)

    # Apply filtering by language (check if the language is in the comma-separated string)
    if language:
        query = query.filter(Movie.languages.like(f"%{language}%"))

    # Apply sorting by both release_date and vote_average
    if sort_by_release_date == 'asc':
        query = query.order_by(Movie.release_date.asc())
    else:
        query = query.order_by(Movie.release_date.desc())

    if sort_by_vote_average == 'asc':
        query = query.order_by(Movie.vote_average.asc())
    else:
        query = query.order_by(Movie.vote_average.desc())

    # Apply pagination
    movies = query.paginate(page=page, per_page=per_page)

    # Response
    return jsonify({
        'total': movies.total,
        'pages': movies.pages,
        'current_page': movies.page,
        'movies': [{
            'title': movie.title,
            'original_title': movie.original_title,
            'original_language': movie.original_language,
            'release_date': movie.release_date.strftime('%Y-%m-%d'),
            'rating': movie.vote_average,
            'vote_count': movie.vote_count,
            'languages': movie.languages.split(",") 
        } for movie in movies.items]
    })

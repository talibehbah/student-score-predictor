from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    results = None

    # default form values (prevents missing variable errors)
    gender = ""
    race_ethnicity = ""
    parental_level_of_education = ""
    lunch = ""
    test_preparation_course = ""
    math_score = ""
    reading_score = ""

    if request.method == 'POST':
        try:
            # collect input
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                math_score=float(request.form.get('math_score')),
                reading_score=float(request.form.get('reading_score'))
            )

            pred_df = data.get_data_as_data_frame()

            pipeline = PredictPipeline()
            results = int(round(pipeline.predict(pred_df)[0]))

            # keep form values after submit
            gender = data.gender
            race_ethnicity = data.race_ethnicity
            parental_level_of_education = data.parental_level_of_education
            lunch = data.lunch
            test_preparation_course = data.test_preparation_course
            math_score = data.math_score
            reading_score = data.reading_score

        except Exception as e:
            results = f"Error: {str(e)}"

    return render_template(
        'home.html',
        results=results,
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        math_score=math_score,
        reading_score=reading_score
    )


if __name__ == "__main__":
    app.run(debug=True)
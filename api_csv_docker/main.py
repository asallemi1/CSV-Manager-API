from flask import Flask, jsonify, request
from it.akron.csv_manager import CsvManager

app = Flask(__name__)


@app.route('/csv', methods=['GET','POST'])
def csv_api():

    csv_path = request.args.get('csv', type=str)
    action = request.args.get('action', type=str)
    rows = request.args.get('rows', type=int)

    if not csv_path:
        return jsonify({"error": "Parametro 'csv' mancante"}), 400

    if not action:
        return jsonify({"error": "Parametro 'action' mancante"}), 400

    try:
        csv_manager = CsvManager(csv_path)

        if action == "head":
            if rows:
                df = csv_manager.rows_csv("head", rows)
            else:
                df = csv_manager.rows_csv("head")
            return jsonify(df.to_dict(orient="records"))

        elif action == "tail":
            if rows:
                df = csv_manager.rows_csv("tail", rows)
            else:
                df = csv_manager.rows_csv("tail")
            return jsonify(df.to_dict(orient="records"))

        elif action == "info":
            return jsonify(csv_manager.info_csv())

        elif action == "describe":
            df = csv_manager.describe_csv()
            return jsonify(df.to_dict())

        elif action == "shape":
            shape = csv_manager.shape_csv()
            return jsonify({"rows": shape[0], "columns": shape[1]})

        elif action == "columns":
            return jsonify({"columns": list(csv_manager.columns_csv())})

        elif action == "pivot":
            # prende il body JSON
            data = request.get_json()
            if not data:
                return jsonify({"error": "JSON mancante"}), 400

            values = data.get("values")
            index = data.get("index")
            aggfunc = data.get("aggfunc")

            df = csv_manager.pivot_csv(
                values=values,
                index=index,
                aggfunc=aggfunc
            )
            return jsonify(df.to_dict(orient="records"))

        else:
            return jsonify({"error": "Action non valida"}), 400

    except FileNotFoundError:
        return jsonify({"error": "File non trovato"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
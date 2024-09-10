from flask import Flask, request, jsonify
from connection import Manage

app = Flask(__name__)

@app.route('/api/word', methods=['GET'])
def get_word_info():
    word = request.args.get('word')
    if not word:
        return jsonify({"error": "Kelime parametresi eksik"}), 400

    try:
        manager = Manage(word)
        if not manager.rslt():
            return jsonify({"error": "Kelime bulunamadı"}), 404

        meanings = manager.get_10_meanings()
        sentences = manager.get_sentences()

        return jsonify({
            "word": word,
            "meanings": meanings,
            "sentences": sentences
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        manager.close()

if __name__ == '__main__':
    app.run(port=5000)


"""
𝓢4𝓓0 𝓟4𝓢𝓗4
FULLSTACK DEVELOPER
DATE: SEPTEMBER 10 2024
GİTHUB: https://github.com/SADOx00
"""
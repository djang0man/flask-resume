import os
from resume import app

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, use_reloader=False)

if __name__ == '__main__':
    run()

from app import app
import os

app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

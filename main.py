import uvicorn
from app import app
import logging
import json


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True, reload=True)
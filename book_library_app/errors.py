from book_library_app import app


class ErrorResponse:
    def __init__(self,message: str, http_status: int):
        self.payload = {
            "success": False,
            'message': message
        }
@app.errorhandler(404)
def not_found_error(err):
    pass
from settings import db


class BookRatingsAndComments(db.Model):
    __tablename__ = 'bookRatings'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    bookId = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(254), nullable=False)
    anonymous = db.Column(db.BOOLEAN, default=False, nullable=False)


def get_all_ratings_for_book(_bookId):
    return BookRatingsAndComments.query.filter_by(bookId=_bookId).first()


def add_rating_and_comment(_userId, _bookId, _rating, _comments, _anonymous):
    if _anonymous == 'on':
        _anonymous = 1
    new_rating_and_comment = BookRatingsAndComments(userId=_userId, bookId=_bookId, rating=_rating, comments=_comments, anonymous=_anonymous)
    db.session.add(new_rating_and_comment)
    db.session.commit()


def get_average_rating_for_book(_bookId):
    totalRating = 0
    comments = BookRatingsAndComments.query.filter_by(bookId=_bookId).all()
    for comment in comments:
        totalRating = comment.rating
    return totalRating






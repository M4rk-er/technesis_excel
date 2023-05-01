import pandas as pd
import exceptions
from db.models import Product
from db.database import get_session


def create_product_in_db(name, url, price):
    if pd.isna(name) or pd.isna(url) or pd.isna(price):
        raise exceptions.EmptyTableValueExceprion
    session = get_session()
    product = Product(title=name, url=url, price=price)
    if not (session.query(Product)
            .filter_by(title=name, url=url, price=price)
            .first()):
        session.add(product)
        session.commit()
        session.close()
    return product

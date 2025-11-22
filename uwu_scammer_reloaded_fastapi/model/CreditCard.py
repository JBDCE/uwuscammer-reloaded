from sqlmodel import SQLModel, Field
from pydantic import field_validator

# I do like the file separation for separate database tables but
# i dont yet get the idea of separating the model into base and actual card classes
class CreditCardBase(SQLModel):
    card_num: str
    expiry_date: str
    cvs: int

class CreditCard(CreditCardBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    @field_validator('card_num')
    def validate_cardnum(cls, v: str):
        v = v.replace(' ', '')
        if len(v) != 16:
            # TODO Good luck figuring out issues like translating messages like this
            raise ValueError('Credit card numbers must bemust be 16 characters long')
        return v
    
    @field_validator('expiry_date')
    def validate_expiry(cls, v: str):
        if not '/' in v:
            raise ValueError('Invalid expiry format')
        items = v.split('/')
        if not len(items):
            raise ValueError('Invalid expiry format')
        month = items[0]
        year = items[1]
        try:
            month = int(month)
            year = int(year)
        except ValueError:
            raise
        # TODO validate if the card has expired
        return v

    @field_validator('cvs')
    def validate_cvs(cls, v: int):
        # TODO Figure out how to validate this. What validation do we even bother with at this time?
        return v

# Its a neat idea of creating a defined method of creating database sets like this
class CreditCardCreate(CreditCardBase):
    pass
"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

#It's a SQLAlchemy object (BaseQuery object). If we were to finish the query by adding at the end:
    # '.all()' it would be a list of Brand objects.
    #'.first()' it would be a Brand object.
    #'.first().<column name>' it would be the type of the requested column, specified in the brands table



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

#An association table is a type of table with no meaningful fields that is created to "connect" two other tables. It manages associations between 
#tables with a many-to-many relationship. 


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = Brand.query.filter(Brand.brand_id=='ram').one().name
#I'm showing the brand name, for the whole brand object, remove '.name'

# Get all models with the name "Corvette" and the brand_id "che."
q2 = Model.query.filter((Model.name=='Corvette') & (Model.brand_id=='che')).all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year<1960).all()
#I'm showing the whole model object of each of the 18 models returned (in a list)

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with "Cor."
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter((Brand.founded==1903) & (Brand.discontinued == None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded<1950)).all()

# Get any model whose brand_id is not "for."
q8 = Model.query.filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_info_all = db.session.query(Model.name, Brand.name, Brand.headquarters).join(Brand).filter(Model.year == year).all()
    
    for model_name, brand_name, hq in model_info_all: 
        print "Model: %-20s \t Brand: %-20s \t HQ: %-30s \n" % (model_name, brand_name, hq)


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""
    #For what I understood, we have to print the brands and their models, if any
    brand_summary_all = db.session.query(Brand.name, Model.name, Model.year).outerjoin(Model).order_by(Brand.name).all()
    brands = sorted(set([brand[0] for brand in brand_summary_all]))

    for one_brand in brands:
        print "Brand: %-20s \n" %one_brand
        for a_brand, model, year in brand_summary_all:
            if a_brand == one_brand:
                if model is not None:
                    print "\t Model: %-20s \t Year of model: %d \n" % (model, year)
                else:
                    print "\t Model: -- \t\t\t Year of model: -- \n"


#SELECT brands.name FROM brands LEFT JOIN models USING(brand_id) GROUP BY(brand_id) ORDER BY(brand_id);
#db.session.query(Brand.name).outerjoin(Model).group_by(Brand.brand_id).order_by(Brand.name).all()

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""
    #I'm assuming the search IS case sensitive

    return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()


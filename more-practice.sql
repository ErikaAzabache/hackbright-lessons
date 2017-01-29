-- Include your solutions to the More Practice problems in this file.

-- INSERT BRAND
INSERT INTO brands (brand_id, name, founded, headquarters) VALUES ('sub', 'Subaru', 1953, 'Tokyo, Japan');

-- INSERT MODELS
    --model_id | year | brand_id | name
    --2015 Chevrolet Malibu, and the 2015 Subaru Outback.
INSERT INTO models (year, brand_id, name)
  SELECT 2015, brand_id, 'Malibu'
  FROM brands
  WHERE name = 'Chevrolet';

INSERT INTO models (year, brand_id, name)
  SELECT 2015, brand_id, 'Outback'
  FROM brands
  WHERE name = 'Subaru';

-- CREATE AWARDS TABLE
    --id (which should be a primary key), name, year, and winner_id.
CREATE TABLE awards (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
year INTEGER NOT NULL,
winner_id INTEGER REFERENCES models(model_id));

-- INSERT AWARDS

    -- Name: IIHS Safety Award
    -- Year: 2015
    -- Winner ID: the id for 2015 Chevrolet Malibu

INSERT INTO awards (name, year, winner_id)
  SELECT 'IIHS Safety Award', 2015, models.model_id
  FROM models JOIN brands ON brands.brand_id=models.brand_id
  WHERE models.year = 2015 AND brands.name = 'Chevrolet' AND models.name = 'Malibu';

    -- Name: IIHS Safety Award
    -- Year: 2015
    -- Winner ID: the id for 2015 Subaru Outback

INSERT INTO awards (name, year, winner_id)
  SELECT 'IIHS Safety Award', 2015, models.model_id
  FROM models JOIN brands ON brands.brand_id=models.brand_id
  WHERE models.year = 2015 AND brands.name = 'Subaru' AND models.name = 'Outback';

    -- Name: Best in Class
    -- Year: 2015
    -- DON’T include a winner – we haven’t assigned one yet!

INSERT INTO awards (name, year)
  VALUES ('Best in Class', 2015);
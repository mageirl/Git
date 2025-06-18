CREATE DEFINER=`root`@`localhost` PROCEDURE `add_movie`(
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_release_year YEAR,
    IN p_language_id TINYINT,
    IN p_rental_duration TINYINT,
    IN p_rental_rate DECIMAL(4,2),
    IN p_length SMALLINT,
    IN p_replacement_cost DECIMAL(5,2),
    IN p_rating ENUM('G','PG','PG-13','R','NC-17'),
    IN p_special_features SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes')
)
BEGIN
    INSERT INTO film (
        title, description, release_year, language_id, rental_duration,
        rental_rate, length, replacement_cost, rating, special_features, last_update
    )
    VALUES (
        p_title, p_description, p_release_year, p_language_id, p_rental_duration,
        p_rental_rate, p_length, p_replacement_cost, p_rating, p_special_features, NOW()
    );
END
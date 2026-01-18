DELIMITER //

CREATE PROCEDURE show_client_bookings(IN v_client_id INT)
BEGIN
    SELECT 
        b.booking_id,
        c.first_name,
        c.last_name,
        r.room_number,
        r.room_type,
        b.check_in,
        b.check_out
    FROM bookings b
    JOIN clients c ON b.client_id = c.client_id
    JOIN rooms r ON b.room_id = r.room_id
    WHERE b.client_id = v_client_id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE update_room_status(IN v_room_id INT, IN v_status VARCHAR(20))
BEGIN
    -- Проверяем, что статус корректный
    IF v_status = 'Свободен' OR v_status = 'Занят' THEN
        UPDATE rooms
        SET status = v_status
        WHERE room_id = v_room_id;
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE bookings_in_period(IN start_date DATE, IN end_date DATE)
BEGIN
    SELECT 
        b.booking_id,
        c.first_name,
        c.last_name,
        r.room_number,
        r.room_type,
        b.check_in,
        b.check_out
    FROM bookings b
    JOIN clients c ON b.client_id = c.client_id
    JOIN rooms r ON b.room_id = r.room_id
    WHERE b.check_in >= start_date AND b.check_out <= end_date;
END //

DELIMITER ;

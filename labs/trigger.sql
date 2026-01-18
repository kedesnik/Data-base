DELIMITER //

CREATE TRIGGER trg_booking_insert
AFTER INSERT ON bookings
FOR EACH ROW
BEGIN
    -- меняем статус комнаты на "Занят"
    UPDATE rooms
    SET status = 'Занят'
    WHERE room_id = NEW.room_id;
END //

DELIMITER ;

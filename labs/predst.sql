
CREATE VIEW view_bookings_clients AS
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
JOIN rooms r ON b.room_id = r.room_id;


CREATE VIEW view_payments_summary AS
SELECT 
    booking_id,
    SUM(amount) AS total_paid
FROM payments
GROUP BY booking_id;


CREATE VIEW view_free_rooms AS
SELECT room_id, room_number, room_type, price
FROM rooms
WHERE status = 'Свободен';



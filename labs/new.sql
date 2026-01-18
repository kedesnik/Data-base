UPDATE view_bookings_clients
SET check_out = '2026-01-26'
WHERE booking_id = 1;

SELECT * FROM view_payments_summary;

UPDATE view_free_rooms
SET price = 3900
WHERE room_number = 104;

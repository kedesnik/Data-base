SELECT room_id, room_number, status FROM rooms WHERE room_id = 1;

INSERT INTO bookings (client_id, room_id, check_in, check_out)
VALUES (1, 1, '2026-01-30', '2026-02-02');

SELECT room_id, room_number, status FROM rooms WHERE room_id = 1;

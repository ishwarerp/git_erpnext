Hostel = doc.hostel
Room = doc.hostel_room

occupancy = frappe.db.get_value('Hostel Room', Room, ['available_beds'], as_dict=1)
occupancy = occupancy.available_beds

if occupancy is None:
    current_occupancy = 0
    new_occupancy = current_occupancy + 1
    frappe.db.set_value('Hostel Room', Room, 'available_beds', new_occupancy)
else :
    new_occupancy = int(occupancy) + 1
    frappe.db.set_value('Hostel Room', Room, 'available_beds', new_occupancy)

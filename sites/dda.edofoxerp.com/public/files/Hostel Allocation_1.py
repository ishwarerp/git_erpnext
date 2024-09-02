if doc.party_type == "Student" and doc.fee_receipt_components[0].fees_category == "Hostel Admission Fee":
    Student = doc.party
    
    #first get hostel from hostel admission
    Hostel_Admission_doc = frappe.get_doc('Hostel Admission', {'student': Student})
    Hostel = Hostel_Admission_doc.hostel
    Guardian = Hostel_Admission_doc.guardian_name
    # Hostel_Admission = frappe.db.get_value('Hostel Admission', {'student' : Student} ,['hostel', 'guardian_name'])
    # Hostel = Hostel_Admission.hostel
    # Guardian = Hostel_Admission.guardian_name
    #bed no which is available
    Available_Room = frappe.db.get_value("Hostel Room", {"hostel" : Hostel, "occupancy_limit" : [">", "0"]}, ["name"], order_by="room_no asc")
    
    Available = frappe.get_doc("Hostel Bed", {"hostel" : Hostel, "status" : "Vacant"}, order_by="bed_no asc")
    # Available_Bed = frappe.db.get_value("Hostel Bed", {"hostel" : Hostel, "status" : "Vacant"}, ["name"], order_by="bed_no asc")
    Bed = Available.name
    Room = Available.hostel_room
    
    Hostel_Allocation = frappe.get_doc({
        "doctype": "Hostel Allocation",
        "student": Student,
        "hostel" : Hostel,
        "room": Room,
        "bed" : Bed,
        "guardian_name" : Guardian,
        "status" : "Active"
    })
    Hostel_Allocation.insert()
    Hostel_Allocation.save()
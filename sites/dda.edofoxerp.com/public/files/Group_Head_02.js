frappe.ui.form.on('Site Visit Form002', {
	refresh: function(frm) {
	    	frm.add_custom_button(__("Next"), function() {

            frappe.new_doc('Site Visit Form003', {
                client: frm.doc.name
            });
	
        });
		let Field_Name = ['*'];
    frappe.call({
              method: "frappe.client.get_list",
              args: {
                doctype: "Group Head",
                fieldname : Field_Name
              },
              callback: function(response)
              {
                    frm.doc.total_area = [];
                    $.each(response.message, function(_i, e) {
            	    //Add Child to the table
                	    let child_row = frm.add_child("total_area");
                	
                	    child_row.group_head = e.name;
            	    });
                refresh_field("total_area");
              }
            });
	},
	'measurement_for':function(frm) {
		
		let Filter = '';
		
		if(frm.doc.measurement_for == "Residential")
		{
		    frm.set_query("name_of_measurement",'measurements', function() {
    			return {
    				filters: {
    					'residential': 1
    				},
    				orders:{
                        "creation": "ASC"
    				}
    			}
    		});
		}
		else
		{
		    frm.set_query("name_of_measurement",'measurements', function() {
    			return {
    				filters: {
    					'commercial': 1
    				},
    				orders:{
                        "creation": "ASC"
    				}
    			}
    		});
		}
	}
});

var Total_Area = {};
	
frappe.ui.form.on('Measurements', {
    'width':function(frm, cdt, cdn) {
		let Measurement = locals[cdt][cdn];
		
		
		Measurement.area = flt(Measurement.lengths * Measurement.width);
        
	    
	    if(!((Measurement.group_head) in Total_Area))
	    {
	        Total_Area[Measurement.group_head] = Measurement.area;
	    }
	    else
	    {
	        Total_Area[Measurement.group_head] = Total_Area[Measurement.group_head] + Measurement.area;
	    }
        
		frm.refresh_field("measurements");
    }
});
 
// frappe.ui.form.on('Total Area', {
//     on_load:function(frm, cdt, cdn) {
// 		let Total = locals[cdt][cdn];
		
		
// 		frm.refresh_field("total_area");
//     }
// });






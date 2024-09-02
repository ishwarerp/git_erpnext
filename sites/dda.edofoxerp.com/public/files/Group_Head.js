frappe.ui.form.on('Site Visit Form002', {
	onload:function(frm) {
		console.log(frm);
		let Field_Name = ['*'];
// 		let Filters = { }
		
		frappe.call({
          method: "frappe.client.get_list",
          args: {
            doctype: "Group Head",
            // filters : Filters,
            fieldname : Field_Name
          },
          callback: function(response)
          {
            console.log("response",response);
            // Handle the response
            // if (response)
            // {
                frm.fields_dict.total_area = [];
                $.each(response.message, function(_i, e) {
        	    //Add Child to the table
            	    let child_row = frm.add_child("total_area");
            	
            	    child_row.group_head = e.name;
        	    });
            refresh_field("total_area");
            // }
          }
        });
	}
});

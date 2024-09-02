# Copyright (c) 2013, Frappe
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from datetime import datetime # from python std library
from frappe.utils import add_to_date

class LibraryTransaction(Document):
	def validate(self):
		last_transaction = frappe.get_list("Library Transaction",
			fields=["transaction_type", "transaction_date"],
			filters = {
				"article": self.article,
				"transaction_date": ("<=", self.transaction_date),
				"name": ("!=", self.name)
			})
		if self.transaction_type=="Issue":
			if last_transaction and last_transaction[0].transaction_type=="Issue":
				frappe.throw(_("Article {0} {1} has not been recorded as returned since {1}".format(
					self.article, self.article_name, last_transaction[0].transaction_date
				)))
		else:
			pass
			# if not last_transaction or last_transaction[0].transaction_type!="Issue":
			# 	frappe.throw(_("Cannot return article not issued"))
   	def on_update(self):
        if(self.transaction_type == "Issue"):
            article_name = self.article
            occupation = "Issued"
            transaction_date = self.transaction_date
            loan_period_for_student = frappe.db.get_single_value('Library Management Settings', 'borrowing_period_for_student')
            loan_period_for_student = int(loan_period_for_student)
            due_date_borrow = add_to_date(transaction_date, years=0, months=0, weeks=0, days=loan_period_for_student, hours=0, minutes=0, seconds=0, as_string=False, as_datetime=False)			
            frappe.db.set_value('Article', Article_ID.name, {'occupation_status': occupation,'issue_date': transaction_date,'due_date': due_date_borrow, 'available_from': due_date_borrow})
            frappe.msgprint(
                msg = 'Book Issued Successfully to !',
                title = 'Issued Successfully'
                )
        elif(self.transaction_type == "Return"):
            article_name = self.article
            occupation = "Available"
            transaction_date = self.transaction_date
            fine_amount = self.fine_amount
            blank = ""
            frappe.db.set_value('Article', Article_ID.name, {'occupation_status': occupation, 'issue_date':blank, 'due_date': blank, 'available_from': transaction_date})
            if(fine_amount > 0):
                frappe.msgprint(
                    msg = 'Book Returned Successfully by and fine amount is : ' + fine_amount + ' !',
                    title = 'Returned Successfully'
                    )
            else:
                frappe.msgprint(
                    msg = 'Book Returned Successfully and fine amount is : ' + fine_amount + ' !',
                    title = 'Returned Successfully'
                    )
        elif(self.transaction_type == "Reserve"):
            article_name = self.article
            occupation = "Reserved"
            transaction_date = self.transaction_date
            reserve_period = frappe.db.get_single_value('Library Management Settings', 'max_reserve_days_for_student')
            reserve_period = int(reserve_period)
            due_date_reserve = add_to_date(transaction_date, years=0, months=0, weeks=0, days=reserve_period, hours=0, minutes=0, seconds=0, as_string=False, as_datetime=False)
            frappe.db.set_value('Article', Article_ID.name, {'occupation_status': occupation,'issue_date': transaction_date,'due_date': due_date_reserve, 'available_from': due_date_reserve})
            frappe.msgprint(
                msg = 'Book Reserved Successfully until date : ' + due_date_reserve + '.',
                title = 'Reserved Successfully'
                )

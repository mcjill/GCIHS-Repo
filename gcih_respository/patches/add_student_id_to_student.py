import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def execute():
    """Add custom_student_id field to Student, Patient, and Customer doctypes"""
    
    # Add custom_student_id to Student
    if not frappe.db.exists('Custom Field', {'dt': 'Student', 'fieldname': 'custom_student_id'}):
        create_custom_field('Student', {
            'label': 'Student ID',
            'fieldname': 'custom_student_id',
            'fieldtype': 'Data',
            'insert_after': 'first_name',
            'in_list_view': 1,
            'in_standard_filter': 1,
            'in_global_search': 1,
            'read_only': 0,
            'allow_on_submit': 0,
            'translatable': 0,
            'unique': 1,
            'no_copy': 0,
            'reqd': 1
        })

    # Add custom_student_id to Patient
    if not frappe.db.exists('Custom Field', {'dt': 'Patient', 'fieldname': 'custom_student_id'}):
        create_custom_field('Patient', {
            'label': 'Student ID',
            'fieldname': 'custom_student_id',
            'fieldtype': 'Data',
            'insert_after': 'patient_name',
            'in_list_view': 1,
            'in_standard_filter': 1,
            'in_global_search': 1,
            'read_only': 0,
            'allow_on_submit': 0,
            'translatable': 0,
            'unique': 1,
            'no_copy': 0,
            'reqd': 0
        })

    # Add custom_student_id to Customer
    if not frappe.db.exists('Custom Field', {'dt': 'Customer', 'fieldname': 'custom_student_id'}):
        create_custom_field('Customer', {
            'label': 'Student ID',
            'fieldname': 'custom_student_id',
            'fieldtype': 'Data',
            'insert_after': 'customer_type',
            'in_list_view': 1,
            'in_standard_filter': 1,
            'in_global_search': 1,
            'read_only': 0,
            'allow_on_submit': 0,
            'translatable': 0,
            'unique': 1,
            'no_copy': 0,
            'reqd': 0
        })
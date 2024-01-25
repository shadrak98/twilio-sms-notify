from twilio.rest import Client
import frappe

AUTH_TOKEN = frappe.db.get_single_value("Twilio Settings", "auth_token")
ACCOUNT_SID = frappe.db.get_single_value("Twilio Settings", "account_sid")
FROM = frappe.db.get_single_value("Twilio Settings", "twilio_number")

@frappe.whitelist()
def send_sms(to, body):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        to=to,
        from_=FROM,
        body=body
    )
    return message.sid

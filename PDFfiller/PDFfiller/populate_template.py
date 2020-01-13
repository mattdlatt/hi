import os
import pdfrw
import settings
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
import dropbox
import datetime
import socket


socket.getaddrinfo('localhost', 8080)
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for i in range(0,len(template_pdf.pages)-1):
        annotations = template_pdf.pages[i][ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        if key == 'FTEstart3':
                            print("hi")
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                        )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

def write_fillable_pdf2(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for i in range(0,len(template_pdf.pages)):
        annotations = template_pdf.pages[i][ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        if key == 'FTEstart3':
                            print("hi")
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                        )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

def sendEmail(input_pdf_path, output_pdf_path, data_dict, input_pdf_path2, output_pdf_path2, data_dict2):
    write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict)
    write_fillable_pdf2(input_pdf_path2, output_pdf_path2, data_dict2)
    subject = data_dict.get("name") + " " + 'Demand Wealth Financial Plan Worksheet'
    message = """Your Financial Plan and Expense Data Worksheet has been recieved, and a Demand Wealth team member will reach out to you shortly. In the meantime if you have any questions, please email info@demandwealth.com. If you would like to edit your worksheet <a href="https://demandwealth.us-east-1.elasticbeanstalk.com/load/"> Click Here </a> .

    Demand Wealth regards the confidentiality of client data to be of utmost importance and does not share data with any third party. All of your information is secured and encrypted by Amazon and Dropbox's cloud-based storage security system. This email was sent automatically."""
    email_from = settings.EMAIL_HOST_USER
    path = "/" + data_dict.get("name") + "/" +  data_dict.get("name") + " " + str(datetime.datetime.now()) + ".pdf"
    path2 = "/" + data_dict.get("name") + "/" +  data_dict.get("name") + " " + str(datetime.datetime.now()) + " " + "2" + ".pdf"
    #info@minkwealth.com
    upload(output_pdf_path, path)
    upload(output_pdf_path2, path2)
    recipient_list = [data_dict.get("email"), "info@demandwealth.com"]
    msg = EmailMessage(subject, message, email_from, recipient_list)
    msg.content_subtype = "html"
    msg.attach_file(output_pdf_path)
    msg.attach_file(output_pdf_path2)
    msg.send()



class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def upload(output, path):
    access_token = 'C6PkaRl6ViAAAAAAAAAAbnvGYaLAMjMKofG8ac0hpFA0ZrfO1bq7atc1GZAeFHhg'
    transferData = TransferData(access_token)

    file_from = output
    file_to = path
    transferData.upload_file(file_from, file_to)

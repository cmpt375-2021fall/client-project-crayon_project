import pdfkit
import platform
 
def html_to_string(html, to_file):
    if platform.system() == 'Windows':
        path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    else:
        path_wkthmltopdf = '/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_string(html, to_file, configuration=config)


 